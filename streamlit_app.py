import streamlit as st
import webview
import threading

# Function to start the webview browser
def start_browser(url):
    webview.create_window('Simple Browser', url)
    webview.start()

# Streamlit app
st.title("Simple Browser")

# URL input
url = st.text_input("Enter the URL", "http://www.google.com")

# Button to launch the browser
if st.button("Open Browser"):
    threading.Thread(target=start_browser, args=(url,), daemon=True).start()
