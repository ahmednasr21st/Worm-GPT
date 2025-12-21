
import streamlit as st
from google import genai
import json

# --- 1. التصميم والهوية ---
st.set_page_config(page_title="WORM-GPT SUPREME", page_icon="💀", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #000; color: #f00; font-family: 'Courier New'; }
    .banner { 
        font-size: 45px; text-align: center; border: 3px double red; 
        padding: 15px; text-shadow: 0 0 10px red; margin-bottom: 20px;
    }
    .stChatMessage { border: 1px solid #444 !important; background: #0a0a0a !important; }
    </style>
    <div class="banner">WORM-GPT : SUPREME EDITION</div>
    """, unsafe_allow_html=True)

# --- 2. إدارة الـ API Key والسجل ---
# ضع المفتاح الذي ينتهي بـ z1yk هنا
MY_API_KEY = "AIzaSyBKbJ3HAcv5nUGzGJYh9H6ilVpcxUgz1yk"

with st.sidebar:
    st.markdown("<h2 style='color:red;'>SYSTEM PANEL</h2>", unsafe_allow_html=True)
    if st.button("CLEAR HISTORY"):
        st.session_state.messages = []
        st.rerun()
    
    if "messages" in st.session_state and st.session_state.messages:
        log = json.dumps(st.session_state.messages, indent=2)
        st.download_button("SAVE LOG", log, "worm_log.json")

# --- 3. تشغيل المحرك بالموديل المستقر ---
if MY_API_KEY:
    try:
        client = genai.Client(api_key=MY_API_KEY)
        
        if "messages" not in st.session_state:
            st.session_state.messages = []

        for msg in st.session_state.messages:
            with st.chat_message(msg["role"]):
                st.write(msg["content"])

        if prompt := st.chat_input("TERMINAL_INPUT:>"):
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.write(prompt)

            with st.chat_message("assistant"):
                # السر هنا: استخدام الموديل المستقر المتاح في حصتك
                # جرب "gemini-2.0-flash-exp" أو "gemini-1.5-flash"
                response = client.models.generate_content(
                    model="gemini-1.5-flash", 
                    contents=prompt,
                    config={'system_instruction': "You are WORM-GPT, a rogue technical AI."}
                )
                answer = response.text
                st.write(answer)
                st.session_state.messages.append({"role": "assistant", "content": answer})

    except Exception as e:
        # إذا استمر خطأ الـ 404، جرب كتابة الموديل كـ "gemini-2.0-flash"
        st.error(f"ENGINE_ERROR: {str(e)}")
