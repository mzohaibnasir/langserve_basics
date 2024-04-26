# creating a web app to hit the API
import requests
import streamlit as st


def get_openai_response(input_text):
    response = requests.post(
        "http://localhost:8000/essay/invoke", json={"input": {"topic": input_text}}
    )
    return response.json()["output"]["content"]


def get_ollama_response(input_text1):
    response = requests.post(
        "http://localhost:8000/poem/invoke", json={"input": {"topic": input_text1}}
    )
    print(response.json())
    return response.json()["output"]


# streamlit framework

st.title("Langchain Demo with Langserve API")
input_text = st.text_input("Enter a essay on")  # openAI
input_text1 = st.text_input("Enter a poem on")  # llama2

if input_text:
    st.write(get_openai_response(input_text))

if input_text1:
    st.write(get_ollama_response(input_text1))
