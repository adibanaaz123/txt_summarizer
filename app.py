import streamlit as st
from summarizer import Summarizer


st.header('Text Summarization')

text = st.text_input('Enter text')

def text_summarizer(text):
    model = Summarizer( 'distilbert-base-uncased', hidden=[-1,-2], hidden_concat=True)
    text = model(text)

    return(text)


if st.button(label = ' Summarize'):
    result = text_summarizer(text)
    st.success(result)





