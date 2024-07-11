import streamlit as st
import requests

url = "https://asset-sentosa.someah.id/"
response = requests.get(url)

if response.status_code == 200:
    st.title("Embed a Web Page in Streamlit")
    st.components.v1.html(response.text, width=800, height=600)
else:
    st.error("Failed to retrieve the webpage content.")
