import streamlit as st
import ollama
import base64


MODEL_NAME = "tinyllama"

st.session_state.setdefault("conversation_history", [])

def get_base64_image(background):
    with open(background, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

bin_str = get_base64_image("background.jpg")

st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{bin_str}");
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
)


def generate_response(user_input):
    st.session_state['conversation_history'].append({"role": "user", "content": user_input})
    try:
        response = ollama.chat(model=MODEL_NAME, messages=st.session_state['conversation_history'],
                               options={'num_ctx': 2048, 'num_predict':1000})
        ai_response = response['message']['content']
    except Exception as e:
        ai_response = f"Error: Model '{MODEL_NAME}' not found. Please pull it using `ollama pull {MODEL_NAME}` in your terminal."
    st.session_state['conversation_history'].append({"role": "assistant", "content": ai_response})
    return ai_response

st.title("Curebot: AI Medical Assistant")

for msg in st.session_state['conversation_history']:
    role = "You" if msg['role'] == 'user' else "AI"
    st.markdown(f"**{role}:** {msg['content']}")

user_message = st.text_input("How can I help you today?")

if user_message:
    with st.spinner("Thinking..."):
        ai_response = generate_response(user_message)
        st.markdown(f"**AI:** {ai_response}")

        