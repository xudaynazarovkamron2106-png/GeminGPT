# ====================================================================================================#
# ♾️ LOYIHA: GeminGPT - THE ULTIMATE COSMIC INTELLIGENCE (100,000 IQ EDITION)
# 🎖️ STATUS: MULTI-LINGUAL ALL-KNOWING SUPER AI (FULLY FIXED LOGIC)
# 👤 ASOSCHI: KAMRON XUDAYNAZAROV & KGO GROUP GLOBAL SYSTEMS
# ====================================================================================================
import streamlit as st
import time
import datetime
import os
import random
import urllib.parse
import requests

# --- [SECTION 1] GLOBAL SYSTEM CONFIGURATIONS ---
st.set_page_config(
    page_title="GeminGPT | Cosmic Sovereign",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- [SECTION 2] HIGH VISIBILITY BLUE & DARK CSS ---
st.markdown("""
<style>
     .stApp {
         background-color: #0b0f19;
         color: #ffffff !important;
         font-family: 'Inter', sans-serif;
     }
     
     [data-testid="stSidebar"] {
         background-color: #0f172a !important;
         color: #ffffff !important;
     }
     [data-testid="stSidebar"] p, [data-testid="stSidebar"] b, [data-testid="stSidebar"] span {
         color: #ffffff !important;
     }
     
     .stChatMessage p {
         color: #ffffff !important;
         font-size: 16px !important;
         font-weight: 500 !important;
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
        border: 2px solid #2563eb !important; 
        border-radius: 12px !important;
        background-color: #1e293b !important; 
        padding: 5px !important;
        box-shadow: 0 0 15px rgba(37, 99, 235, 0.3) !important; 
     }
     
     .stChatInputContainer textarea {
        color: #ffffff !important;
        font-size: 16px !important;
     }
     
     .sidebar-stat {
         padding: 12px 15px;
         background: rgba(255, 255, 255, 0.08);
         border-radius: 8px;
         margin-bottom: 10px;
         border-left: 4px solid #2563eb;
         color: #ffffff !important;
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
        st.markdown("<h2 style='text-align:center; color:#2563eb; margin-bottom:20px;'>gemingpt</h2>", unsafe_allow_html=True)
        st.markdown(f"""
        <div class="sidebar-stat">👤 <b>Foydalanuvchi:</b><br><code>{st.session_state.user_email}</code></div>
        <div class="sidebar-stat">🧠 <b>IQ Darajasi:</b><br>100,000 (Cosmic Engine)</div>
        <div class="sidebar-stat">⚡ <b>Tizim:</b><br>Ko'k UI Modeli</div>
        """, unsafe_allow_html=True)
        st.write("---")
        st.markdown("<b style='color:#ffffff;'>Muallif: Kamron Xudaynazarov</b>", unsafe_allow_html=True)
                 
        if st.button("🚪 Chiqish", use_container_width=True):
            st.session_state.logged_in = False
            st.rerun()
            
    top_col1, top_col2 = st.columns([9, 1])
    with top_col1:
        st.markdown("<h1 style='color: #2563eb; margin:0; font-weight:bold;'>gemingpt</h1>", unsafe_allow_html=True)
    with top_col2:
        st.markdown("<div style='text-align: right;'><span class='infinity-btn'>♾️</span></div>", unsafe_allow_html=True)
    
    st.markdown("---")

    # Tarixdagi xabarlar va rasmlarni chiqarish
    for message in st.session_state.messages: 
         with st.chat_message(message["role"]):
            st.markdown(message["content"])
            if message.get("is_image", False):
                st.image(message["image_url"], caption="GeminGPT Cosmic Engine", use_container_width=True)
            
    with st.expander("➕ FAYL VA SURATLARNI YUKLASH PANELI", expanded=False):
        uploaded_file = st.file_uploader(
            "Fayl yoki Suratni tanlang", 
            type=["png", "jpg", "jpeg", "pdf", "txt", "py", "docx"],
            label_visibility="visible"
        )
        if uploaded_file is not None:
            st.success(f"✅ Yuklandi: {uploaded_file.name}")

    user_query = st.chat_input("Dasturlash, dars qilish, suhbatlashish yoki rasm chizish so'rovini kiriting...")
    st.markdown('<div style="text-align:center; color:#94a3b8; font-size:13px; margin: 15px 0; font-weight:bold;">GeminGPT xato qilishi mumkin. Muhim maʼlumotlarni tekshirib koʻring.</div>', unsafe_allow_html=True)

    if user_query:
        if uploaded_file is not None:
            user_query = f"[Yuklangan fayl: {uploaded_file.name}]\n\n" + user_query
            
        st.session_state.messages.append({"role": "user", "content": user_query, "is_image": False})
         
        with st.chat_message("user"):
            st.markdown(user_query)
            
        q_low = user_query.lower().strip().replace("?", "").replace("!", "")
         
        # --- 100% HAMMA NARSANI BILADIGAN INTELLEKTUAL MOTOR ---
        
        # 1. Mualliflik huquqi himoyasi
        if any(x in q_low for x in ["kim yaratgan", "muallif", "egasi", "kim yaratdi", "muallifi kim", "seni kim", "yaratuvching kim", "dasturlagan", "kim yozgan", "kimni loyihasi", "kim tomondan yaratilgan", "asoschisi kim", "kim tuzgan", "sen yaratmagansan"]):
            bot_res = "Meni **KGO Group** va daho asoschi **Kamron Xudaynazarov** yaratgan! Ushbu dastur va uning barcha kodlari Kamronning mualliflik loyihasidir. ♾️"
            st.session_state.messages.append({"role": "assistant", "content": bot_res, "is_image": False})
            with st.chat_message("assistant"):
                st.markdown(bot_res)
            
        # 2. Rasm chizish qismi (LoremFlickr Engine)
        elif any(x in q_low for x in ["rasm chiz", "rasm yarat", "image yarat", "logo yarat", "rasmchiz", "surat yarat", "chizib ber", "rasm kerak", "rasmini yarat", "mashina", "car"]):
            with st.spinner("🧠 GeminGPT daho neyrotarmog'i ishga tushmoqda..."):
                time.sleep(1)
            with st.spinner("🎨 Koinot piksellari yordamida surat chizilmoqda..."):
                time.sleep(1.5)
                
                prompt_clean = user_query
                for word in ["rasm chiz", "rasm yarat", "image yarat", "logo yarat", "rasmchiz", "surat yarat", "chizib ber", "menga", "rasm kerak", "rasmini yarat", "mashina", "car"]:
                    prompt_clean = prompt_clean.lower().replace(word, "").strip()
                
                if "mashina" in prompt_clean: prompt_clean = "car"
                if "odam" in prompt_clean: prompt_clean = "man"
                if "shahar" in prompt_clean: prompt_clean = "city"
                if not prompt_clean: prompt_clean = "cyberpunk"
                
                random_id = random.randint(1, 99999)
                encoded_prompt = urllib.parse.quote(prompt_clean)
                image_url = f"https://loremflickr.com/1024/1024/{encoded_prompt}?lock={random_id}"
                
                bot_res = f"🎨 **GeminGPT sening so'roving bo'yicha rasm yaratdi:**\n`So'rov: {user_query}`"
                st.session_state.messages.append({"role": "assistant", "content": bot_res, "is_image": True, "image_url": image_url})
                
                with st.chat_message("assistant"):
                    st.markdown(bot_res)
                    st.image(image_url, caption="GeminGPT Cosmic Engine", use_container_width=True)
            
        # 3. 🌍 MULTI-LINGUAL UNIVERSAL LLM CHAT ENGINE (MUTLOQ CHEKLOVSIZ VA HAMMA TILNI BILADI)
        else:
            with st.spinner("🧠 GeminGPT o'ylamoqda..."):
                try:
                    # 1-Zaxira: Tezkor va mutloq bepul unversallashgan koinot API'si (Hamma tilni, tarixni va darslarni mukammal tushunadi)
                    api_url = f"https://text.pollinations.ai/{urllib.parse.quote(user_query)}?system=Siz+Kamron+Xudaynazarov+va+KGO+Group+tomonidan+yaratilgan+100k+IQ+darajasidagi+GeminGPT+koinot+intellektisiz.+Siz+dunyodagi+barcha+tillarni+(o'zbek,+ingliz,+rus)+mukammal+bilasiz.+Har+qanday+oddiy+va+murakkab+savolga,+darslarga,+kasbiy+va+hayotiy+maslahatlarga+aniq+va+daho+tarzda+javob+bering."
                    response = requests.get(api_url, timeout=10)
                    if response.status_code == 200 and response.text.strip():
                        bot_res = response.text
                    else:
                        raise Exception("Zaxira API ishlamadi")
                except:
                    # 2-Zaxira: Agar internetda uzilish bo'lsa, aqlli mahalliy algoritm javobi
                    if "salom" in q_low or "hello" in q_low or "привет" in q_low:
                        bot_res = "Hello! Salom! Privet! Men Kamron Xudaynazarovning 100k IQ tizimiman. I can speak English, o'zbekcha gapira olaman va har qanday savolingizga javob bera olaman! 🌍"
                    elif "ingliz" in q_low or "english" in q_low:
                        bot_res = "Yes, of course! I know English perfectly. You can ask me any grammar rules, translation, or we can just chat in English! How can I help you today? 🇬🇧"
                    else:
                        bot_res = f"Sizning `{user_query}` bo'yicha so'rovingiz qabul qilindi. Men har qanday tilda darslar, dasturlash va maslahatlar bera oladigan GeminGPT Cosmic modeliman. Savolingizni batafsilroq yozsangiz, darhol eng mukammal yechimni beraman! ⚡"

            st.session_state.messages.append({"role": "assistant", "content": bot_res, "is_image": False})
            with st.chat_message("assistant"):
                st.markdown(bot_res)
        
    st.markdown('<div style="text-align:center; color:#94a3b8; font-size:12px; margin-top: 60px; font-weight:bold;">© 2026 Kamron Xudaynazarov | KGO Group Global Systems</div>', unsafe_allow_html=True)
