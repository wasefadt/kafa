import streamlit as st
import sqlite3
import pandas as pd
import numpy as np
import os
import glob

# 1. إعداد الصفحة وتصميم الهوية البصرية القطرية (FutureX قطر)
st.set_page_config(page_title="المنصة الوطنية القطرية للتعلم المرن (كفاءة X)", layout="wide", initial_sidebar_state="expanded")

# تفعيل النمط العربي والاتجاه RTL والألوان المعتمدة (العنابي والأخضر الفاتح #AAD2C3)
st.markdown('''
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700&display=swap');
    html, body, [class*="css"] {
        font-family: 'Cairo', 'Arial', sans-serif;
        direction: RTL;
        text-align: right;
    }
    .main {
        background-color: #f4f7f6;
    }
    .sidebar .sidebar-content {
        direction: RTL;
        text-align: right;
    }
    h1, h2, h3 {
        color: #1b4d3e; /* الأخضر الداكن */
    }
    .stButton>button {
        background-color: #8b263e; /* العنابي القطري المعتمد */
        color: white;
        border-radius: 8px;
        padding: 8px 24px;
        border: none;
    }
    .stButton>button:hover {
        background-color: #a33851;
        color: white;
    }
    .card {
        background-color: white;
        padding: 20px;
        border-radius: 12px;
        border-right: 5px solid #AAD2C3; /* الأخضر الفاتح */
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        margin-bottom: 15px;
    }
    .card-title {
        font-weight: bold;
        color: #1b4d3e;
        margin-bottom: 8px;
    }
    .card-meta {
        font-size: 13px;
        color: #666;
    }
    .futurex-badge {
        background-color: #e3f2fd;
        color: #0d47a1;
        padding: 4px 8px;
        border-radius: 4px;
        font-size: 12px;
        font-weight: bold;
        display: inline-block;
        margin-bottom: 10px;
    }
    .timeline {
        border-right: 2px solid #AAD2C3;
        padding-right: 20px;
        margin-right: 10px;
        position: relative;
    }
    .timeline-item {
        margin-bottom: 25px;
        position: relative;
    }
    .timeline-dot {
        position: absolute;
        right: -26px;
        top: 5px;
        background-color: #8b263e;
        width: 12px;
        height: 12px;
        border-radius: 50%;
    }
    </style>
''', unsafe_allow_html=True)

db_path = "kafaah_learning.db"

