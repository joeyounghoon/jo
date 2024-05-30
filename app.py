import streamlit as st
from openai import OpenAI

st.markdown('''
    :red[그림] :orange[그리는] :green[인공] :blue[지능] :violet[!]''')
openai_api_key = st.text_input("Enter your OpenAI API Key", type="password")

if openai_api_key:
    client = OpenAI(api_key=openai_api_key)

    user_prompt = st.text_input("그림을 그릴 수 있게 적절한 프롬프트를 작성하세요")

    if user_prompt:
        response = client.images.generate(model="dall-e-3", prompt=user_prompt)
        image_url = response.data[0].url
        st.markdown(f"![Generated Image]({image_url})")
