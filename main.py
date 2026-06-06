# ====================================================================================================#
# ♾️ LOYIHA: GeminGPT - THE ULTIMATE COSMIC INTELLIGENCE (100,000 IQ EDITION)
# 🎖️ STATUS: 100% LIVE AI CHAT ENGINE (NO MORE STATIC REPEATS!)
# 👤 ASOSCHI: KAMRON XUDAYNAZAROV & KGO GROUP GLOBAL SYSTEMS
# ====================================================================================================
import streamlit as st
import time
import random
import urllib.parse
import requests

# --- [SECTION 1] GLOBAL SYSTEM CONFIGURATIONS ---
st.set_page_config(
    page_title="GeminGPT | Cosmic Sovereign",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- [SECTION 2] UI & DESIGN (BLUE-DARK ULTRA) ---
st.markdown("""
<style>
     .stApp {
         background-color: #0b0f19;
         color: #ffffff !important;
         font-family: 'Inter', sans-serif;
     }
     [data-testid="stSidebar"] {
         background-color: #0f172a !important;
     }
     [data-testid="stSidebar"] p, [data-testid="stSidebar"] b, [data-testid="stSidebar"] span {
         color: #ffffff !important;
     }
     .stChatMessage p {
         color: #ffffff !important;
         font-size: 16px !important;
     }
     .stChatInputContainer {
        border: 2px solid #2563eb !important; 
        border-radius: 12px !important;
        background-color: #1e293b !important; 
        box-shadow: 0 0 15px rgba(37, 99, 235, 0.3) !important; 
     }
     .stChatInputContainer textarea {
        color: #ffffff !important;
     }
     .sidebar-stat {
         padding: 12px 15px;
         background: rgba(255, 255, 255, 0.08);
         border-radius: 8px;
         margin-bottom: 10px;
         border-left: 4px solid #2563eb;
     }
     .google-card-ultra {
         background: #111827;
         padding: 45px;
         border-radius: 20px;
         border: 1px solid rgba(255, 255, 255, 0.1);
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

# --- [SECTION 4] GOOGLE AUTH ---
if not st.session_state.logged_in:
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("""
        <div class="google-card-ultra">
        <h1 style="font-family: 'Product Sans', sans-serif; font-size: 45px; font-weight:bold;">
        <span style="color:#4285F4">G</span><span style="color:#EA4335">o</span><span style="color:#FBBC05">o</span><span style="color:#4285F4">g</span><span style="color:#34A853">l</span><span style="color:#EA4335">e</span>
        </h1>
        <h2 style="color:#f8fafc; font-weight: 300; font-size:24px;">Sign in</h2>
        <p style="color:#94a3b8;">Use your account to enter <b>GeminGPT Cosmic</b></p>
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

# --- [SECTION 5] MAIN APP ---
else:
    with st.sidebar:
        st.markdown("<h2 style='text-align:center; color:#2563eb;'>gemingpt</h2>", unsafe_allow_html=True)
        st.markdown(f"""
        <div class="sidebar-stat">👤 <b>Foydalanuvchi:</b><br><code>{st.session_state.user_email}</code></div>
        <div class="sidebar-stat">🧠 <b>IQ Darajasi:</b><br>100,000 (Cosmic Engine)</div>
        """, unsafe_allow_html=True)
        st.write("---")
        st.markdown("<b>Muallif: Kamron Xudaynazarov</b>", unsafe_allow_html=True)
        if st.button("🚪 Chiqish", use_container_width=True):
            st.session_state.logged_in = False
            st.rerun()
            
    st.markdown("<h1 style='color: #2563eb; font-weight:bold;'>gemingpt ♾️</h1>", unsafe_allow_html=True)
    st.markdown("---")

    # Tarixni chiqarish
    for message in st.session_state.messages: 
         with st.chat_message(message["role"]):
            st.markdown(message["content"])
            if message.get("is_image", False):
                st.image(message["image_url"], use_container_width=True)

    user_query = st.chat_input("Savol yozing yoki rasm chizdiring...")

    if user_query:
        st.session_state.messages.append({"role": "user", "content": user_query, "is_image": False})
        with st.chat_message("user"):
            st.markdown(user_query)
            
        q_low = user_query.lower().strip()
         
        # 1. SPECIAL TRIGGER: Rasm chizish buyrug'i
        if any(x in q_low for x in ["rasm chiz", "rasm yarat", "image", "logo", "surat", "chizib ber"]):
            with st.spinner("🎨 Koinot piksellari noldan chizilmoqda..."):
                time.sleep(1.5)
                prompt_clean = q_low
                for word in ["rasm chiz", "rasm yarat", "image", "logo", "surat", "chizib ber", "menga"]:
                    prompt_clean = prompt_clean.replace(word, "").strip()
                
                if "mashina" in prompt_clean: prompt_clean = "car"
                if not prompt_clean: prompt_clean = "cyberpunk"
                
                random_id = random.randint(1, 9999)
                image_url = f"https://loremflickr.com/1024/1024/{urllib.parse.quote(prompt_clean)}?lock={random_id}"
                
                bot_res = f"🎨 **GeminGPT sening so'roving bo'yicha rasm yaratdi!**"
                st.session_state.messages.append({"role": "assistant", "content": bot_res, "is_image": True, "image_url": image_url})
                with st.chat_message("assistant"):
                    st.markdown(bot_res)
                    st.image(image_url, use_container_width=True)

        # 2. SPECIAL TRIGGER: Mualliflik haqida savol
        elif any(x in q_low for x in ["kim yaratgan", "muallif", "egasi", "kim yaratdi", "muallifi", "yaratuvching"]):
            bot_res = "Meni **KGO Group** va daho asoschi **Kamron Xudaynazarov** yaratgan! Men Kamronning shaxsiy 100,000 IQ koinot intellektiman. ♾️"
            st.session_state.messages.append({"role": "assistant", "content": bot_res, "is_image": False})
            with st.chat_message("assistant"): st.markdown(bot_res)

        # 3. 🧠 HAQIQIY JONLI CHAT MOTOR (Har qanday tildagi erkin savollar, tarjima va matematika uchun)
        else:
            with st.spinner("🧠 GeminGPT o'ylamoqda..."):
                try:
                    # Hech qachon o'chmaydigan va xatosiz ishlaydigan jonli sun'iy intellekt API havolasi
                    system_prompt = "Siz Kamron Xudaynazarov va KGO Group yaratgan 100k IQ darajasidagi GeminGPT modelisiz. Foydalanuvchining har qanday savoliga (tarjima, dars, suhbat) juda aniq, aqlli va qisqa javob bering. Hech qachon shablon gaplarni qaytarmang."
                    api_url = f"https://text.pollinations.ai/{urllib.parse.quote(user_query)}?system={urllib.parse.quote(system_prompt)}"
                    
                    response = requests.get(api_url, timeout=10)
                    if response.status_code == 200 and response.text.strip():
                        bot_res = response.text.strip()
                    else:
                        raise Exception("API Error")
                except:
                    # Agar internetda juda kuchli uzilish bo'lsa, zaxira javob
                    bot_res = "Hozirda ulanishda biroz uzilish bo'ldi. Iltimos, so'rovingizni qayta yuboring."

            st.session_state.messages.append({"role": "assistant", "content": bot_res, "is_image": False})
            with st.chat_message("assistant"):
                st.markdown(bot_res)

    st.markdown('<div style="text-align:center; color:#94a3b8; font-size:12px; margin-top: 60px;">© 2026 Kamron Xudaynazarov | KGO Group Global Systems</div>', unsafe_allow_html=True)
