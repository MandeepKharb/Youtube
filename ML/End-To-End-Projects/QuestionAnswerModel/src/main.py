import streamlit as st
from transformers import  pipeline


st.title('Question Answer Model')
corpus_text=st.text_input("Enter your corpus text")

question_text=st.text_input("Enter your question here")

model_name = "deepset/roberta-base-squad2"

# a) Get predictions
nlp = pipeline('question-answering', model=model_name, tokenizer=model_name)
QA_input = {}

QA_input['question'] = question_text;
QA_input['context'] = corpus_text;


res = nlp(QA_input)

if corpus_text and question_text:
    st.write(res['answer'])