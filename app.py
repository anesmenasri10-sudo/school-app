import streamlit as st

# إعدادات الصفحة والتصميم العام بألوان متدرجة وعصرية
st.set_page_config(page_title="حساب المعدل المدرسي - الجزائر", page_icon="🎓", layout="centered")

st.markdown("""
    <style>
    .main {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    }
    .stButton>button {
        background: linear-gradient(90deg, #4facfe 0%, #00f2fe 100%);
        color: white;
        font-weight: bold;
        border: none;
        border-radius: 10px;
        padding: 10px 20px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .stButton>button:hover {
        background: linear-gradient(90deg, #00f2fe 0%, #4facfe 100%);
        color: white;
    }
    h1 {
        background: -webkit-linear-gradient(45deg, #1d2671, #c33764);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1>منصة حساب المعدل المدرسي 🎓</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #555;'>اختر مستواك وشعبتك لحساب معدلك بتصميم رائع ومتدرج</p>", unsafe_allow_html=True)
st.write("---")

# اختيار السنة الدراسية
grade_level = st.selectbox("اختر مستواك الدراسي:", ["السنة الأولى ثانوي", "السنة الثانية ثانوي"])

# اختيار الشعبة بناءً على السنة
if grade_level == "السنة الأولى ثانوي":
    stream = st.selectbox("اختر الشعبة:", ["جذع مشترك علوم وتكنولوجيا", "جذع مشترك آداب"])
    if stream == "جذع مشترك علوم وتكنولوجيا":
        subjects_info = {
            "الرياضيات": 5,
            "علوم الطبيعة والحياة": 4,
            "الفيزياء والكيمياء": 4,
            "اللغة العربية": 3,
            "اللغة الفرنسية": 3,
            "اللغة الإنجليزية": 2,
            "التاريخ والجغرافيا": 2,
            "العلوم الإسلامية": 2,
            "التربية المدنية": 1,
            "الإعلام الآلي": 2,
            "التربية البدنية": 1
        }
    else:
        subjects_info = {
            "اللغة العربية": 5,
            "الرياضيات": 3,
            "التاريخ والجغرافيا": 4,
            "اللغة الفرنسية": 3,
            "اللغة الإنجليزية": 3,
            "علوم الطبيعة والحياة": 2,
            "الفيزياء والكيمياء": 2,
            "العلوم الإسلامية": 2,
            "التربية المدنية": 1,
            "التربية البدنية": 1
        }
else:  # السنة الثانية ثانوي
    stream = st.selectbox("اختر الشعبة:", ["علوم تجريبية", "رياضيات", "تقني رياضي", "تسيير واقتصاد", "آداب وفلسفة", "لغات أجنبية"])
    if stream == "علوم تجريبية":
        subjects_info = {
            "علوم الطبيعة والحياة": 5,
            "الرياضيات": 5,
            "الفيزياء والكيمياء": 5,
            "اللغة العربية": 3,
            "اللغة الفرنسية": 2,
            "اللغة الإنجليزية": 2,
            "التاريخ والجغرافيا": 2,
            "العلوم الإسلامية": 2,
            "الفلسفة": 2,
            "التربية البدنية": 1
        }
    elif stream == "رياضيات":
        subjects_info = {
            "الرياضيات": 7,
            "الفيزياء والكيمياء": 6,
            "علوم الطبيعة والحياة": 2,
            "اللغة العربية": 3,
            "اللغة الفرنسية": 2,
            "اللغة الإنجليزية": 2,
            "التاريخ والجغرافيا": 2,
            "العلوم الإسلامية": 2,
            "الفلسفة": 2,
            "التربية البدنية": 1
        }
    elif stream == "تقني رياضي":
        subjects_info = {
            "الرياضيات": 6,
            "العلوم التقنية (التخصص)": 6,
            "الفيزياء والكيمياء": 5,
            "اللغة العربية": 3,
            "اللغة الفرنسية": 2,
            "اللغة الإنجليزية": 2,
            "التاريخ والجغرافيا": 2,
            "العلوم الإسلامية": 2,
            "الفلسفة": 2,
            "التربية البدنية": 1
        }
    elif stream == "تسيير واقتصاد":
        subjects_info = {
            "الرياضيات": 5,
            "التسيير المحاسبي والمالي": 6,
            "الاقتصاد والمناجمنت": 5,
            "القانون": 2,
            "اللغة العربية": 3,
            "اللغة الفرنسية": 2,
            "اللغة الإنجليزية": 2,
            "التاريخ والجغرافيا": 2,
            "العلوم الإسلامية": 2,
            "الفلسفة": 2,
            "التربية البدنية": 1
        }
    elif stream == "آداب وفلسفة":
        subjects_info = {
            "اللغة العربية": 6,
            "الفلسفة": 6,
            "التاريخ والجغرافيا": 4,
            "الرياضيات": 2,
            "اللغة الفرنسية": 3,
            "اللغة الإنجليزية": 3,
            "العلوم الإسلامية": 2,
            "التربية البدنية": 1
        }
    else:  # لغات أجنبية
        subjects_info = {
            "اللغة العربية": 5,
            "اللغة الأجنبية الأولى": 5,
            "اللغة الأجنبية الثانية": 5,
            "اللغة الأجنبية الثالثة": 4,
            "التاريخ والجغرافيا": 2,
            "الرياضيات": 2,
            "العلوم الإسلامية": 2,
            "الفلسفة": 2,
            "التربية البدنية": 1
        }

st.write("---")
st.write("### أدخل نقاط المواد:")

grades = []
coefficients = []

for subj, coef in subjects_info.items():
    grade = st.number_input(f"{subj} (المعامل: {coef})", min_value=0.0, max_value=20.0, value=10.0, step=0.25, key=subj)
    grades.append(grade)
    coefficients.append(coef)

st.write("---")

if st.button("حساب المعدل النهائي 🚀", use_container_width=True):
    total_score = sum(g * c for g, c in zip(grades, coefficients))
    total_coef = sum(coefficients)
    
    if total_coef > 0:
        gpa = total_score / total_coef
        st.success(f"معدلك لهذا الفصل هو : {gpa:.2f} / 20 🏆")
        if gpa >= 10:
            st.balloons()
    else:
        st.error("حدث خطأ في حساب المعاملات.")

st.markdown("<p style='text-align: center; color: gray;'>تم التطوير بواسطة Anes Menasri © 2026</p>", unsafe_allow_html=True)
