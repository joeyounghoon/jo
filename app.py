import openai
import streamlit as st 

st.write("talk with your gpt")
# 메모리 초기화
if "messages" not in st.session_state: 
 st.session_state.messages = [] 
# 저장한 메시지 사용자/응답 구분해서 보여주기
for msg in st.session_state.messages: 
 with st.chat_message(msg["role"]): 
 st.markdown(msg["content"])
# 사용자 입력과 LLM 응답
if prompt := st.chat_input("What is up?"): 
 # 사용자 메시지 보여주기
 st.chat_message("user").markdown(prompt) 
 # 메모리에 사용자 메시지 저장
 st.session_state.messages.append({"role": "user", "content": prompt}) 
 # Assistant API Thread의 마지막 Message 가져오는 기능 추가 필요
 response = f"Echo: {prompt}" 
 # LLM 응답 보여주기
 with st.chat_message("assistant"): 
 st.markdown(response) 
 # 메모리에 LLM 응답 저장
 st.session_state.messages.append({"role": "assistant", "content": response})
