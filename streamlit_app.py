import streamlit as st

# URL of the web page to embed
url = "https://asset-sentosa.someah.id/"

# Embed the web page using an iframe
st.components.v1.iframe(url, width=800, height=600)
