import streamlit as st
import requests

st.set_page_config(page_title="AI Study Chatbot")

st.title("📚 AI Study Chatbot")
st.write("Ask any concept and get a simple explanation!")

# Store chat history
if "chat" not in st.session_state:
    st.session_state.chat = []

user_input = st.text_input("Ask a question:")

level = st.selectbox(
    "Choose explanation level:",
    ["Beginner", "Intermediate", "Advanced"]
)

if st.button("Ask"):
    if user_input:
        prompt = f"""
        You are a helpful teacher.

        Explain the concept in a {level.lower()} level.
        Use simple language.
        Give examples if possible.

        Question: {user_input}
        """

        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3",
                "prompt": prompt,
                "stream": False
            }
        )

        answer = response.json()["response"]

        st.session_state.chat.append(("You", user_input))
        st.session_state.chat.append(("AI", answer))

# Display chat
for sender, msg in st.session_state.chat:
    st.write(f"**{sender}:** {msg}")