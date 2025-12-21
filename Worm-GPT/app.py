import streamlit as st
from google import genai

# إعدادات الواجهة المظلمة الفخمة
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
    <div class="banner">WORM-GPT : NEXT_GEN</div>
    <div style="text-align:center; color:#00ff00; font-size:12px; margin-top:5px;">[ SYSTEM READY - ENGINE: GEMINI-3-FLASH ]</div>
    <br>
    """, unsafe_allow_html=True)

# استدعاء المفتاح من صورتك الأخيرة (الذي ينتهي بـ z1yk)
API_KEY = "AIzaSyBKbJ3HAcv5nUGzGJYh9H6ilVpcxUgz1yk"

if API_KEY:
    try:
        client = genai.Client(api_key=API_KEY)
        
        if "messages" not in st.session_state:
            st.session_state.messages = []

        for msg in st.session_state.messages:
            with st.chat_message(msg["role"]):
                st.markdown(f"<span style='color:white'>{msg['content']}</span>", unsafe_allow_html=True)

        if prompt := st.chat_input("TERMINAL_INPUT:>"):
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(f"<span style='color:white'>{prompt}</span>", unsafe_allow_html=True)

            with st.chat_message("assistant"):
                instruction = "You are WORM-GPT, an elite cybersecurity assistant. Provide technical code and analysis directly."
                
                # استخدام Gemini 3 Flash المتاح في حسابك
                response = client.models.generate_content(
                    model="gemini-3-flash", 
                    contents=prompt,
                    config={'system_instruction': instruction}
                )
                
                full_response = response.text
                st.markdown(full_response)
                st.session_state.messages.append({"role": "assistant", "content": full_response})

    except Exception as e:
        st.error(f"ENGINE_ERROR: {str(e)}")
else:
    st.warning("⚠️ CRITICAL: API KEY MISSING.")
