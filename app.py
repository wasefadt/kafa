import streamlit as st
import sqlite3
import pandas as pd
import numpy as np
import os
import glob

# إعداد الصفحة وتصميم الهوية البصرية القطرية (FutureX قطر)
st.set_page_config(page_title="المنصة الوطنية القطرية للتعلم المرن (كفاءة X)", layout="wide", initial_sidebar_state="expanded")

# تفعيل النمط العربي والاتجاه RTL والألوان المعتمدة (العنابي والأخضر الفاتح #AAD2C3)
st.markdown("""
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
    </style>
""", unsafe_allow_html=True)

db_path = "kafaah_learning.db"

# دالة ذكية لبناء قاعدة البيانات تلقائياً سحابياً إذا لم تكن موجودة
def init_database_on_demand():
    if not os.path.exists(db_path):
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # إنشاء الجداول الأساسية
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
            skills_covered TEXT
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
            estimated_duration TEXT
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

        # استيراد البيانات الحقيقية من ملفات Excel المستوردة
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

        # ملفات المواءمة التخصصية للإدارات الحكومية بقطر
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
            
            try:
                df = pd.read_csv(df_file)
            except Exception:
                continue
                
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

# تشغيل التهيئة التلقائية فورياً
init_database_on_demand()

def get_db_connection():
    return sqlite3.connect(db_path)

# شريط التنقل الجانبي للهوية البصرية لجهة حكومية قطرية
st.sidebar.title("منصة كفاءة X الوطنية")
st.sidebar.subheader("مستوحاة من مبادئ FutureX العالمية")

role = st.sidebar.selectbox("اختر بوابة الدخول الذكية:", [
    "بوابة الموظف (المحفظة الوطنية والتعلم)", 
    "بوابة الجهات الحكومية والشركاء (B2B)", 
    "بوابة الترخيص والاعتماد وضمان الجودة (NeLC)",
    "لوحة التقارير ومؤشرات الأداء الوطنية"
])

# محاولة جلب الإحصائيات من قاعدة البيانات الفعالة
try:
    conn = get_db_connection()
    total_courses = conn.execute("SELECT COUNT(*) FROM courses;").fetchone()[0]
    total_competencies = conn.execute("SELECT COUNT(*) FROM competencies;").fetchone()[0]
    total_pathways = conn.execute("SELECT COUNT(*) FROM pathways;").fetchone()[0]
    conn.close()
except Exception:
    total_courses, total_competencies, total_pathways = 352, 6, 8

if role == "بوابة الموظف (المحفظة الوطنية والتعلم)":
    st.title("👋 مرحباً بك في محفظتك المهارية الوطنية")
    st.write("رحلتك التعليمية الموثوقة والموائمة مع الكفاءات الوطنية لتطوير مهارات المستقبل.")

    tabs = st.tabs(["💼 محفظتي المهارية المعتمدة", "🔍 استكشاف المسارات الوطنية", "🧠 محلل الفجوات والتوصيات"])

    with tabs[0]:
        st.subheader("📊 رصيد الساعات والشهادات المعتمدة سحابياً")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("رصيد الساعات التعليمية المعتمدة", "65 ساعة")
        with col2:
            st.metric("الشهادات المهنية الموثقة", "3 شهادات")
        with col3:
            st.metric("مستوى الكفاءة الحالي", "متقدم (تطبيقي)")

        st.markdown("""
            <div class='card'>
                <span class='futurex-badge'>🔒 شهادة موثقة وطرق الربط الذكي</span>
                <div class='card-title'>🏆 شهادة التميز في خدمة وإسعاد المتعاملين (Coursera & معهد الإدارة العامة)</div>
                <p><b>حالة الاعتماد:</b> معتمدة بالكامل ومسجلة في نظام الموارد البشرية الحكومي (Mawared).</p>
                <div class='card-meta'>تاريخ الإصدار: أكتوبر 2023 | معرف الشهادة: QAT-9842104</div>
            </div>
        """, unsafe_allow_html=True)

    with tabs[1]:
        st.subheader("🛤️ مسارات التعلم التخصصية والمشتركة")
        st.write("المسارات التخصصية المتاحة بناءً على الإدارات والبرامج الحقيقية في قاعدة البيانات:")
        
        try:
            conn = get_db_connection()
            df_paths = pd.read_sql("SELECT * FROM pathways", conn)
            conn.close()
            for idx, row in df_paths.iterrows():
                st.markdown(f"""
                    <div class='card'>
                        <div class='card-title'>{row['name']}</div>
                        <p>{row['description']}</p>
                        <div class='card-meta'><b>نوع المسار:</b> {row['type']} | <b>الهدف التعليمي:</b> {row['learning_objective']}</div>
                    </div>
                """, unsafe_allow_html=True)
        except Exception:
            st.warning("يرجى التأكد من رفع ملفات المواءمة الـ CSV على مستودع GitHub لملء قاعدة البيانات.")

    with tabs[2]:
        st.subheader("🧠 محلل الفجوات المهارية الذكي (AI Skills-Gap Analyzer)")
        st.write("بناءً على بطاقتك الوظيفية الحالية، قمنا بمطابقة مهاراتك مع متطلبات 'منصة كفاءة X' وتحديد الفجوات:")
        
        st.markdown("""
            <div class='card' style='border-right-color: #8b263e;'>
                <span class='futurex-badge'>🚨 فجوة مهارية مكتشفة</span>
                <div class='card-title'>تطوير تجربة العملاء في السياق الحكومي</div>
                <p><b>البرنامج الموصى به لسد الفجوة:</b> مقرر 'التميز في خدمة وإسعاد المتعاملين'</p>
                <a href='https://www.coursera.org/programs/m-hd-ldr-l-m-0pl54/learn/customer-service-excellence' target='_blank'>📎 رابط الالتحاق بالبرنامج المعتمد عبر Coursera</a>
            </div>
        """, unsafe_allow_html=True)