# 2. بناء قاعدة البيانات سحابياً وتعبئتها تلقائياً من الـ 16 ملفاً الحقيقية مع معالجة الأخطاء الذكية
def init_database_on_demand():
    if not os.path.exists(db_path):
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        cursor.executescript("""
        CREATE TABLE IF NOT EXISTS departments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE
        );
        CREATE TABLE IF NOT EXISTS competencies (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE,
            type TEXT,
            level TEXT
        );
        CREATE TABLE IF NOT EXISTS courses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            provider TEXT DEFAULT 'Coursera',
            language TEXT,
            duration_hours INTEGER,
            difficulty_level TEXT,
            url TEXT,
            skills_covered TEXT,
            description TEXT,
            rating REAL,
            partner_name TEXT,
            scorable_skills TEXT,
            department_id INTEGER,
            competency_id INTEGER,
            FOREIGN KEY(department_id) REFERENCES departments(id),
            FOREIGN KEY(competency_id) REFERENCES competencies(id)
        );
        CREATE TABLE IF NOT EXISTS competency_course_mapping (
            competency_id INTEGER,
            course_id INTEGER,
            PRIMARY KEY(competency_id, course_id),
            FOREIGN KEY(competency_id) REFERENCES competencies(id),
            FOREIGN KEY(course_id) REFERENCES courses(id)
        );
        CREATE TABLE IF NOT EXISTS pathways (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE,
            description TEXT,
            learning_objective TEXT,
            target_audience TEXT,
            type TEXT,
            level TEXT,
            estimated_duration TEXT,
            skills_targeted TEXT,
            outcomes TEXT,
            cert_status TEXT,
            department_id INTEGER,
            competency_id INTEGER,
            FOREIGN KEY(department_id) REFERENCES departments(id),
            FOREIGN KEY(competency_id) REFERENCES competencies(id)
        );
        CREATE TABLE IF NOT EXISTS pathway_courses (
            pathway_id INTEGER,
            course_id INTEGER,
            step_order INTEGER,
            PRIMARY KEY(pathway_id, course_id),
            FOREIGN KEY(pathway_id) REFERENCES pathways(id),
            FOREIGN KEY(course_id) REFERENCES courses(id)
        );
        """)
        conn.commit()

        courses_dict = {}
        competencies_dict = {}
        depts_map = {}

        def clean_txt(val):
            if pd.isna(val): return ""
            return str(val).strip()

        def get_clean_level(val):
            val = str(val).strip()
            if 'مبتدئ' in val or 'Beginner' in val or 'BEGINNER' in val: return 'مبتدئ'
            elif 'متوسط' in val or 'Intermediate' in val or 'INTERMEDIATE' in val: return 'متوسط'
            elif 'متقدم' in val or 'Advanced' in val or 'ADVANCED' in val: return 'متقدم'
            elif 'خبير' in val or 'الخبير' in val or 'Expert' in val: return 'خبير'
            return 'متوسط'

        # استيراد برامج كورسير والمواءمة من ملفات الكفاءات
        comp_files = glob.glob("Copy of موائمة*.csv")
        for cf in comp_files:
            try:
                df = pd.read_csv(cf, skiprows=2)
            except Exception:
                try:
                    df = pd.read_csv(cf)
                except Exception:
                    continue
                
            for idx, row in df.iterrows():
                try:
                    course_name = clean_txt(row.get('Course'))
                    if not course_name or course_name == 'Course': continue
                    
                    course_url = clean_txt(row.get('Course URL'))
                    course_id = clean_txt(row.get('Course ID')) or course_name
                    subj = clean_txt(row.get('Subject'))
                    if not subj: subj = "عام"
                    
                    arabic_comp = subj
                    if 'Customer' in subj or 'خدمة' in subj: arabic_comp = "خدمة العملاء"
                    elif 'Work' in subj or 'العمل' in subj: arabic_comp = "العمل بفعالية"
                    elif 'Adaptability' in subj or 'التكيف' in subj: arabic_comp = "القدرة على التكيف"
                    elif 'Initiative' in subj or 'المبادرة' in subj: arabic_comp = "المبادرة"
                    elif 'Relationship' in subj or 'العلاقات' in subj: arabic_comp = "إدارة العلاقات"
                    elif 'Communication' in subj or 'التواصل' in subj: arabic_comp = "التواصل"
                    
                    raw_lvl = clean_txt(row.get('Unnamed: 4')) or clean_txt(row.get('Difficulty Level'))
                    level_clean = get_clean_level(raw_lvl)
                    
                    lang = clean_txt(row.get('Course Language'))
                    lang_clean = 'العربية' if ('Arabic' in lang or 'عربي' in lang) else 'الإنجليزية'
                    desc = clean_txt(row.get('Course Description'))
                    partner = clean_txt(row.get('University / Industry Partner Name'))
                    skills = clean_txt(row.get('Skills Learned'))
                    scorable = clean_txt(row.get('Scorable Skills'))
                    
                    if course_id not in courses_dict:
                        cursor.execute("""
                            INSERT INTO courses (title, provider, language, duration_hours, difficulty_level, url, skills_covered, description, rating, partner_name, scorable_skills)
                            VALUES (?, 'Coursera', ?, 12, ?, ?, ?, ?, 4.5, ?, ?)
                        """, (course_name, lang_clean, level_clean, course_url, skills, desc, partner, scorable))
                        courses_dict[course_id] = cursor.lastrowid
                        
                    if arabic_comp not in competencies_dict:
                        cursor.execute("INSERT OR IGNORE INTO competencies (name, type) VALUES (?, 'سلوكية')", (arabic_comp,))
                        cursor.execute("SELECT id FROM competencies WHERE name = ?", (arabic_comp,))
                        competencies_dict[arabic_comp] = cursor.fetchone()[0]
                        
                    try:
                        cursor.execute("INSERT INTO competency_course_mapping (competency_id, course_id) VALUES (?, ?)", (competencies_dict[arabic_comp], courses_dict[course_id]))
                    except Exception:
                        pass
                except Exception:
                    continue

        # استيراد ملفات الإدارات والمسارات التخصصية بدولة قطر
        dept_files = [
            "نظم المعلومات.xlsx_Sheet1_Table1.csv",
            "الوظائف المكتبية.xlsx_Sheet1_Table1.csv",
            "الموارد البشرية.xlsx_Sheet1_Table1.csv",
            "العلاقات العامة والإعلام.xlsx_Sheet1_Table1_(2).csv",
            "الشؤون المالية والإدارية.xlsx_Sheet1_Table1_(2).csv",
            "الشؤون القانونية.xlsx_Sheet1_Table1.csv",
            "التعاون الدولي.xlsx_Sheet1_Sheet1.csv",
            "التخطيط والجودة.xlsx_Sheet1_Table1.csv"
        ]
        
        for df_file in dept_files:
            if not os.path.exists(df_file): continue
            dept_name = df_file.split(".xlsx")[0]
            cursor.execute("INSERT OR IGNORE INTO departments (name) VALUES (?)", (dept_name,))
            cursor.execute("SELECT id FROM departments WHERE name = ?", (dept_name,))
            dept_id = cursor.fetchone()[0]
            depts_map[dept_name] = dept_id
            
            try:
                df = pd.read_csv(df_file)
            except Exception:
                continue
                
            pathway_name = f"مسار {dept_name} المتكامل"
            cursor.execute("""
                INSERT OR IGNORE INTO pathways (name, description, learning_objective, target_audience, type, level, estimated_duration, skills_targeted, outcomes, cert_status, department_id)
                VALUES (?, ?, ?, 'موظفو الإدارة الحكومية', 'تخصصية', 'تطبيقي', '45 ساعة', 'مهارات فنية متطورة', 'تأهيل ورفع الأداء المؤسسي', 'شهادة وطنية معتمدة للترقية', ?)
            """, (pathway_name, f"مسار مخصص لتطوير جدارات وكفاءات {dept_name}", f"تمكين موظفي {dept_name} من المهارات الحديثة", dept_id))
            
            cursor.execute("SELECT id FROM pathways WHERE name = ?", (pathway_name,))
            pathway_id = cursor.fetchone()[0]
            
            step_order = 1
            for idx, row in df.iterrows():
                try:
                    course_name = clean_txt(row.get('Course Name') or row.get('Course'))
                    if not course_name: continue
                    course_url = clean_txt(row.get('Course URL'))
                    course_id = clean_txt(row.get('Course ID')) or course_name
                    
                    diff_level = get_clean_level(clean_txt(row.get('Difficulty Level') or row.get('المستوى')))
                    desc = clean_txt(row.get('Course Description'))
                    partner = clean_txt(row.get('University / Industry Partner Name'))
                    skills = clean_txt(row.get('Skills Learned'))
                    scorable = clean_txt(row.get('Scorable Skills'))
                    
                    if course_id not in courses_dict:
                        cursor.execute("""
                            INSERT INTO courses (title, provider, language, duration_hours, difficulty_level, url, skills_covered, description, rating, partner_name, scorable_skills, department_id)
                            VALUES (?,
