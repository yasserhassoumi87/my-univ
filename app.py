import streamlit as st

# إعداد الصفحة لتظهر بشكل احترافي
st.set_page_config(page_title="My copy book", page_icon="📚", layout="wide")

# تصميم CSS لجعل الواجهة تشبه التطبيقات الحقيقية (مربعات وألوان مريحة)
st.markdown("""
    <style>
    .main { background-color: #f0f2f6; }
    .stButton>button { width: 100%; border-radius: 10px; height: 3em; background-color: #4CAF50; color: white; }
    .subject-card {
        background-color: white; padding: 20px; border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1); text-align: center;
        margin-bottom: 10px; border: 1px solid #ddd;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🎓 مساعد الطالب الذكي")
st.write("نظّم محاضراتك، تمارينك، وتقارير الـ TP في مكان واحد.")

# إدارة المواد (إضافة مادة جديدة من قبل المستخدم)
if 'subjects' not in st.session_state:
    st.session_state.subjects = ["رياضيات", "فيزياء", "كيمياء"]

new_sub = st.text_input("➕ أضف مادة جديدة (مثلاً: إعلام آلي):")
if st.button("إضافة المادة"):
    if new_sub and new_sub not in st.session_state.subjects:
        st.session_state.subjects.append(new_sub)
        st.rerun()

st.divider()

# عرض المواد على شكل مربعات (Layout)
cols = st.columns(2) # تقسيم الشاشة لمربعين في كل سطر
for i, sub in enumerate(st.session_state.subjects):
    with cols[i % 2]:
        st.markdown(f'<div class="subject-card"><h3>{sub}</h3></div>', unsafe_allow_html=True)
        
        # خيارات داخل كل مادة
        option = st.selectbox(f"ماذا تريد أن ترفع في {sub}؟", ["اختر...", "محاضرة (Cours)", "سلسلة تمارين (TD)", "تقرير (TP)"], key=f"select_{sub}")
        
        if option != "اختر...":
            uploaded_file = st.file_uploader(f"ارفع {option} لـ {sub}", type=['pdf', 'png', 'jpg'], key=f"file_{sub}_{option}")
            
            # ميزة الملاحظة الصوتية (تسجيل أو رفع)
            st.write("🎤 ملاحظة صوتية:")
            audio_file = st.file_uploader("ارفع شرحاً صوتياً للمحاضرة", type=['mp3', 'wav', 'm4a'], key=f"audio_{sub}")
            
            if st.button(f"حفظ في أرشيف {sub}", key=f"btn_{sub}"):
                st.success(f"تم الحفظ بنجاح في قسم {option}!")

st.divider()
st.info("تطبيق تجريبي لتسهيل الحياة الجامعية - لا حاجة لتسجيل الدخول.")

