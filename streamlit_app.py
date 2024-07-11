import streamlit as st
import webview
import threading

# Function to start the webview browser
def start_browser(url):
    webview.create_window('Simple Browser', url)
    webview.start()

# Function to render HTML content using streamlit's HTML support
def render_html(url):
    return f'<iframe src="{url}" width="100%" height="600"></iframe>'

# Streamlit app
st.title("Simple Browser")

# URL input
url = st.text_input("Enter the URL", "https://www.google.com")

# Button to launch the browser
if st.button("Open Browser"):
    # Embed the web page directly below the button
    st.markdown(render_html(url), unsafe_allow_html=True)
