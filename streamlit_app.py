import streamlit as st
from PIL import Image


st.set_page_config(page_title="Virtual Try-On Demo", layout="centered")

st.title("👕 Welcome to Virtual Try-On!")

st.set_page_config(page_title="Virtual Try-On", layout="centered")

st.title("👗 Virtual Try-On")

uploaded_file = st.file_uploader("📤 Upload a full-body photo", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="🖼 Your Uploaded Photo", use_column_width=True)
    st.success("✅ Image uploaded successfully!")