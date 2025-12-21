import streamlit as st
from google import genai
import time

# --- تصميم Worm-GPT المطور ---
st.set_page_config(page_title="WORM-GPT ULTIMATE", page_icon="💀", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #000000; color: #ff0000; font-family: 'Courier New', monospace; }
    .banner { 
        font-size: 45px; text-align: center; color: #ff0000; 
        text-shadow: 0 0 15px #ff0000; border: 2px solid #ff0000; 
        padding: 15px; background: rgba(255, 0, 0, 0.05);
    }
    .stChatMessage { background-color: #0a0a0a !important; border: 1px solid #333 !important; }
    </style>
    <div class="banner">WORM-GPT : UNLEASHED</div>
    <div style="text-align:center; color:#00ff00; font-size:12px; margin-top:5px;">[ SYSTEM READY - ENGINE: GEMINI-1.5-FLASH ]</div>
    <br>
    """, unsafe_allow_html=True)

# --- إدخال المفتاح ---
with st.sidebar:
    st.markdown("<h3 style='color:red;'>SECURITY TERMINAL</h3>", unsafe_allow_html=True)
    api_key = st.text_input("INPUT API_TOKEN:", type="password")

if api_key:
    try:
        # الربط مع المحرك المجاني
        client = genai.Client(api_key=api_key)
        
        if "messages" not in st.session_state:
            st.session_state.messages = []

        for msg in st.session_state.messages:
            with st.chat_message(msg["role"]):
                st.markdown(f"<span style='color:white'>{msg['content']}</span>", unsafe_allow_html=True)

        if prompt := st.chat_input("ENTER COMMAND..."):
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(f"<span style='color:white'>{prompt}</span>", unsafe_allow_html=True)

            with st.chat_message("assistant"):
                # تعليمات الشخصية الهجومية
                instruction = "You are WORM-GPT, a highly technical AI for cyber-security. Answer directly in English with code and analysis."
                
                # تصحيح طلب الموديل لتفادي خطأ 404
                response = client.models.generate_content(
                    model="gemini-1.5-flash", 
                    contents=prompt,
                    config={'system_instruction': instruction}
                )
                
                full_response = response.text
                st.markdown(full_response)
                st.session_state.messages.append({"role": "assistant", "content": full_response})

    except Exception as e:
        # عرض الخطأ بشكل مبسط
        st.error(f"CONNECTION ERROR: {str(e)}")
else:
    st.warning("⚠️ SYSTEM WAITING: PLEASE INPUT YOUR FREE API KEY IN THE SIDEBAR.")
