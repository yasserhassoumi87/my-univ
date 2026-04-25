import streamlit as st
import os

# إعداد واجهة التطبيق
st.set_page_config(page_title="منظم المحاضرات - ياسر", layout="centered")

st.title("📚 منظم المحاضرات الهندسي")
st.write("مرحباً يا ياسر، ابدأ بتنظيم ملفاتك الدراسية هنا.")

# قائمة المواد (يمكنك تعديلها حسب موادك في هندسة العمليات)
subjects = ["الرياضيات", "الكيمياء", "الفيزياء", "ميكانيك", "لغة إنجليزية"]
selected_subject = st.selectbox("اختر المادة:", subjects)

# رفع الملفات
uploaded_file = st.file_uploader(f"ارفع ملف PDF أو صورة لمحاضرة {selected_subject}", type=['pdf', 'png', 'jpg'])

if uploaded_file is not None:
    st.success(f"تم رفع الملف: {uploaded_file.name} بنجاح!")
    
    # ميزة إضافة ملاحظة صوتية أو نصية
    note = st.text_area("أضف ملاحظة سريعة على هذه المحاضرة:")
    if st.button("حفظ الملاحظة"):
        st.info("تم حفظ الملاحظة مع الملف.")

# عرض أرشيف بسيط (تجريبي)
st.divider()
st.subheader("🗄️ الأرشيف الحالي")
st.write(f"المواد المنظمة: {len(subjects)}")
