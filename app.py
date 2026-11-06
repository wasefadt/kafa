import streamlit as st
import sqlite3
import pandas as pd
import numpy as np
import os
import glob

# 1. إعداد الصفحة وتصميم الهوية البصرية القطرية (FutureX قطر)
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
""", unsafe_allow_html=True)

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
            scorable_skills TEXT
        );
        CREATE TABLE IF NOT EXISTS competency_course_mapping (
            competency_id INTEGER,
            course_id INTEGER,
            PRIMARY KEY(competency_id, course_id),
            FOREIGN KEY(competency_id) REFERENCES competencies(id),
            FOREIGN KEY(course_id) REFERENCES courses(id)
        );
        CREATE TABLE IF NOT EXIS
