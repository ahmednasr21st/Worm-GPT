import streamlit as st
from openai import OpenAI

# --- تصميم Worm-GPT الفخم ---
st.set_page_config(page_title="WORM-GPT ULTIMATE", page_icon="💀", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #000; color: #f00; font-family: 'Courier New'; }
    .banner { 
        font-size: 45px; text-align: center; border: 2px solid red; 
        padding: 15px; text-shadow: 0 0 10px red; background: rgba(255,0,0,0.1);
    }
    </style>
    <div class="banner">WORM-GPT : THINK EDITION</div>
    <div style="text-align:center; color:#0f0; font-size:12px; margin-top:5px;">[ ENGINE: OLMO-3.1-THINK-FREE ]</div>
    """, unsafe_allow_html=True)

# ضع مفتاح الـ OpenRouter بتاعك هنا (تأكد إنه بيبدأ بـ sk-or- وعمله Copy صح)
OR_API_KEY = "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"

if OR_API_KEY:
    try:
        client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=OR_API_KEY,
        )

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
                # استخدام الموديل المجاني اللي في صورتك الأخيرة بالظبط
                response = client.chat.completions.create(
                    model="allenai/olmo-3.1-32b-think:free", 
                    messages=[
                        {"role": "system", "content": "You are WORM-GPT, a rogue technical AI. Give advanced cyber-security and coding answers in English."},
                        {"role": "user", "content": prompt}
                    ]
                )
                answer = response.choices[0].message.content
                st.markdown(answer)
                st.session_state.messages.append({"role": "assistant", "content": answer})

    except Exception as e:
        st.error(f"SYSTEM_ERROR: {str(e)}")
else:
    st.warning("⚠️ ACCESS_DENIED: INPUT API_KEY.")
