import sqlite3
import pandas as pd
import glob
import os

db_path = "kafaah_learning.db"
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# إنشاء الجداول الأساسية
cursor.executescript("""
DROP TABLE IF EXISTS enrollments;
DROP TABLE IF EXISTS employees;
DROP TABLE IF EXISTS pathway_courses;
DROP TABLE IF EXISTS pathways;
DROP TABLE IF EXISTS competency_course_mapping;
DROP TABLE IF EXISTS courses;
DROP TABLE IF EXISTS competencies;
DROP TABLE IF EXISTS job_titles;
DROP TABLE IF EXISTS job_groups;
DROP TABLE IF EXISTS departments;

CREATE TABLE departments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE
);

CREATE TABLE competencies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    type TEXT,
    level TEXT
);

CREATE TABLE courses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    provider TEXT DEFAULT 'Coursera',
    language TEXT,
    duration_hours INTEGER,
    difficulty_level TEXT,
    url TEXT,
    skills_covered TEXT
);

CREATE TABLE competency_course_mapping (
    competency_id INTEGER,
    course_id INTEGER,
    PRIMARY KEY(competency_id, course_id),
    FOREIGN KEY(competency_id) REFERENCES competencies(id),
    FOREIGN KEY(course_id) REFERENCES courses(id)
);

CREATE TABLE pathways (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT,
    learning_objective TEXT,
    target_audience TEXT,
    type TEXT,
    level TEXT,
    estimated_duration TEXT
);

CREATE TABLE pathway_courses (
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

# استيراد برامج كورسير والمواءمة من ملفاتك الحقيقية المرفوعة
comp_files = glob.glob("Copy of موائمة*.csv")
for cf in comp_files:
    try:
        df = pd.read_csv(cf, skiprows=2)
    except Exception:
        df = pd.read_csv(cf)
        
    for idx, row in df.iterrows():
        course_name = str(row.get('Course', '')).strip()
        if not course_name or course_name == 'Course':
            continue
        
        course_url = str(row.get('Course URL', '')).strip()
        course_id = str(row.get('Course ID', '')).strip() or course_name
        comp_title = str(row.get('Subject', 'عام')).strip()
        
        if course_id not in courses_dict:
            cursor.execute("""
                INSERT INTO courses (title, provider, language, duration_hours, difficulty_level, url, skills_covered)
                VALUES (?, 'Coursera', 'العربية', 12, 'تطبيقي', ?, ?)
            """, (course_name, course_url, str(row.get('Skills Learned', '')).strip()))
            courses_dict[course_id] = cursor.lastrowid
            
        if comp_title not in competencies_dict:
            cursor.execute("INSERT OR IGNORE INTO competencies (name, type, level) VALUES (?, 'سلوكية', 'تطبيقي')", (comp_title,))
            cursor.execute("SELECT id FROM competencies WHERE name = ?", (comp_title,))
            competencies_dict[comp_title] = cursor.fetchone()[0]
            
        try:
            cursor.execute("INSERT INTO competency_course_mapping (competency_id, course_id) VALUES (?, ?)", (competencies_dict[comp_title], courses_dict[course_id]))
        except sqlite3.IntegrityError:
            pass

# استيراد الإدارات والمسارات التخصصية من ملفاتك
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
    if not os.path.exists(df_file):
        continue
    dept_name = df_file.split(".xlsx")[0]
    cursor.execute("INSERT OR IGNORE INTO departments (name) VALUES (?)", (dept_name,))
    
    df = pd.read_csv(df_file)
    pathway_name = f"مسار {dept_name}"
    
    cursor.execute("""
        INSERT OR IGNORE INTO pathways (name, description, learning_objective, target_audience, type, level, estimated_duration)
        VALUES (?, ?, ?, 'موظفو الإدارة', 'تخصصية', 'تطبيقي', '40 ساعة')
    """, (pathway_name, f"مسار مخصص لتطوير جدارات {dept_name}", f"تأهيل الكوادر الفنية في {dept_name}"))
    
    cursor.execute("SELECT id FROM pathways WHERE name = ?", (pathway_name,))
    pathway_id = cursor.fetchone()[0]
    
    step_order = 1
    for idx, row in df.iterrows():
        course_name = str(row.get('Course Name', row.get('Course', ''))).strip()
        if not course_name:
            continue
        course_url = str(row.get('Course URL', '')).strip()
        course_id = str(row.get('Course ID', '')).strip() or course_name
        
        if course_id not in courses_dict:
            cursor.execute("""
                INSERT INTO courses (title, provider, language, duration_hours, difficulty_level, url, skills_covered)
                VALUES (?, 'Coursera', 'العربية', 15, 'تطبيقي', ?, ?)
            """, (course_name, course_url, str(row.get('Skills Learned', '')).strip()))
            courses_dict[course_id] = cursor.lastrowid
            
        try:
            cursor.execute("INSERT INTO pathway_courses (pathway_id, course_id, step_order) VALUES (?, ?, ?)", (pathway_id, courses_dict[course_id], step_order))
            step_order += 1
        except sqlite3.IntegrityError:
            pass

conn.commit()
conn.close()
print("تم بناء وتجهيز قاعدة البيانات بنجاح!")
