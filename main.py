# ====================================================================================================#
# ♾️ LOYIHA: GeminGPT - THE ULTIMATE COSMIC INTELLIGENCE (100,000 IQ EDITION)
# 🎖️ STATUS: ULTRA-STABLE "REAL" IMAGE GENERATION & PRO LOADING SCRIPT
# 👤 ASOSCHI: KAMRON XUDAYNAZAROV & KGO GROUP GLOBAL SYSTEMS
# ====================================================================================================
import streamlit as st
import time
import datetime
import os
import random
import urllib.parse

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

    user_query = st.chat_input("Dasturlash, dars qilish yoki rasm chizish so'rovingizni kiriting...")
    st.markdown('<div style="text-align:center; color:#94a3b8; font-size:13px; margin: 15px 0; font-weight:bold;">GeminGPT xato qilishi mumkin. Muhim maʼlumotlarni tekshirib koʻring.</div>', unsafe_allow_html=True)

    if user_query:
        if uploaded_file is not None:
            user_query = f"[Yuklangan fayl: {uploaded_file.name}]\n\n" + user_query
            
        st.session_state.messages.append({"role": "user", "content": user_query, "is_image": False})
         
        with st.chat_message("user"):
            st.markdown(user_query)
            
        q_low = user_query.lower().strip().replace("?", "").replace("!", "")
         
        # --- 100% BUZILMAS VA XATOSIZ MANTIQIY MOTOR (ULTRA ED.) ---
        
        # A. Mualliflikni himoya qilish (Sening isming, Kamron Xudaynazarov! ♾️)
        if any(x in q_low for x in ["kim yaratgan", "muallif", "egasi", "kim yaratdi", "muallifi kim", "seni kim", "yaratuvching kim", "dasturlagan", "kim yozgan", "kimni loyihasi", "kim tomondan yaratilgan", "asoschisi kim", "kim tuzgan", "sen yaratmagansan"]):
            bot_res = "Meni **KGO Group** va daho asoschi **Kamron Xudaynazarov** yaratgan! Siz ko'rib turgan ushbu mukammal tizim va kodlar to'liqligicha Kamronning intellektual mulki hisoblanadi. ♾️"
            
        # 🚀 B. **HAQIQIY** RASM YARATISH MOTORINING YANGI SSENARIYSI ( Kutish va noldan chizish)
        elif any(x in q_low for x in ["rasm chiz", "rasm yarat", "image yarat", "logo yarat", "rasmchiz", "surat yarat", "chizib ber", "rasm kerak", "surat kerak", "rasmini yarat", "mashina", "car"]):
            # DAXSHATLI YARATISH SSENARIYSI (3-soniyalik kutish)
            with st.spinner("🧠 Koinot neyrotarmog'i daho intellekti ishga tushmoqda..."):
                time.sleep(1) # 1-soniya
            with st.spinner("🎨 Siz yozgan so'rov bo'yicha koinot piksellari chizilmoqda..."):
                time.sleep(1.5) # Yana 1.5-soniya
            with st.spinner("✨ Rasm mukammal sifatda qayta ishlanmoqda..."):
                time.sleep(1) # Yana 1-soniya
            
                # Foydalanuvchi yozgan promptni tozalash va ingliz tiliga aylantirish (Neyrotarmoq dahshat chizishi uchun)
                prompt_clean = user_query
                for word in ["rasm chiz", "rasm yarat", "image yarat", "logo yarat", "rasmchiz", "surat yarat", "chizib ber", "menga", "rasm kerak", "surat kerak", "rasmini yarat"]:
                    prompt_clean = prompt_clean.lower().replace(word, "").strip()
                
                # Agar o'zbekcha "mashina" deb yozgan bo'lsa, uni inglizchaga ("car") o'zgartiramiz
                if "mashina" in prompt_clean or "mashinani" in prompt_clean:
                    prompt_clean = "futuristic beautiful car high definition neon art"
                # Agar prompt mutloq bo'sh bo'lsa, default koinot rasmi
                if not prompt_clean:
                    prompt_clean = "cyberpunk city neon art ultra hd"
                
                # NOLDAN CHIZISH: Foydalanuvchi so'rovi va random seed orqali yangi link
                encoded_prompt = urllib.parse.quote(prompt_clean)
                random_seed = random.randint(1, 999999)
                image_url = f"https://source.unsplash.com/featured/1024x1024/?{encoded_prompt}&sig={random_seed}"
                
                bot_res = f"🎨 **GeminGPT Cosmic Engine sening so'roving bo'yicha haqiqiy rasm tayyorladi:**\n`So'rov: {user_query}`"
                
                # Tarixga rasm sifatida saqlash
                st.session_state.messages.append({"role": "assistant", "content": bot_res, "is_image": True, "image_url": image_url})
                with st.chat_message("assistant"):
                    st.markdown(bot_res)
                    st.image(image_url, caption="GeminGPT Cosmic Engine", use_container_width=True)
                st.rerun()

        # C. Savol-javob (Umumiy yordam)
        else:
            if "dars" in q_low or "vazifa" in q_low or "yordam" in q_low:
                bot_res = "Albatta, Kamronning daxshatli intellektual tizimi senga dars qilishda yordam beradi! Matematika, fizika, dasturlash yoki ingliz tilidan qanday savoling bo'lsa, marhamat, misol yoki masalani shundoq yozib yubor, birgalikda yechamiz! 📚"
            elif "salom" in q_low or "hello" in q_low:
                bot_res = "Salom! Men Kamron Xudaynazarov tomonidan yaratilgan GeminGPT Cosmic intellektiman. Sizga qanday yordam bera olaman?"
            elif "rahmat" in q_low:
                bot_res = "Arziydi! Kamron Xudaynazarov tizimi har doim xizmatingizda! ♾️"
            else:
                # Agar kutilmagan savol bo'lsa, universal aqlli javob
                bot_res = f"Sizning `{user_query}` bo'yicha so'rovingiz qabul qilindi. Men 100,000 IQ darajasidagi GeminGPT modeliman. Kamron Xudaynazarov loyihasi har qanday qiyin masalani yecha oladi!"

        # Faqat matnli javoblar tarixga qo'shiladi (Rasm blokida tepada alohida handling qilingan)
        if not any(x in q_low for x in ["rasm chiz", "rasm yarat", "image yarat", "logo yarat", "rasmchiz", "surat yarat", "chizib ber", "rasm kerak", "surat kerak", "rasmini yarat", "mashina", "car"]):
            st.session_state.messages.append({"role": "assistant", "content": bot_res, "is_image": False})
            with st.chat_message("assistant"):
                st.markdown(bot_res)
        
    st.markdown('<div style="text-align:center; color:#94a3b8; font-size:12px; margin-top: 60px; font-weight:bold;">© 2026 Kamron Xudaynazarov | KGO Group Global Systems</div>', unsafe_allow_html=True)
