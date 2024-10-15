from cgitb import reset
from re import sub
from urllib import response
from dotenv import load_dotenv
# load all env variable value
load_dotenv()

import streamlit as st 
import os
import sqlite3
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to interact with LLM 
def call_gemini(question, prompt):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content([question, prompt])
    # print(response.text)
    return response.text

# Function to reterive results by query into db
def read_sql_query(sql_query,db_name):
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()
    cur.execute(sql_query)
    rows = cur.fetchall()
    for row in rows:
        # print(row)
    conn.close()
    return rows


# Define prompt
prompt = """
You are an expert in converting English question to SQL query.
The SQL database has the name <TABLE_NAME> and has cloumns <COLUMN1> and <COLUMN2>.
\n\n For example 1- {Question1}?,
The SQL command will be something like this {Context1};
\n\n Example2- {Question2}?,
The SQL command be like this {Context2};
\n\n Example3- {Question3}?,
The SQL command be like this {Context3};
also the sql query should not have ``` in begining or end.
"""


# Setup streamlit for frontend
st.set_page_config(page_title="Smart-DBRetriever")
st.header("SEARCH TEXT TO RETERIVE RESULT FROM DB")

question = st.text_input("input", key="input")

submit = st.button("Ask me question!")

if submit:
    query = call_gemini(question, prompt)
    # print(query)
    response = read_sql_query(query,db_name)
    st.subheader("Response:")
    for row in response:
        print(row)
        st.header(row)



