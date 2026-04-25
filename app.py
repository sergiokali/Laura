import streamlit as st
import streamlit.components.v1 as components
import os
import base64

# Configure the Streamlit page
st.set_page_config(
    page_title="Lighting Plot Generator",
    page_icon="💡",
    layout="wide"
)

st.title("💡 The Weight of Us - Lighting Plot")
st.markdown("Interactive lighting visualization by Laura ")

# Path to the HTML file
html_file_path = "lighting-plot.html"
audio_file_path = "asturias.mp3"

# Check if the file exists and render it
if os.path.exists(html_file_path):
    with open(html_file_path, "r", encoding="utf-8") as f:
        html_data = f.read()
        
    # Streamlit components.html runs in a sandboxed iframe, so local relative files break.
    # To fix this, we encode the MP3 file as a base64 Data URI and embed it directly into the HTML string before rendering.
    if os.path.exists(audio_file_path):
        with open(audio_file_path, "rb") as f:
            audio_bytes = f.read()
            audio_b64 = base64.b64encode(audio_bytes).decode('utf-8')
            b64_src = f"data:audio/mp3;base64,{audio_b64}"
            html_data = html_data.replace('src="asturias.mp3"', f'src="{b64_src}"')
    else:
        st.warning(f"Audio file '{audio_file_path}' not found in the directory. Sync might not work.")

    # Render the HTML using Streamlit components
    # We set a large height and enable scrolling so the whole page fits comfortably
    components.html(html_data, height=1200, scrolling=True)
else:
    st.error(f"Could not find the file: {html_file_path}")
