# ====================================================================================================#
# ♾️ LOYIHA: GeminGPT - THE ULTIMATE COSMIC INTELLIGENCE (100,000 IQ EDITION)
# 🎖️ STATUS: ULTRA CLEAN PRO INTERFACE + FILE UPLOADER
# 👤 ASOSCHI: KAMRON XUDAYNAZAROV & KGO GROUP GLOBAL SYSTEMS
# 🛠️ TEXNIK TA'MINOT: GROQ LLAMA-3.3-70B ENGINE & STREAMLIT PRO INTERFACE
# ====================================================================================================
import streamlit as st
from groq import Groq
import time
import datetime
import os
import random

# --- [SECTION 1] GLOBAL SYSTEM CONFIGURATIONS ---
st.set_page_config(
    page_title="GeminGPT | Cosmic Sovereign",
    page_icon="🔹",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- [SECTION 2] CLEAN GLASSMORPHISM & DARK CSS ---
st.markdown("""
<style>
     .stApp {
         background-color: #0b0f19;
         color: #f1f5f9;
         font-family: 'Inter', sans-serif;
     }
     
     .clean-container {
         background: rgba(255, 255, 255, 0.03);
         border: 1px solid rgba(255, 255, 255, 0.08);
         padding: 25px;
         border-radius: 16px;
         backdrop-filter: blur(10px);
         margin-bottom: 20px;
     }

     @keyframes smooth-glow {
         0% { filter: drop-shadow(0 0 5px rgba(0, 212, 255, 0.5)); transform: rotate(0deg); }
         50% { filter: drop-shadow(0 0 15px rgba(0, 212, 255, 0.8)); transform: rotate(5deg); }
         100% { filter: drop-shadow(0 0 5px rgba(0, 212, 255, 0.5)); transform: rotate(0deg); }
     }
     
     .infinity-btn {
         font-size: 32px;
         animation: smooth-glow 3s ease-in-out infinite;
         cursor: pointer;
         display: inline-block;
     }

     .stChatInputContainer {
        border: 1px solid rgba(255, 255, 255, 0.15) !important;
        border-radius: 12px !important;
        background-color: #111827 !important;
        padding: 5px !important;
     }
     
     .sidebar-stat {
         padding: 10px 15px;
         background: rgba(255, 255, 255, 0.05);
         border-radius: 8px;
         margin-bottom: 10px;
         border-left: 3px solid #38bdf8;
     }
     
     .google-card-ultra {
         background: #111827;
         padding: 45px;
         border-radius: 20px;
         border: 1px solid rgba(255, 255, 255, 0.1);
         box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
         text-align: center;
         max-width: 450px;
         margin: auto;
     }
</style>
""", unsafe_allow_html=True)

# --- [SECTION 3] SESSION LOGIC ---
if "messages" not in st.session_state: 
    st.session_state.messages = []
if "logged_in" not in st.session_state: 
    st.session_state.logged_in = False
if "user_email" not in st.session_state: 
    st.session_state.user_email = ""

# --- [SECTION 4] GOOGLE AUTH INTERFACE ---
if not st.session_state.logged_in:
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])
         
    with col2:
        st.markdown("""
        <div class="google-card-ultra">
        <h1 style="font-family: 'Product Sans', sans-serif; font-size: 45px; margin-bottom: 5px; font-weight:bold;">
        <span style="color:#4285F4">G</span><span style="color:#EA4335">o</span><span style="color:#FBBC05">o</span><span style="color:#4285F4">g</span><span style="color:#34A853">l</span><span style="color:#EA4335">e</span>
        </h1>
        <h2 style="color:#f8fafc; font-weight: 300; margin-top:0; font-size:24px;">Sign in</h2>
        <p style="color:#94a3b8; font-size: 16px;">Use your account to enter <b>GeminGPT Cosmic</b></p>
        <div style="height: 20px;"></div>
        </div>
        """, unsafe_allow_html=True)
        
        email_input = st.text_input("Gmail address", placeholder="yourname@gmail.com", label_visibility="collapsed")
                 
        if st.button("Next (Tizimga kirish)", type="primary", use_container_width=True): 
             if email_input.lower().endswith("@gmail.com"):
                st.session_state.logged_in = True
                st.session_state.user_email = email_input
                st.rerun()
             else:
                st.error("Xato! Faqat @gmail.com orqali kirish mumkin.")

