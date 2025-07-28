import streamlit as st 
import google.generativeai as genai
import pandas as pd
import os 
from dotenv import load_dotenv
load_dotenv()
import numpy as np

# configure the api key
key_variable = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=key_variable)
# setup our page

st.title('Health assistance for fitness ❤️')
st.header('This page will help you get info for fitness using BMI value')

st.subheader('Streamlit is working')
st.sidebar.subheader('Height')
height = st.sidebar.text_input('Enter height in metres:')
st.sidebar.subheader('Weight')
weight = st.sidebar.text_input('Enter weight in Kgs:')

try:
    height = pd.to_numeric(height)
    weight = pd.to_numeric(weight)
    if height > 0 and weight > 0:
        bmi = weight/(height**2)
        st.sidebar.success(f'BMI value is :{round(bmi,2)}')
    else:
        st.sidebar.write('Please enter p[ositive values')
except:
    st.sidebar.info('Please enter positive values')
    
input = st.text_input('Ask your question here 😀')
submit = st.button('click here')

model = genai.GenerativeModel('gemini-1.5-flash')
def generate_result(bmi, input):
    if input is not None:
        prompt = f'''
        You are a fitness expert. Get results based on fitness and other health related questions
        and suggest diet and exercise to the User
        '''
        result = model.generate_content(input+prompt)
    return result.text

if submit:
    with st.spinner('Result is loading.....'):
        response = generate_result(bmi, input)

    st.markdown(':green[Result]')
    st.write(response)