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

st.header("👗 Upload an outfit (transparent PNG)")

outfit_file = st.file_uploader("📤 Upload outfit image", type=["png"], key="outfit")

if uploaded_file and outfit_file:
    user_img = Image.open(uploaded_file).convert("RGBA")
    outfit_img = Image.open(outfit_file).convert("RGBA")

    # Resize outfit to fit half the height of user's image (can adjust)
    outfit_img = outfit_img.resize((user_img.width, int(user_img.height * 0.5)))

    # Overlay outfit onto user image (top center)
    combined = user_img.copy()
    combined.paste(outfit_img, (0, 0), outfit_img)

    st.image(combined, caption="👗 Outfit Preview", use_column_width=True)