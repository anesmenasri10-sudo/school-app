import streamlit as st

st.set_page_config(page_title="حساب المعدل المدرسي", page_icon="📚", layout="centered")

st.markdown("<h1 style='text-align: center; color: #1E3A8A;'>حساب المعدل المدرسي 🎓</h1>", unsafe_allow_html=True)
st.write("---")

# اختيار السنة الدراسية
grade_level = st.selectbox("اختر مستواك الدراسي:", ["السنة الأولى ثانوي", "السنة الثانية ثانوي"])

# إدخال عدد المواد
num_subjects = st.number_input("أدخل عدد المواد:", min_value=1, max_value=20, value=5)

subjects = []
coefficients = []
grades = []

st.write("### أدخل تفاصيل المواد:")
for i in range(num_subjects):
    col1, col2 = st.columns(2)
    with col1:
        subj = st.text_input(f"اسم المادة {i+1}", value=f"المادة {i+1}", key=f"subj_{i}")
    with col2:
        coef = st.number_input(f"المعامل لـ {subj}", min_value=1.0, max_value=10.0, value=1.0, key=f"coef_{i}")
    
    grade = st.number_input(f"النقطة لـ {subj} (من 20)", min_value=0.0, max_value=20.0, value=10.0, key=f"grade_{i}")
    
    subjects.append(subj)
    coefficients.append(coef)
    grades.append(grade)
    st.write("---")

if st.button("حساب المعدل 🚀", use_container_width=True):
    total_score = sum(g * c for g, c in zip(grades, coefficients))
    total_coef = sum(coefficients)
    
    if total_coef > 0:
        gpa = total_score / total_coef
        st.success(f"معدلك لهذا الفصل هو : {gpa:.2f} / 20 🏆")
    else:
        st.error("مجموع المعاملات لا يمكن أن يكون صفراً!")

st.markdown("<p style='text-align: center; color: gray;'>تم التطوير بواسطة Anes Menasri © 2026</p>", unsafe_allow_html=True)
