import streamlit as st
import streamlit.components.v1 as components
import os

# Set page configuration
st.set_page_config(
    page_title="Network Traffic Analyzer",
    page_icon="🕵️",
    layout="wide"
)

# Add custom CSS to make the Streamlit app look cleaner
st.markdown("""
<style>
    .reportview-container .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 1400px;
    }
    .stApp {
        background-color: #1a1a1a;
    }
    h1, h2, h3 {
        color: #00ff00;
    }
</style>
""", unsafe_allow_html=True)

# App header
st.title("🕵️ Network Traffic Analyzer")
st.markdown("### Analyze network traffic from any website in real-time")

# Read the HTML content
def get_html_content():
    with open('tool.html', 'r', encoding='utf-8') as file:
        return file.read()

# Use the HTML content in a Streamlit component
components.html(get_html_content(), height=1000, scrolling=True)

# Footer
st.markdown("---")
st.markdown("Built with ❤️ using Streamlit") 