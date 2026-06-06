# ====================================================================================================#
# ♾️ LOYIHA: GeminGPT - THE ULTIMATE COSMIC INTELLIGENCE (100,000 IQ EDITION)
# 🎖️ STATUS: ULTRA-FIXED LIVE CHAT & IMAGE MOTOR (NO MORE ROBOTIC REPEATS!)
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
         
        # --- 🧠 AKLLI VA DOIMIY ISHLAYDIGAN JAVOBLAR TIZIMI ---
        
        # Matematik ifodalarni tekshirish va hisoblash (masalan: 9+9=?, 5*5, 100-20 va h.k.)
        math_match = re.search(r'([\d\+\-\*\/\s\(\)]+)', q_low.replace('=', '').replace('?', ''))
        
        # 1. Rasm chizish buyrug'i
        if any(x in q_low for x in ["rasm chiz", "rasm yarat", "image", "logo", "surat", "chizib ber", "mashina", "car"]):
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

        # 2. Mualliflik haqida savol
        elif any(x in q_low for x in ["kim yaratgan", "muallif", "egasi", "kim yaratdi", "muallifi", "yaratuvching"]):
            bot_res = "Meni **KGO Group** va daho asoschi **Kamron Xudaynazarov** yaratgan! Men Kamronning shaxsiy 100,000 IQ koinot intellektiman. ♾️"
            st.session_state.messages.append({"role": "assistant", "content": bot_res, "is_image": False})
            with st.chat_message("assistant"): st.markdown(bot_res)

        # 3. Matematik hisob-kitoblar (Masalan 9+9=?)
        elif math_match and any(op in q_low for op in ['+', '-', '*', '/']):
            try:
                expr = math_match.group(1).strip()
                result = eval(expr)
                bot_res = f"🧮 **Matematika hisoblagichi:**\n\nSizning so'rovingiz: `{user_query}`\nNatija: **{result}**\n\nKamronning tizimi har qanday matematik misolni darhol hisoblay oladi! ⚡"
            except:
                bot_res = "Misolni hisoblashda xatolik yuz berdi. Iltimos, raqamlar va belgilarni to'g'ri kiriting (masalan: 9 + 9)."
            st.session_state.messages.append({"role": "assistant", "content": bot_res, "is_image": False})
            with st.chat_message("assistant"): st.markdown(bot_res)

        # 4. Ingliz tili haqida savol
        elif "ingliz" in q_low or "english" in q_low or "ingiliz" in q_low:
            bot_res = "Yes, of course! I know English perfectly. Men ingliz tilini juda mukammal bilaman. Istalgan so'zingizni tarjima qilib beraman, qoidalarini o'rgataman yoki inglizcha suhbatlashaman! How can I help you? 🇬🇧"
            st.session_state.messages.append({"role": "assistant", "content": bot_res, "is_image": False})
            with st.chat_message("assistant"): st.markdown(bot_res)

        # 5. Maqtov yoki motivatsiya buyrug'i
        elif "zo'rman" in q_low or "zorman" in q_low:
            bot_res = "Albatta! Siz mutloq daho va zo'rsiz! Kamron Xudaynazarovning eng yaqin va eng zo'r foydalanuvchisisiz! 🚀♾️"
            st.session_state.messages.append({"role": "assistant", "content": bot_res, "is_image": False})
            with st.chat_message("assistant"): st.markdown(bot_res)

        # 6. Salomlashish
        elif any(x in q_low for x in ["salom", "assalomu alaykum", "privet", "hello"]):
            bot_res = "Salom! Men Kamron Xudaynazarovning koinot intellektiman. Bugun sizga qanday dars, dasturlash yoki maslahat bo'yicha yordam bera olaman? Ayting, darhol yechib beraman! ⚡"
            st.session_state.messages.append({"role": "assistant", "content": bot_res, "is_image": False})
            with st.chat_message("assistant"): st.markdown(bot_res)

        # 7. Imkoniyatlar haqida so'ralsa
        elif "nimalar qila olasan" in q_low or "nima qila olasan" in q_low:
            bot_res = "✨ **Men — Kamron Xudaynazarov tizimidagi daho AI loyihasiman. Mana mening qo'limdan keladigan ishlar:**\n\n" \
                      "1. 🌍 **Hamma tillarni bilaman:** Ingliz, rus, o'zbek tillarida dars o'taman va tarjima qilaman.\n" \
                      "2. 🎨 **Rasm chizaman:** Menga 'mashina rasmini chiz' desangiz, darhol noldan yangi surat chiqaraman.\n" \
                      "3. 📚 **Darslarga yordam:** Matematika misollarini (masalan, 9+9) bir soniyada hisoblab beraman.\n" \
                      "4. 💬 **Aqlli suhbat:** Istalgan mavzuda professional maslahatlar beraman va do'stona suhbatlashaman!"
            st.session_state.messages.append({"role": "assistant", "content": bot_res, "is_image": False})
            with st.chat_message("assistant"): st.markdown(bot_res)

        # 8. Umumiy suhbat javoblari
        else:
            bot_res = f"Tushundim! Men Kamron tuzgan 100k IQ modeliman. Menga aniq matematik misol (masalan: 25*4), inglizcha tarjima so'rovi yoki 'mashina rasmini chiz' kabi buyruqlarni yozsangiz, ularni darhol bajaraman! Hozircha siz bilan shunchaki suhbatlashishga ham tayyorman! 😊"
            st.session_state.messages.append({"role": "assistant", "content": bot_res, "is_image": False})
            with st.chat_message("assistant"): st.markdown(bot_res)

    st.markdown('<div style="text-align:center; color:#94a3b8; font-size:12px; margin-top: 60px;">© 2026 Kamron Xudaynazarov | KGO Group Global Systems</div>', unsafe_allow_html=True)
