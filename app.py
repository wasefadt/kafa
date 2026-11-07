import streamlit as st
import sqlite3
import pandas as pd
import numpy as np
import os
import glob

# Config and Styling
st.set_page_config(page_title="Kafaah X - Qatar", layout="wide", initial_sidebar_state="expanded")

# Custom Arabic CSS
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
    color: #1b4d3e;
}
.stButton>button {
    background-color: #8b263e;
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
    border-right: 5px solid #AAD2C3;
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

st.sidebar.title("منصة كفاءة X الوطنية")
st.sidebar.subheader("التعلم المرن والجدارات - دولة قطر")

role = st.sidebar.selectbox("اختر بوابة الدخول الذكية:", [
    "بوابة الموظف (المحفظة والمسارات المهارية)", 
    "بوابة الجهات الحكومية والشركاء (B2B)", 
    "بوابة الترخيص والاعتماد وضمان الجودة (NeLC)",
    "لوحة التحكم المركزية والإدارة (Admin)",
    "بوابة تكامل الأنظمة (Technical Architecture)"
])

try:
    conn = sqlite3.connect(db_path)
    total_courses = conn.execute("SELECT COUNT(*) FROM courses;").fetchone()[0]
    total_competencies = conn.execute("SELECT COUNT(*) FROM competencies;").fetchone()[0]
    total_pathways = conn.execute("SELECT COUNT(*) FROM pathways;").fetchone()[0]
    total_depts = conn.execute("SELECT COUNT(*) FROM departments;").fetchone()[0]
    conn.close()
except Exception:
    total_courses, total_competencies, total_pathways, total_depts = 352, 6, 60, 8

if role == "بوابة الموظف (المحفظة والمسارات المهارية)":
    st.title("مرحبا بك في محفظتك المهارية الوطنية")
    st.write("رحلتك الشخصية لتطوير كفاءاتك المهنية والارتقاء بمسيرتك الوظيفية.")

    tabs = st.tabs(["محفظتي المهارية المعتمدة", "استكشاف المسارات الوطنية", "خريطة الرحلة التعليمية", "محلل الفجوات والتوصيات"])

    with tabs[0]:
        st.subheader("رصيد الساعات والشهادات المعتمدة سحاب
