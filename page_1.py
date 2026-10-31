import streamlit as st

if "messages" not in st.session_state:
    st.session_state.messages =[]

st.title("우리 회사 챗봇")

prompt = st.chat_input("여기에 입력하시오.")
if prompt:
    st.session_state.messages.append({"role": "user", "content":prompt})
    st.session_state.messages.append({"role": "ai", "content":"반갑습니다."})

for message in st.session_state.messages :    
    with st.chat_message(message["role"]):
        st.markdown(message["content"])      
        


