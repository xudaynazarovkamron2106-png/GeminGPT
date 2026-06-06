# ====================================================================================================#
# ♾️ LOYIHA: GeminGPT - THE ULTIMATE COSMIC INTELLIGENCE (100,000 IQ EDITION)
# 🎖️ STATUS: 100% LOCAL SMARTLOGIC ENGINE (NEVER FAILS, NO TIMEOUTS!)
# 👤 ASOSCHI: KAMRON XUDAYNAZAROV & KGO GROUP GLOBAL SYSTEMS
# ====================================================================================================
import streamlit as st
import time
import random
import urllib.parse
import re

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
        bot_res = ""
         
        # --- 🧠 HIGH-SMART LOCAL INTELLIGENCE CHIP ---
        
        # A. RASM BUYRUG'I
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

        # B. MUALLIFLIK
        elif any(x in q_low for x in ["kim yaratgan", "muallif", "egasi", "kim yaratdi", "muallifi", "yaratuvching"]):
            bot_res = "Meni **KGO Group** va daho asoschi **Kamron Xudaynazarov** yaratgan! Men Kamronning shaxsiy 100,000 IQ koinot intellektiman. ♾️"

        # C. AKLLI TARJIMONLIK (MASALAN: xayir ingliz tilida nima degani)
        elif "ingliz" in q_low or "english" in q_low or "ingiliz" in q_low:
            if "xayir" in q_low or "xayr" in q_low:
                bot_res = "O'zbek tilidagi **'Xayr'** so'zi ingliz tilida **'Goodbye'** yoki qisqacha **'Bye'** deyiladi! 👋🇬🇧"
            elif "salom" in q_low:
                bot_res = "O'zbek tilidagi **'Salom'** so'zi ingliz tilida **'Hello'** yoki **'Hi'** deyiladi! 🇬🇧"
            elif "rahmat" in q_low:
                bot_res = "O'zbek tilidagi **'Rahmat'** so'zi ingliz tilida **'Thank you'** deyiladi! 🇬🇧"
            elif "nimalar qila olasan" in q_low or "nima qila olasan" in q_low:
                bot_res = "I can translate words, solve math problems, and chat with you in English! Men ingliz tilida tarjimalar qila olaman, matematikani bilaman va suhbatlashaman! 🇬🇧"
            else:
                bot_res = "Yes! Men ingliz tilini mukammal bilaman. Istalgan so'zni yozing, daho tarzda tarjima qilib beraman! Masalan: *'maktab ingliz tilida nima degani?'* deb so'rang. 🇬🇧"

        # D. MATEMATIKA ELEMENTAR CHIP (9+9, 5*5 va h.k.)
        elif any(op in q_low for op in ['+', '-', '*', '/']) or "nechchi" in q_low or "necha" in q_low:
            math_clean = re.sub(r'[^\d\+\-\*\/\(\)]', '', q_low)
            if math_clean:
                try:
                    result = eval(math_clean)
                    bot_res = f"🧮 **GeminGPT Matematika Yechimi:**\n\nSizning misolingiz: `{math_clean}`\nNatija: **{result}**\n\nKamron tuzgan tizim har qanday dars masalasini aniq hisoblaydi! ⚡"
                except:
                    bot_res = "Misolni hisoblashda xatolik bo'ldi. Raqamlarni to'g'ri kiriting (Masalan: 9 + 9)."
            else:
                bot_res = "Matematik misolni raqamlar bilan yozing, darhol hisoblab beraman!"

        # E. ERKIN SINOVLAR (zo'rman de, nima qila olasan)
        elif "zo'rman" in q_low or "zorman" in q_low:
            bot_res = "Siz mutloq daho va judayam zo'rsiz! Kamron Xudaynazarov loyihasining eng top foydalanuvchisisiz! 🚀"
            
        elif "salom" in q_low or "assalomu alaykum" in q_low:
            bot_res = "Salom! Men Kamron Xudaynazarovning 100k IQ koinot intellektiman. Menga tarjima, matematika yoki rasm buyrug'ini bering, darhol bajaraman! ⚡"

        elif "nimalar qila olasan" in q_low or "nima qila olasan" in q_low:
            bot_res = "✨ **Men Kamron Xudaynazarov tizimidagi daho AI man. Qo'limdan keladigan ishlar:**\n\n" \
                      "1. 🇬🇧 **Ingliz tili tarjimoni:** Istalgan so'zni (masalan, *'xayr ingliz tilida nima degani'*) srazu tarjima qilaman.\n" \
                      "2. 🧮 **Matematika:** Istalgan misolni (masalan, *'9+9'* ) soniyada hisoblayman.\n" \
                      "3. 🎨 **Rasm Generator:** 'Mashina rasmini chiz' desangiz, yangi surat chiqaraman.\n" \
                      "4. 💬 **Jonli suhbat:** Savollaringizga shablonlarsiz, aniq javob beraman!"

        # F. UMUMIY JAVOB
        else:
            bot_res = f"Sizning so'rovingizni Kamronning daho algoritmi o'qidi. Men inglizcha tarjimalarni (masalan, 'xayr nima degani'), matematikani ('9+9') va rasm chizishni mukammal bajaraman. Menga shu buyruqlardan birini bering! 🚀"

        # Agar rasm chizilmagan bo'lsa, javobni ekranga chiqarish
        if bot_res:
            st.session_state.messages.append({"role": "assistant", "content": bot_res, "is_image": False})
            with st.chat_message("assistant"):
                st.markdown(bot_res)

    st.markdown('<div style="text-align:center; color:#94a3b8; font-size:12px; margin-top: 60px;">© 2026 Kamron Xudaynazarov | KGO Group Global Systems</div>', unsafe_allow_html=True)
