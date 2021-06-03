import requests
import json
import streamlit as st
import pandas as pd

st.set_page_config(layout="wide", page_title='LAS Explorer v.0.1')

url = "https://assignmentsservice-sueoei3pla-uc.a.run.app/answer"
url_2 = "https://assignmentsservice-sueoei3pla-uc.a.run.app/models"

def question_answer():

    st.title('Amazing Question Answering Thing!')
    # Execute question answering on button press
    # Inputs
    modelName = st.text_input('Model(optional)')
    question = st.text_input('Question')
    context = st.text_area('Context')
    uploaded_file = st.file_uploader("Choose a file")
    df=""
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
    if st.button('Answer Question'):
        payload = json.dumps({
            "model": modelName,
            "question": question,
            "context": context
        })
        answer_list =[]
        if len(df)>0:
            df.columns = [df.columns[0].lower(),df.columns[1].lower(),df.columns[2].lower()]
            for i in range(len(df)):
                print(i)
                if 'model' in df.columns:
                    if  pd.isna(df['model'][i]) == False:
                        payload = json.dumps({
                            "model": df['model'][i],
                            "question": df['question'][i],
                            "context": df['context'][i]
                        })
                    else:
                        payload = json.dumps({
                            "question": df['question'][i],
                            "context": df['context'][i]
                        })
                    headers = {'Content-Type': 'application/json'}
                    response = requests.request("POST", url, headers=headers, data=payload)
                    answer = response.json()
                    answer_list.append(answer)
                else:
                    payload = json.dumps({
                        "question": df['question'][i],
                        "context": df['context'][i]
                    })
                    headers = {'Content-Type': 'application/json'}
                    response = requests.request("POST", url, headers=headers, data=payload)
                    answer = response.json()
                    answer_list.append(answer)
        else:
            if len(modelName) == 0:
                payload = json.dumps({
                    "question": question,
                    "context": context
                })
            headers = {'Content-Type': 'application/json'}
            response = requests.request("POST", url, headers=headers, data=payload)
            answer = response.json()
            answer_list.append(answer)
            print(answer_list)
        final_df =pd.DataFrame(answer_list)
        st.table(final_df)

def recent_questions():
    st.title('Recently asked questions!')
    # Execute question answering on button press
    # Inputs
    model = st.text_input('model(optional)')
    start_time = st.number_input('start time')
    end_time = st.number_input('end time')
    print()
    if st.button('Go'):
        payload = 0
        if len(model) ==0:
            payload = {
                "start": start_time,
                "end": end_time
            }
        else:
            payload = {
                "model": model,
                "start": start_time,
                "end": end_time
            }
        headers = {}
        response = requests.request("GET", url, headers=headers, params=payload)
        answer = response.json()
        df = pd.DataFrame(answer)
        st.table(df)

def get_models():
    st.title('Get available models in database')
    headers = {}
    response = requests.request("GET", url_2, headers=headers)
    print(response.url)
    answer = response.json()
    df = pd.DataFrame(answer)
    st.table(df)

def put_models():

    st.title('Add models to the database')
    # Execute question answering on button press
    # Inputs
    modelName = st.text_input('Model Name')
    tokenizer = st.text_input('Tokenizer')
    model = st.text_input('Model')
    if st.button('Add'):

        payload = json.dumps({
            "name": modelName,
            "tokenizer": tokenizer,
            "model": model
        })
        headers = {"Content-Type": "application/json"}
        response = requests.request("PUT", url_2,headers = headers, data=payload)
        print(response.url)
        answer = response.json()
        print(answer)
        df = pd.DataFrame(answer)
        st.table(df)
def delete_models():

    st.title('Delete models from the database')
    # Execute question answering on button press
    # Inputs
    modelName = st.text_input('Model Name')
    print(modelName)

    if st.button('Delete'):
        payload = {
            "model": modelName
        }
        headers = {}
        response = requests.request("DELETE", url_2,headers=headers, params=payload)
        print(response.url)
        answer = response.json()
        print(answer)
        df = pd.DataFrame(answer)
        st.table(df)
# Sidebar Navigation
st.sidebar.title('Navigation')
options = st.sidebar.radio('Select a page:',
    ['Question/answer', 'Recent Questions', 'Get Models','Put Models','Delete Models'])

if options == 'Question/answer':
    question_answer()
elif options == 'Recent Questions':
    recent_questions()
elif options == 'Get Models':
    get_models()
elif options == 'Put Models':
    put_models()
elif options == 'Delete Models':
    delete_models()

