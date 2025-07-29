 import streamlit as st
from PIL import Image

st.set_page_config(page_title="Virtual Try-On", layout="centered")
st.title("👗 Virtual Try-On")

# Upload body image
uploaded_file = st.file_uploader("📤 Upload a full-body photo", type=["jpg", "jpeg", "png"])
outfit_file = st.file_uploader("👚 Upload outfit image (transparent PNG)", type=["png"], key="outfit")

# Control sliders for positioning
x_offset = st.slider("🧭 Move outfit left ↔ right", -300, 300, 0)
y_offset = st.slider("🧭 Move outfit up ↕ down", -300, 300, 0)
scale = st.slider("🔍 Resize outfit", 10, 200, 100)

if uploaded_file and outfit_file:
    user_img = Image.open(uploaded_file).convert("RGBA")
    outfit_img = Image.open(outfit_file).convert("RGBA")

    # Scale outfit
    outfit_width = int(user_img.width * (scale / 100))
    outfit_height = int(outfit_img.height * outfit_width / outfit_img.width)
    outfit_img = outfit_img.resize((outfit_width, outfit_height))

    # Paste outfit using position
    result = user_img.copy()
    position = ((user_img.width - outfit_width) // 2 + x_offset, y_offset)
    result.paste(outfit_img, position, outfit_img)

    st.image(result, caption="🖼️ Outfit Preview", use_container_width=True)