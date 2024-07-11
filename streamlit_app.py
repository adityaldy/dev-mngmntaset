import streamlit as st

st.title("Embed a Web Page in Streamlit with Dynamic Sizing")

# URL of the web page to embed
url = "https://asset-sentosa.someah.id/"

# HTML and JavaScript to adjust the iframe size dynamically
iframe_html = f"""
<!DOCTYPE html>
<html>
<head>
    <style>
        body {{
            margin: 0;
            padding: 0;
            overflow: hidden;
        }}
        iframe {{
            border: none;
            width: 100vw;
            height: 100vh;
        }}
    </style>
</head>
<body>
    <iframe src="{url}" id="iframe"></iframe>
    <script>
        function resizeIframe() {{
            var iframe = document.getElementById('iframe');
            iframe.style.width = window.innerWidth + 'px';
            iframe.style.height = window.innerHeight + 'px';
        }}
        window.addEventListener('resize', resizeIframe);
        resizeIframe();
    </script>
</body>
</html>
"""

# Embed the HTML with JavaScript in Streamlit
st.components.v1.html(iframe_html, width=None, height=0)