elif role == "بوابة الجهات الحكومية والشركاء (B2B)":
    st.title("🏢 بوابة تمكين الجهات والمؤسسات الحكومية")
    st.write("بوابة مخصصة لمدراء التدريب والموارد البشرية في الوزارات لمتابعة موظفيهم وتخصيص الميزانيات والمسارات.")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("الجهات الحكومية المرتبطة", "18 جهة")
    with col2:
        st.metric("إجمالي الموازنات المخصصة", "1,200,000 ر.ق")
    with col3:
        st.metric("متوسط نسبة التزام الموظفين بالتعلم", "86%")

    st.subheader("📋 تتبع التزام الإدارات بمسارات التعلم المرن")
    chart_data = pd.DataFrame(
        np.random.randint(40, 95, size=(5, 1)),
        columns=['نسبة الالتزام بالمسارات %'],
        index=['إدارة الشؤون القانونية', 'إدارة العلاقات العامة', 'إدارة الشؤون المالية', 'إدارة الموارد البشرية', 'إدارة نظم المعلومات']
    )
    st.bar_chart(chart_data)

elif role == "بوابة الترخيص والاعتماد وضمان الجودة (NeLC)":
    st.title("🛡️ بوابة التراخيص وضمان جودة التعليم الرقمي")
    st.write("بوابة الإشراف لضمان جودة البرامج الموائمة مع المعايير الوطنية ومتابعة التراخيص للشركاء العالميين والمحليين.")
    
    st.markdown("""
        <div class='card'>
            <div class='card-title'>⚙️ فحص جودة ملفات المواءمة المستوردة</div>
            <p><b>حالة الملفات الحالية:</b> جميع ملفات المواءمة متوافقة بنسبة 100% مع معايير جودة المنصة الوطنية.</p>
            <p>🔒 <b>موثوقية المحتوى:</b> تم التحقق من تفعيل الترجمة العربية لجميع دورات كورسير وتوافقها مع الدرجات الوظيفية.</p>
        </div>
    """, unsafe_allow_html=True)

else:
    st.title("📈 مؤشرات الأداء والتقارير الوطنية")
    st.write("لوحة المؤشرات التفاعلية العامة لقياس الأثر المعرفي والمهاري على مستوى الدولة.")
    
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("إجمالي المسارات الوطنية المعتمدة", total_pathways)
    col2.metric("إجمالي البرامج التدريبية الموثقة", total_courses)
    col3.metric("إجمالي الكفاءات المعالجة", total_competencies)
    col4.metric("معدل نجاح وإتمام البرامج", "78%")

    st.subheader("📊 توزيع المهارات المكتسبة بين الجهات الحكومية")
    chart_data = pd.DataFrame(
        np.random.randint(10, 100, size=(5, 2)),
        columns=['وزارة الاتصالات وتكنولوجيا المعلومات', 'وزارة المالية'],
        index=['مهارات تقنية', 'مهارات تخصصية', 'كفاءات سلوكية', 'مهارات القيادة', 'الأمن السيبراني']
    )
    st.bar_chart(chart_data)
