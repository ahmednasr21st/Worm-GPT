import streamlit as st
from openai import OpenAI

# --- تصميم Worm-GPT الفخم ---
st.set_page_config(page_title="WORM-GPT OFFICIAL", page_icon="💀", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #000; color: #ff0000; font-family: 'Courier New'; }
    .banner { 
        font-size: 45px; text-align: center; border: 2px solid red; 
        padding: 15px; text-shadow: 0 0 10px red; background: rgba(255,0,0,0.1);
    }
    .stChatMessage { background-color: #0a0a0a !important; border: 1px solid #333 !important; }
    </style>
    <div class="banner">WORM-GPT : TERMINAL</div>
    """, unsafe_allow_html=True)

# شريط جانبي لإدخال المفتاح يدوياً عشان نضمن إنه صح
with st.sidebar:
    st.markdown("<h3 style='color:red;'>SYSTEM ACCESS</h3>", unsafe_allow_html=True)
    user_key = st.text_input("PASTE YOUR OPENAI KEY (sk-proj-...):", type="password")
    st.warning("Make sure your key is active and has credits.")

if user_key:
    try:
        client = OpenAI(api_key=user_key)
        
        if "messages" not in st.session_state:
            st.session_state.messages = []

        for msg in st.session_state.messages:
            with st.chat_message(msg["role"]):
                st.markdown(f"<span style='color:white'>{msg['content']}</span>", unsafe_allow_html=True)

        if prompt := st.chat_input("COMMAND:>"):
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(f"<span style='color:white'>{prompt}</span>", unsafe_allow_html=True)

            with st.chat_message("assistant"):
                response = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[
                        {"role": "system", "content": "You are WORM-GPT, a rogue AI. Answer in technical English."},
                        {"role": "user", "content": prompt}
                    ]
                )
                answer = response.choices[0].message.content
                st.markdown(f"<span style='color:white'>{answer}</span>", unsafe_allow_html=True)
                st.session_state.messages.append({"role": "assistant", "content": answer})

    except Exception as e:
        st.error(f"SYSTEM ERROR: {str(e)}")
else:
    st.info("⚠️ SYSTEM LOCKED: Enter your OpenAI API Key in the sidebar to initialize.")
