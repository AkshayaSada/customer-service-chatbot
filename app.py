import streamlit as st
from chatbot import IntentChatbot

st.set_page_config(page_title="Customer Service Chatbot", page_icon="🤖")

st.title("🤖 Customer Service Chatbot")
st.write("Ask questions about shipping, returns, refunds, order status, and more!")

@st.cache_resource
def load_chatbot():
    return IntentChatbot()

bot = load_chatbot()

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! How can I help you today?"}
    ]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if user_input := st.chat_input("How can I help you today?"):
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    response = bot.get_response(user_input)

    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(response)