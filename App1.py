import streamlit as st
import google.generativeai as genai

# 1. ตั้งค่า API Key ของคุณ
API_KEY = "AIzaSyDinwyY9J8QmupzEF-Zp7tKn_UMkGmLKmE"
genai.configure(api_key=API_KEY)

st.title("🎨 LINE Sticker Generator AI")

sticker_text = st.text_input("ระบุข้อความบนสติกเกอร์")
mood = st.selectbox("เลือกโทนอารมณ์", ("มีความสุข", "กวนๆ", "น่ารัก"))

if st.button("🚀 เริ่มสร้างสติกเกอร์"):
    if sticker_text:
        with st.spinner("กำลังเชื่อมต่อกับ AI..."):
            try:
                # แก้ไขตรงนี้: เปลี่ยนเป็น gemini-pro
                model = genai.GenerativeModel('gemini-pro') 
                
                prompt = f"Design a LINE sticker. Concept: {mood}. Character holds a sign saying '{sticker_text}'. Description: cute cartoon style, white background."
                
                # ลองส่งคำสั่งไปที่ AI
                response = model.generate_content(prompt)
                
                st.success("AI ตอบกลับมาแล้ว!")
                st.write("แนวทางการออกแบบจาก AI:")
                st.info(response.text) # จะเห็นข้อความบรรยายสติกเกอร์ที่ AI ออกแบบให้
                
            except Exception as e:
                st.error(f"ยังคงเกิดข้อผิดพลาด: {e}")
                st.info("ลองตรวจสอบว่า API Key ของคุณเปิดใช้งานใน Google AI Studio หรือยังนะคะ")
