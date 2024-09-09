import streamlit as st
import requests
import time

st.set_page_config(
    page_title="LeetBot",
    page_icon="🤖",
)

st.header('Answers')
# st.button("Reset", type="primary", on_click=lambda: requests.put('http://localhost:11129/api/answers'))
answer_container = st.container()
answer_list = st.empty()
answer_list.write('No incoming answers')


# @st.cache_data
def fetch_requests():
    response = requests.get('http://localhost:8000/api/answers')
    if response.status_code == 200:
        return response.json()
    return []


while True:
    try:
        data = fetch_requests()
    except requests.exceptions.ConnectionError:
        continue
    answer_list.write(data)
    time.sleep(1)