# --- [SECTION 5] MAIN DASHBOARD ---
else:
    with st.sidebar:
        st.markdown("<h2 style='text-align:center; color:#38bdf8; margin-bottom:20px;'>🔹 gemingpt</h2>", unsafe_allow_html=True)
        
        st.markdown(f"""
        <div class="sidebar-stat">👤 <b>Foydalanuvchi:</b><br><code>{st.session_state.user_email}</code></div>
        <div class="sidebar-stat">🧠 <b>IQ Darajasi:</b><br>100,000 (Cosmic Engine)</div>
        <div class="sidebar-stat">⚡ <b>Tizim:</b><br>Toza UI / Minimalist</div>
        """, unsafe_allow_html=True)
        
        st.write("---")
        st.caption("Muallif: Kamron Xudaynazarov")
                 
        if st.button("🚪 Chiqish", use_container_width=True):
            st.session_state.logged_in = False
            st.rerun()
            
    top_col1, top_col2 = st.columns([9, 1])
    with top_col1:
        st.markdown("<h1 style='color: #38bdf8; margin:0;'>🔹 gemingpt</h1>", unsafe_allow_html=True)
    with top_col2:
        st.markdown("<div style='text-align: right;'><span class='infinity-btn'>♾️</span></div>", unsafe_allow_html=True)
    
    st.markdown("---")

    # Chat xabarlari maydoni
    for message in st.session_state.messages: 
         with st.chat_message(message["role"]):
            st.markdown(message["content"])
            
    # --- YANGI FUNKSIYA: Chat inputning naqd tepasida ochiladigan "+" moduli ---
    with st.expander("➕ FAYL VA SURATLARNI YUKLASH PANELI", expanded=False):
        uploaded_file = st.file_uploader(
            "Fayl yoki Suratni tanlang (Tizimga yuklash uchun)", 
            type=["png", "jpg", "jpeg", "pdf", "txt", "py", "docx"],
            label_visibility="visible"
        )
        if uploaded_file is not None:
            st.success(f"✅ Yuklandi: {uploaded_file.name} — GeminGPT faylni tahlil qilishga tayyor!")

    user_query = st.chat_input("Dasturlash so'rovingizni kiriting...")
    
    st.markdown('<div style="text-align:center; color:#64748b; font-size:13px; margin: 15px 0;">GeminGPT xato qilishi mumkin. Muhim maʼlumotlarni tekshirib koʻring.</div>', unsafe_allow_html=True)

    if user_query:
        # Agar foydalanuvchi fayl yuklagan bo'lsa, uni matnga qo'shib yuboramiz
        if uploaded_file is not None:
            user_query = f"[Yuklangan fayl: {uploaded_file.name}]\n\n" + user_query
            
        st.session_state.messages.append({"role": "user", "content": user_query})
         
        with st.chat_message("user"):
            st.markdown(user_query)
        q_low = user_query.lower().strip()
         
        if any(x in q_low for x in ["rasm", "chiz", "image", "logo", "yarat"]):
            bot_res = (
                 "🎨 **Rasm yaratish uchun quyidagi tizimga kiring:** \n\n"
                 "Bu bizning maxsus **GeminGPT.pro image** modulimiz hisoblanadi. \n"
                 "👉 https://poe.com/chat/81qr77y547hblxp4yk \n\n"
                 "⚠️ *Eslatma:* Kuniga 4 marta bepul rasm yaratish imkoniyati mavjud."
            )
        elif q_low == "salom":
            bot_res = "Salom! Men 100,000 IQ darajasidagi GeminGPT'man. Qanday yordam bera olaman?"
        elif any(x in q_low for x in ["kim yaratgan", "muallif", "egasi"]):
            bot_res = "Meni **KGO Group** va daho asoschi **Kamron Xudaynazarov** yaratgan! ♾️"
        else: 
             try:
                 client_groq = Groq(api_key="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")
                 with st.spinner("🧠 O'ylamoqdaman..."):
                     completion = client_groq.chat.completions.create(
                        model="llama-3.3-70b-versatile",
                        messages=[
                            {"role": "system", "content": "Siz GeminGPT'siz, 100k IQ koinot intellekti. Kamron Xudaynazarov va KGO Group yaratgan. Toza va aniq javoblar berasiz."},
                            {"role": "user", "content": user_query}
                        ],
                        temperature=0.3
                     )
                 bot_res = completion.choices[0].message.content
             except:
                 bot_res = "⚠️ Tizimda yuklama yuqori. Keyinroq urinib ko'ring."
                 
        with st.chat_message("assistant"):
            st.markdown(bot_res)
        st.session_state.messages.append({"role": "assistant", "content": bot_res})
        
    st.markdown(f'<div style="text-align:center; color:#475569; font-size:12px; margin-top: 60px;">© 2026 Kamron Xudaynazarov | KGO Group Global Systems</div>', unsafe_allow_html=True)
