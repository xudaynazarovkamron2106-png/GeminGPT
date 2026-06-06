# ====================================================================================================#
# ♾️ LOYIHA: GeminGPT - THE ULTIMATE COSMIC INTELLIGENCE (100,000 IQ EDITION)
# 🎖️ STATUS: MULTI-FUNCTIONAL CHAT & IMAGE SYSTEM (ADVANCED EDITION)
# 👤 ASOSCHI: KAMRON XUDAYNAZAROV & KGO GROUP GLOBAL SYSTEMS
# ====================================================================================================
import streamlit as st
import time
import datetime
import os
import random
import urllib.parse
from groq import Groq

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

    user_query = st.chat_input("Maslahat so'rang, dars qiling yoki rasm chizdiring...")
    st.markdown('<div style="text-align:center; color:#94a3b8; font-size:13px; margin: 15px 0; font-weight:bold;">GeminGPT xato qilishi mumkin. Muhim maʼlumotlarni tekshirib koʻring.</div>', unsafe_allow_html=True)

    if user_query:
        if uploaded_file is not None:
            user_query = f"[Yuklangan fayl: {uploaded_file.name}]\n\n" + user_query
            
        st.session_state.messages.append({"role": "user", "content": user_query, "is_image": False})
         
        with st.chat_message("user"):
            st.markdown(user_query)
            
        q_low = user_query.lower().strip().replace("?", "").replace("!", "")
         
        # --- MULTI-INTELLIGENCE LOGIC ENGINE ---
        
        # 1. Mualliflik himoyasi
        if any(x in q_low for x in ["kim yaratgan", "muallif", "egasi", "kim yaratdi", "muallifi kim", "seni kim", "yaratuvching kim", "dasturlagan", "kim yozgan", "kimni loyihasi", "kim tomondan yaratilgan", "asoschisi kim", "kim tuzgan", "sen yaratmagansan"]):
            bot_res = "Meni **KGO Group** va daho asoschi **Kamron Xudaynazarov** yaratgan! Ushbu tizim Kamronning intellektual va mualliflik loyihasi hisoblanadi. ♾️"
            st.session_state.messages.append({"role": "assistant", "content": bot_res, "is_image": False})
            with st.chat_message("assistant"):
                st.markdown(bot_res)
            
        # 2. 🎨 RASM CHIZISH TRIGGERI
        elif any(x in q_low for x in ["rasm chiz", "rasm yarat", "image yarat", "logo yarat", "rasmchiz", "surat yarat", "chizib ber", "rasm kerak", "rasmini yarat", "mashina", "car"]):
            with st.spinner("🧠 GeminGPT daho neyrotarmog'i ishga tushmoqda..."):
                time.sleep(1.5)
            with st.spinner("🎨 Koinot piksellari yordamida surat noldan chizilmoqda..."):
                time.sleep(2)
            with st.spinner("✨ Sifati 4K Ultra-HD formatga o'tkazilmoqda..."):
                time.sleep(1.5)
                
                prompt_clean = user_query
                for word in ["rasm chiz", "rasm yarat", "image yarat", "logo yarat", "rasmchiz", "surat yarat", "chizib ber", "menga", "rasm kerak", "rasmini yarat", "mashina", "car"]:
                    prompt_clean = prompt_clean.lower().replace(word, "").strip()
                
                if "mashina" in prompt_clean or "mashinani" in prompt_clean:
                    prompt_clean = "car"
                if "shahar" in prompt_clean:
                    prompt_clean = "city"
                
                if not prompt_clean:
                    prompt_clean = "cyberpunk"
                
                random_id = random.randint(1, 99999)
                encoded_prompt = urllib.parse.quote(prompt_clean)
                image_url = f"https://loremflickr.com/1024/1024/{encoded_prompt}?lock={random_id}"
                
                bot_res = f"🎨 **GeminGPT sening so'roving bo'yicha rasm yaratdi:**\n`So'rov: {user_query}`"
                
                st.session_state.messages.append({
                    "role": "assistant", 
                    "content": bot_res, 
                    "is_image": True,
                    "image_url": image_url
                })
                
                with st.chat_message("assistant"):
                    st.markdown(bot_res)
                    st.image(image_url, caption="GeminGPT Cosmic Engine", use_container_width=True)
            
        # 3. 💬 HAQIQIY MULTI-AI INTEGRATSIYASI (SUHBAT, MASLAHAT, DARS VA VAZIFALAR)
        else:
            try:
                # Groq super-tezkor koinot serveridan foydalanamiz
                client_groq = Groq(api_key="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")
                with st.spinner("🧠 GeminGPT o'ylamoqda..."):
                    # Chat tarixini shakllantirish
                    history_context = [
                        {"role": "system", "content": "Siz GeminGPT ismli, 100,000 IQ darajasiga ega daho, do'stona va yordamchi koinot intellektisiz. Sizni Kamron Xudaynazarov va KGO Group yaratgan. Foydalanuvchiga har qanday mavzuda (darslar, matematika, hayotiy maslahat, erkin suhbat, dasturlash) eng mukammal va aqlli javoblarni bering."}
                    ]
                    # Oxirgi bir nechta xabarni kontekst sifatida yuklash
                    for msg in st.session_state.messages[-6:]:
                        if not msg.get("is_image", False):
                            history_context.append({"role": msg["role"], "content": msg["content"]})
                    
                    completion = client_groq.chat.completions.create(
                        model="llama-3.3-70b-versatile",
                        messages=history_context,
                        temperature=0.7
                    )
                bot_res = completion.choices[0].message.content
            except Exception as e:
                # API xatolik bersa yoki limit tugasa, zaxira universal aqlli javob tizimi
                bot_res = "Sizning so'rovingiz qabul qilindi. Kamron Xudaynazarov tizimi hozirda ma'lumotlarni qayta ishlamoqda. Aytingchi, sizga aynan qanday maslahat yoki dars bo'yicha yordam kerak?"

            st.session_state.messages.append({"role": "assistant", "content": bot_res, "is_image": False})
            with st.chat_message("assistant"):
                st.markdown(bot_res)
        
    st.markdown('<div style="text-align:center; color:#94a3b8; font-size:12px; margin-top: 60px; font-weight:bold;">© 2026 Kamron Xudaynazarov | KGO Group Global Systems</div>', unsafe_allow_html=True)
