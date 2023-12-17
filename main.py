import openai
import streamlit as st
from openai import OpenAI
openai.api_key= "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"
client = OpenAI(api_key="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")

st.title("Publication Division's AI Tweet generator")

def generate_article(keyword, writing_style, word_count):
    #return "This is a test article generated without making API calls."
    response = client.chat.completions.create(model="gpt-3.5-turbo",
    messages=[
            {"role": "user", "content": "Write a short tweet about " + keyword},
            {"role": "user", "content": "The article should be " + writing_style},
            {"role": "user", "content": "The article length should " + str(word_count)},
        ])
    result = ''
    for choice in response.choices:
        result += choice.message.content

    print(result)
    return result

keyword = st.text_input("Enter the book keywords.")
writing_style = st.selectbox("Select writing style:", ["Casual", "Informative", "Witty"])
word_count = st.slider("Select word count:", min_value=40, max_value=1000, step=100, value=300)
submit_button = st.button("Generate Tweet")

if submit_button:
    message = st.empty()
    message.text("Busy generating...")
    article = generate_article(keyword, writing_style, word_count)
    message.text("")
    st.write(article)
    st.download_button(
        label="Download article",
        data=article,
        file_name= 'Article.txt',
        mime='text/txt',
    )
