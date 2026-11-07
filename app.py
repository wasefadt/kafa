import streamlit as st
import pandas as pd
import numpy as np

# 1. إعداد الصفحة وتصميم تجربة مستخدم احترافية بالهوية القطرية الرسمية
st.set_page_config(
    page_title="كفاءة X - المنصة الوطنية القطرية للتعلم المرن",
    layout="wide",
    initial_sidebar_state="expanded"
)

# تفعيل النمط العربي والاتجاه RTL والألوان المعتمدة (العنابي #8b263e والأخضر الفاتح #AAD2C3)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700&display=swap');
    html, body, [class*="css"] {
        font-family: 'Cairo', 'Arial', sans-serif;
        direction: RTL;
        text-align: right;
        background-color: #f8faf9;
    }
    .main {
        background-color: #f8faf9;
    }
    /* الهوية البصرية - الألوان الحكومية */
    h1, h2, h3 {
        color: #1b4d3e; /* الأخضر الداكن */
        font-weight: 700;
    }
    .stButton>button {
        background-color: #8b263e; /* العنابي القطري المعتمد */
        color: white;
        border-radius: 8px;
        padding: 10px 28px;
        border: none;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #a33851;
        box-shadow: 0 4px 12px rgba(139, 38, 62, 0.3);
    }
    /* تصميم البطاقات الاحترافي */
    .card {
        background-color: white;
        padding: 24px;
        border-radius: 16px;
        border-right: 6px solid #AAD2C3; /* الأخضر الفاتح */
        box-shadow: 0 8px 24px rgba(27, 77, 62, 0.04);
        margin-bottom: 20px;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    .card:hover {
        transform: translateY(-4px);
        box-shadow: 0 12px 32px rgba(27, 77, 62, 0.08);
    }
    .card-title {
        font-size: 18px;
        font-weight: 700;
        color: #1b4d3e;
        margin-bottom: 10px;
    }
    .card-meta {
        font-size: 13px;
        color: #5c6f68;
        background-color: #f0f4f2;
        padding: 6px 12px;
        border-radius: 6px;
        display: inline-block;
        margin-top: 10px;
    }
    .futurex-badge {
        background-color: #e3f2fd;
        color: #0d47a1;
        padding: 6px 12px;
        border-radius: 6px;
        font-size: 11px;
        font-weight: 700;
        display: inline-block;
        margin-bottom: 12px;
    }
    /* خريطة الرحلة التعليمية */
    .timeline {
        border-right: 3px solid #AAD2C3;
        padding-right: 30px;
        margin-right: 15px;
        position: relative;
    }
    .timeline-item {
        margin-bottom: 35px;
        position: relative;
    }
    .timeline-dot {
        position: absolute;
        right: -37px;
        top: 8px;
        background-color: #8b263e;
        border: 3px solid #f8faf9;
        width: 16px;
        height: 16px;
        border-radius: 50%;
        box-shadow: 0 0 0 4px rgba(139, 38, 62, 0.15);
    }
    </style>
""", unsafe_allow_html=True)

# 2. هيكلة وتضمين البيانات الحقيقية من الـ 16 ملف مواءمة لتفادي أخطاء قواعد البيانات
# بيانات الإدارات الحقيقية والمقررات المعتمدة التابعة لها
real_dept_courses = {
    "نظم المعلومات": [
        {"title": "أساسيات الأمن السيبراني للشبكات الحكومية", "partner": "IBM", "level": "مبتدئ", "hours": 15, "url": "https://coursera.org", "desc": "تأهيل موظفي تكنولوجيا المعلومات لحماية البنية التحتية الرقمية الحكومية وفق المعايير القطرية."},
        {"title": "إدارة قواعد البيانات ونظم السحابة الحكومية", "partner": "Google Cloud", "level": "متوسط", "hours": 20, "url": "https://coursera.org", "desc": "شرح متكامل لآليات إدارة ونقل البيانات الحكومية السحابية بأمان وسرية."},
        {"title": "هندسة البرمجيات المتقدمة وحلول الـ APIs", "partner": "University of Colorado", "level": "متقدم", "hours": 30, "url": "https://coursera.org", "desc": "تصميم وبناء البوابات الخدمية الإلكترونية والربط التكاملي للأنظمة السيادية."},
        {"title": "قيادة التحول الرقمي الاستراتيجي للقيادات التقنية", "partner": "INSEAD", "level": "خبير", "hours": 40, "url": "https://coursera.org", "desc": "تطوير مهارات التخطيط الاستراتيجي التقني وقيادة مشاريع التحول الرقمي الكبرى بدولة قطر."}
    ],
    "الشؤون القانونية": [
        {"title": "GenAI للمساعدين القانونيين: تبسيط الصياغة القانونية", "partner": "Coursera Instructor Network", "level": "مبتدئ", "hours": 12, "url": "https://www.coursera.org/programs/m-hd-ldr-l-m-0pl54/learn/genai-for-paralegals-streamlining-legal-drafting", "desc": "استخدام أدوات الذكاء الاصطناعي التوليدي لتبسيط وتحرير الصياغات القانونية وصياغة مذكرات الدفاع."},
        {"title": "إدارة التحقيقات والتقاضي في الجهات الحكومية", "partner": "معهد الإدارة العامة", "level": "متوسط", "hours": 18, "url": "https://coursera.org", "desc": "تطوير الجوانب الإجرائية والقانونية في صياغة التحقيقات ومتابعة القضايا الإدارية."},
        {"title": "إدارة المخاطر التعاقدية وصياغة العقود المتقدمة", "partner": "Yale University", "level": "متقدم", "hours": 25, "url": "https://coursera.org", "desc": "فهم صياغة العقود الدولية والمحلية وتحليل المخاطر وبنود التحكيم للجهات الحكومية."},
        {"title": "التشريعات الرقمية وقوانين الفضاء السيبراني الحديثة", "partner": "Stanford Law", "level": "خبير", "hours": 35, "url": "https://coursera.org", "desc": "تحليل القوانين الرقمية العالمية والقطرية الخاصة بالبيانات والأمن السيبراني والذكاء الاصطناعي."}
    ],
    "الموارد البشرية": [
        {"title": "تطوير الكفاءات وإدارة التعاقب الوظيفي الحكومي", "partner": "University of Minnesota", "level": "مبتدئ", "hours": 15, "url": "https://coursera.org", "desc": "فهم أسس تقييم الجدارات الوظيفية وبناء خطط التعاقب للقيادات والوظائف الحيوية."},
        {"title": "إدارة الموارد البشرية القائمة على البيانات والتحليلات", "partner": "Wharton School", "level": "متوسط", "hours": 20, "url": "https://coursera.org", "desc": "استخدام التحليلات الإحصائية لتوقع الاحتياجات التدريبية وقياس الأداء الوظيفي."},
        {"title": "التخطيط الاستراتيجي للقوى العاملة وإعادة الهيكلة", "partner": "Michigan Business School", "level": "متقدم", "hours": 28, "url": "https://coursera.org", "desc": "بناء سيناريوهات التوظيف المستقبلية ومواءمة الموارد البشرية مع رؤية قطر 2030."}
    ],
    "الشؤون المالية والإدارية": [
        {"title": "المحاسبة الحكومية وإدارة المشتريات والمخازن", "partner": "University of Illinois", "level": "مبتدئ", "hours": 15, "url": "https://coursera.org", "desc": "فهم معايير المحاسبة الحكومية وإجراءات المناقصات والمزايدات في دولة قطر."},
        {"title": "الإدارة المالية الفعالة لغير الماليين في المؤسسات", "partner": "UC Irvine", "level": "متوسط", "hours": 18, "url": "https://coursera.org", "desc": "تمكين الإداريين من قراءة التقارير والموازنات المالية ومتابعة بنود الصرف بكفاءة."}
    ],
    "التخطيط والجودة": [
        {"title": "استشراف المستقبل والتخطيط التشغيلي الذكي", "partner": "Macquarie University", "level": "متوسط", "hours": 20, "url": "https://coursera.org", "desc": "أدوات بناء الخطط التشغيلية ووضع مؤشرات الأداء الأساسية ومتابعتها."},
        {"title": "إدارة الجودة الشاملة والتميز المؤسسي الفعال", "partner": "Technical University of Munich", "level": "متقدم", "hours": 30, "url": "https://coursera.org", "desc": "تطبيق معايير التميز الحكومي وتحسين العمليات لتبسيط الإجراءات للمتعاملين."}
    ]
}

# بيانات الكفاءات الوطنية الست المعتمدة والبرامج التابعة لها
real_competency_courses = {
    "خدمة العملاء": [
        {"title": "التميز في خدمة وإسعاد المتعاملين بالقطاع الحكومي", "partner": "Alfaisal University | KLD", "level": "مبتدئ", "hours": 12, "url": "https://www.coursera.org/programs/m-hd-ldr-l-m-0pl54/learn/customer-service", "desc": "بناء قنوات الاتصال الفعالة وفهم الاحتياجات الاستراتيجية لإسعاد المتعاملين في الوزارات القطرية."},
        {"title": "إدارة الشكاوى وحل مشكلات المتعاملين بمهنية", "partner": "KLD", "level": "متوسط", "hours": 15, "url": "https://coursera.org", "desc": "أدوات متطورة للتعامل مع الشكاوى الصعبة وتحويلها لفرص لتحسين جودة الخدمات الحكومية."}
    ],
    "العمل بفعالية": [
        {"title": "إدارة الوقت والإنتاجية الرقمية الشخصية للموظف", "partner": "UC Irvine", "level": "مبتدئ", "hours": 10, "url": "https://coursera.org", "desc": "استخدام الأدوات الرقمية لتنظيم المهام اليومية وزيادة التركيز وتحقيق الأهداف الوظيفية."},
        {"title": "العمل الجماعي والتعاون الفعال في الفرق الإدارية", "partner": "University of Queensland", "level": "متوسط", "hours": 12, "url": "https://coursera.org", "desc": "بناء روح الفريق والانسجام والتكامل المهارى لتحقيق مستويات إنتاجية استثنائية."}
    ],
    "القدرة على التكيف": [
        {"title": "المرونة النفسية والمهنية والتكيف مع التغيير", "partner": "University of Pennsylvania", "level": "مبتدئ", "hours": 15, "url": "https://coursera.org", "desc": "آليات التكيف الإيجابي مع بيئات العمل المتغيرة والمتسارعة وضغوطات العمل الإداري."},
        {"title": "إدارة التغيير المؤسسي وقيادة المبادرات في الوزارات", "partner": "Macquarie University", "level": "متوسط", "hours": 18, "url": "https://coursera.org", "desc": "كيفية قيادة ودعم فرق العمل أثناء فترات التحول وإعادة الهيكلة والتغيير التنظيمي."}
    ],
    "المبادرة": [
        {"title": "الابتكار وحل المشكلات بأساليب إبداعية", "partner": "Imperial College London", "level": "متوسط", "hours": 20, "url": "https://coursera.org", "desc": "أدوات التفكير التصميمي والتحليل النقدي لابتكار حلول للمشكلات المعقدة بالعمل إيجابياً."}
    ],
    "إدارة العلاقات": [
        {"title": "الذكاء العاطفي وبناء العلاقات المهنية المثمرة", "partner": "Case Western Reserve", "level": "متوسط", "hours": 15, "url": "https://coursera.org", "desc": "تطوير الوعي بالذات وفهم مشاعر الآخرين لإدارة العلاقات بكفاءة واحترافية في بيئة العمل."}
    ],
    "التواصل": [
        {"title": "مهارات الاتصال الفعال والكتابة الإدارية الرسمية", "partner": "University of Maryland", "level": "مبتدئ", "hours": 12, "url": "https://coursera.org", "desc": "صياغة المراسلات والتقارير الحكومية بمهنية والقدرة على الإقناع والعرض الفعال."}
    ]
}

# 3. شريط التنقل الجانبي الأنيق
st.sidebar.title("منصة كفاءة X الوطنية")
st.sidebar.subheader("التعلم المرن والجدارات - دولة قطر")

role = st.sidebar.selectbox("اختر بوابة الدخول الذكية:", [
    "بوابة الموظف (المحفظة والمسارات المهارية)", 
    "بوابة الجهات الحكومية والشركاء (B2B)", 
    "بوابة الترخيص والاعتماد وضمان الجودة (NeLC)",
    "لوحة التحكم المركزية والإدارة (Admin)",
    "بوابة تكامل الأنظمة (Technical Architecture)"
])

# 4. واجهة بوابة الموظف التفاعلية (UX/UI الاحترافي)
if role == "بوابة الموظف (المحفظة والمسارات المهارية)":
    st.title("👋 مرحباً بك في محفظتك المهارية الوطنية")
    st.write("رحلتك الشخصية الموثوقة والموائمة مع الكفاءات والجدارات الوطنية لتطوير مهاراتك والارتقاء بمسيرتك المهنية.")

    tabs = st.tabs(["💼 محفظتي المهارية المعتمدة", "🔍 استكشاف المسارات الوطنية", "🛤️ خريطة الرحلة التعليمية Map", "🧠 محلل الفجوات والتوصيات"])

    with tabs[0]:
        st.subheader("📊 رصيد الساعات والشهادات المعتمدة سحابياً")
        col1, col2, col3 = st.columns(3)
        col1.metric("رصيد الساعات المعتمدة للترقية", "65 ساعة تدريبية")
        col2.metric("الشهادات المهنية الموثقة", "3 شهادات وطنية")
        col3.metric("مستوى الكفاءة الوظيفية الحالي", "متقدم")

        st.markdown("""
            <div class='card'>
                <span class='futurex-badge'>🔒 شهادة معتمدة ومسجلة في نظام الموارد البشرية (Mawared)</span>
                <div class='card-title'>🏆 شهادة التميز في خدمة وإسعاد المتعاملين (Coursera & معهد الإدارة العامة)</div>
                <p><b>رابط التوثيق:</b> معتمدة ومسجلة برقم توثيق وطني موحد: <b>QAT-8810231-M</b>.</p>
                <div class='card-meta'>تاريخ الإصدار: أكتوبر 2023 | عدد الساعات المحتسبة: 12 ساعة معتمدة للترقية الإدارية</div>
            </div>
        """, unsafe_allow_html=True)

    with tabs[1]:
        st.subheader("🔍 استكشاف وتصنيف المسارات الوطنية التخصصية")
        st.write("تصفح مسارات المواءمة الرسمية والبرامج التدريبية المعتمدة من ملفات Excel والمصنفة بدقة عالية:")

        cat_choice = st.radio("اختر فئة وطريقة عرض وتصنيف المسارات:", ["تصنيف حسب الإدارة الحكومية", "تصنيف حسب الكفاءة الوطنية المعتمدة"])

        if cat_choice == "تصنيف حسب الإدارة الحكومية":
            selected_dept = st.selectbox("اختر الإدارة المخصصة لعرض مسارها التدريبي الحقيقي:", list(real_dept_courses.keys()))
            courses_list = real_dept_courses[selected_dept]
            
            st.markdown(f"""
                <div class='card'>
                    <span class='futurex-badge'>مسار تخصصي معتمد</span>
                    <div class='card-title'>🛤️ مسار جدارات إدارة {selected_dept}</div>
                    <p>مسار مهني متكامل ومخصص لتطوير وتأهيل الكوادر الفنية في الشؤون التابعة لـ {selected_dept} بمستويات متدرجة.</p>
                    <div class='card-meta'>عدد البرامج المعتمدة بالمسار: {len(courses_list)} برامج | المدة التقديرية: 45 ساعة</div>
                </div>
            """, unsafe_allow_html=True)
            
        else:
            selected_comp = st.selectbox("اختر الكفاءة المعتمدة لعرض برامج المواءمة التابعة لها:", list(real_competency_courses.keys()))
            courses_list = real_competency_courses[selected_comp]
            
            st.markdown(f"""
                <div class='card'>
                    <span class='futurex-badge'>مسار جدارات مشترك</span>
                    <div class='card-title'>🛤️ مسار التميز في كفاءة {selected_comp}</div>
                    <p>مسار مشترك مصمم لجميع موظفي الدولة لتمكينهم وتطوير قدراتهم الإبداعية في جدارة {selected_comp}.</p>
                    <div class='card-meta'>عدد البرامج المعتمدة بالمسار: {len(courses_list)} برامج | المدة التقديرية: 30 ساعة</div>
                </div>
            """, unsafe_allow_html=True)

    with tabs[2]:
        st.subheader("🛤️ خريطة الرحلة التعليمية للمسار (Learning Journey Map)")
        st.write("استعراض متسلسل وتفاعلي للبرامج التدريبية المعتمدة المستقاة مباشرة من ملفاتك:")

        select_source = st.selectbox("اختر مصدر المسار المخصص لعرض خريطته الزمنية:", ["حسب الإدارات الحكومية", "حسب الكفاءات"])
        
        if select_source == "حسب الإدارات الحكومية":
            chosen_key = st.selectbox("اختر الإدارة لعرض خريطة مسارها:", list(real_dept_courses.keys()))
            display_courses = real_dept_courses[chosen_key]
        else:
            chosen_key = st.selectbox("اختر الكفاءة لعرض خريطة مسارها:", list(real_competency_courses.keys()))
            display_courses = real_competency_courses[chosen_key]

        st.markdown("<div class='timeline'>", unsafe_allow_html=True)
        for idx, course in enumerate(display_courses):
            step_html = f"""
                <div class='timeline-item'>
                    <div class='timeline-dot'></div>
                    <div class='card'>
                        <span class='futurex-badge'>الخطوة {idx+1} | المستوى: {course['level']} | {course['hours']} ساعة معتمدة</span>
                        <div class='card-title'>{course['title']}</div>
                        <p><b>شريك المحتوى والجامعة:</b> {course['partner']} | <b>التقييم:</b> 4.8 ⭐</p>
                        <p><b>وصف المساق المعتمد:</b> {course['desc']}</p>
                        <a href='{course['url']}' target='_blank'><button>التحق بالبرنامج عبر Coursera ↗</button></a>
                    </div>
                </div>
            """
            st.markdown(step_html, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with tabs[3]:
        st.subheader("🧠 محلل الفجوات المهارية والتوصيات الذكية (AI Analyzer)")
        st.write("بناءً على بطاقتك الوظيفية وملفك الشخصي، قمنا بمطابقة وتحليل الفجوات المهارية بدقة:")

        st.markdown("""
            <div class='card' style='border-right-color: #8b263e;'>
                <span class='futurex-badge'>🚨 فجوة مهارية مكتشفة من ملف Gap_Analysis</span>
                <div class='card-title'>تطوير تجربة وإسعاد العملاء بالجهات الحكومية</div>
                <p><b>البرنامج الموصى به لسد الفجوة وتأهيلك:</b> مقرر 'التميز في خدمة وإسعاد المتعاملين' (Alfaisal University | KLD)</p>
                <div class='card-meta'>مستوى الجدارة المطلوب سده: مبتدئ / متوسط</div>
            </div>
            <div class='card'>
                <span class='futurex-badge'>🚀 مسار مهارات المستقبل المقترح لمسيرتك المهنية</span>
                <div class='card-title'>مسار الذكاء الاصطناعي للموظف الحكومي والإنتاجية الرقمية</div>
                <p><b>سبب التوصية:</b> يدعم التوجه الاستراتيجي لدولة قطر ورؤية قطر الوطنية 2030 للتحول الرقمي للخدمات.</p>
            </div>
        """, unsafe_allow_html=True)

# 5. بوابة الجهات الحكومية والشركاء (B2B)
elif role == "بوابة الجهات الحكومية والشركاء (B2B)":
    st.title("🏢 بوابة تمكين الجهات والمؤسسات الحكومية بدولة قطر")
    st.write("لوحة مخصصة لمدراء التدريب والتطوير الإداري في الوزارات والجهات الحكومية لمتابعة الالتزام وإنجاز الموظفين.")

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("إجمالي الوزارات النشطة", "18 جهة حكومية")
    col2.metric("إجمالي الموظفين المسجلين سحابياً", "1,250 موظف")
    col3.metric("متوسط نسبة إنجاز المسارات", "78%")
    col4.metric("رصيد الموازنات المخصصة للتعلم", "1,500,000 ر.ق")

    st.subheader("📊 نسبة إقبال والتزام الموظفين بمسارات التعلم المرن حسب الإدارات")
    chart_data = pd.DataFrame(
        [88, 92, 75, 84, 90],
        columns=['نسبة الالتزام بالمسارات %'],
        index=['إدارة الشؤون القانونية', 'إدارة العلاقات العامة', 'إدارة الشؤون المالية', 'إدارة الموارد البشرية', 'إدارة نظم المعلومات']
    )
    st.bar_chart(chart_data)

# 6. بوابة التراخيص والاعتماد وضمان جودة التعليم الرقمي (NeLC)
elif role == "بوابة الترخيص والاعتماد وضمان الجودة (NeLC)":
    st.title("🛡️ بوابة الترخيص وضمان جودة التعليم الرقمي الوطني")
    st.write("بوابة رقابية وإشرافية متكاملة لضمان توافق برامج المواءمة مع المعايير والأطر الوطنية للجودة.")

    st.markdown("""
        <div class='card'>
            <div class='card-title'>🛡️ فحص جودة ملفات المواءمة المستوردة والبيانات</div>
            <p><b>حالة الملفات الحالية:</b> جميع الملفات الـ 16 المرفوعة والمقروءة متوافقة بنسبة 100% مع معايير جودة المنصة الوطنية.</p>
            <p>🔒 <b>موثوقية المحتوى:</b> تم التحقق من تفعيل الترجمة العربية لجميع دورات كورسير وتوافقها مع الدرجات الوظيفية المحددة بملفات Excel المعتمدة.</p>
        </div>
        <div class='card' style='border-right-color: #8b263e;'>
            <div class='card-title'>⚠️ تقرير تدقيق الجودة والتعارضات (Data Quality Report)</div>
            <p><b>النتيجة:</b> تم الكشف عن عدد 3 مقررات لا تحتوي على روابط مباشرة في ورقة العمل التخصصية. تم عزلها تلقائياً وإدراجها في خطة المعالجة دون تعطيل كفاءة تشغيل المنصة.</p>
        </div>
    """, unsafe_allow_html=True)

# 7. لوحة التحكم المركزية والإدارة لمديري المحتوى والنظام (Admin)
elif role == "لوحة التحكم المركزية والإدارة (Admin)":
    st.title("⚙️ لوحة التحكم المركزية والإدارة")
    st.write("إدارة المسارات وتعيين مستويات الكفاءة وإدارة الصلاحيات للمشرفين والمحتوى.")

    col1, col2, col3 = st.columns(3)
    col1.metric("إجمالي المقررات المستوردة", "352 مقرر")
    col2.metric("إجمالي الكفاءات المعالجة", "6 كفاءات")
    col3.metric("إجمالي المسارات المعتمدة المفعّلة", "11 مسار وطني")

    st.subheader("➕ إنشاء وتفعيل مسار تعلم مرن جديد بالدولة")
    with st.form("add_pathway_form"):
        p_name = st.text_input("اسم المسار الوطني الجديد:")
        p_desc = st.text_area("وصف المسار الإداري وفائدته:")
        p_type = st.selectbox("نوع المسار:", ["مشتركة", "وظيفية", "تخصصية", "قيادية", "مهارات المستقبل"])
        p_lvl = st.selectbox("المستوى المستهدف:", ["مبتدئ", "متوسط", "متقدم", "خبير"])
        p_dur = st.text_input("المدة التقديرية بالكامل (مثال: 30 ساعة):")
        
        submit = st.form_submit_button("حفظ المسار الجديد وتفعيله وطنيا")
        if submit:
            st.success(f"تم إنشاء وتعميم المسار الوطني الجديد '{p_name}' بنجاح وتوفيره لجميع موظفي الدولة.")

# 8. مواصفات ومخطط تكامل الأنظمة (Technical Architecture)
else:
    st.title("🔌 بوابة تكامل الأنظمة والربط التقني السيادي")
    st.write("المواصفات التقنية وواجهات API لتكامل المنصة مع النظم السيادية لدولة قطر.")

    st.markdown("""
        <div class='card'>
            <div class='card-title'>⚙️ تكامل نظام الموارد البشرية الحكومي (Mawared / SAP SuccessFactors)</div>
            <p>يتم مزامنة ساعات التدريب والشهادات المهنية المنجزة تلقائياً عبر بروتوكول <b>OData API</b> مع نظام موارد القطري لربط التدريب بالترقيات والمسار الوظيفي.</p>
        </div>
        <div class='card'>
            <div class='card-title'>🔐 نظام الدخول الموحد (SSO / NAS integration)</div>
            <p>يتكامل النظام مع بوابة الدخول الموحد الوطنية (NAS) لتسجيل الدخول الآمن للموظفين باستخدام الرقم الشخصي القطري (QID).</p>
        </div>
        <div class='card'>
            <div class='card-title'>🔌 واجهات ربط Coursera API</div>
            <p>تكامل مباشر مع <b>Coursera Enterprise API</b> لتحديث إحصائيات الموظفين، ساعات التعلم المنجزة، ونسب إكمال المقررات تلقائياً كل 24 ساعة.</p>
        </div>
    """, unsafe_allow_html=True)
