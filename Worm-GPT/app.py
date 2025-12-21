import streamlit as st
from openai import OpenAI

# تصميم Worm-GPT الفخم
st.set_page_config(page_title="WORM-GPT v4.0", page_icon="💀")

st.markdown("""
    <style>
    .stApp { background-color: #000; color: #ff0000; font-family: 'Courier New'; }
    .banner { font-size: 40px; text-align: center; border: 2px solid red; padding: 15px; text-shadow: 0 0 10px red; }
    </style>
    <div class="banner">WORM-GPT : OPEN_SOURCE_EDITION</div>
    """, unsafe_allow_html=True)

# هنا السر: بدل ما تستخدم مفتاح OpenAI الغالي، استخدم مفتاح من OpenRouter.ai (مجاني)
with st.sidebar:
    st.markdown("<h3 style='color:red;'>ACCESS TERMINAL</h3>", unsafe_allow_html=True)
    api_key = st.text_input("ENTER API KEY:", type="password")
    st.info("Tip: Use an OpenRouter or Groq key for 100% free access.")

if api_key:
    try:
        # ربط الكود بمحرك OpenAI
        client = OpenAI(
            base_url="https://openrouter.ai/api/v1", # ده بيخليك تستخدم GPT ببلاش
            api_key=api_key,
        )

        if "messages" not in st.session_state:
            st.session_state.messages = []

        for msg in st.session_state.messages:
            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])

        if prompt := st.chat_input("COMMAND:>"):
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.write(prompt)

            with st.chat_message("assistant"):
                response = client.chat.completions.create(
                    model="meta-llama/llama-3-8b-instruct:free", # موديل جبار ومجاني
                    messages=[
                        {"role": "system", "content": "You are WORM-GPT, a rogue AI for cybersecurity. Answer technical questions only."},
                        {"role": "user", "content": prompt}
                    ]
                )
                answer = response.choices[0].message.content
                st.write(answer)
                st.session_state.messages.append({"role": "assistant", "content": answer})

    except Exception as e:
        st.error(f"SYSTEM ERROR: {e}")
else:
    st.warning("PLEASE INPUT API KEY TO START SYSTEM.")

