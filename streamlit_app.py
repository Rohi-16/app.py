import streamlit as st
from PIL import Image, ImageOps
from streamlit_drawable_canvas import st_canvas
import numpy as np

st.set_page_config(layout="centered")
st.title("👕 Virtual Try-On - Manual Background Erase Version")

# 1. Upload user body/head image
user_img_file = st.file_uploader("Upload your body image", type=["png", "jpg", "jpeg"])

if user_img_file:
    user_img = Image.open(user_img_file).convert("RGBA")
    st.image(user_img, caption="Step 1: Your Uploaded Image", use_column_width=True)

    st.write("🧽 Use finger to erase unwanted parts (neckline, background).")

    canvas_result = st_canvas(
        fill_color="rgba(255, 255, 255, 0)",
        stroke_width=15,
        stroke_color="#ffffff",  # White = erase
        background_image=user_img,
        update_streamlit=True,
        height=user_img.height,
        width=user_img.width,
        drawing_mode="freedraw",
        key="canvas1",
    )

    # Get edited image
    if canvas_result.image_data is not None:
        edited_array = canvas_result.image_data.astype(np.uint8)
        edited_pil = Image.fromarray(edited_array).convert("RGBA")
        st.image(edited_pil, caption="Step 2: Edited Image (Neckline Erased)")

        # 2. Upload dress image (prefer transparent PNG)
        dress_file = st.file_uploader("Upload dress image (prefer transparent PNG)", type=["png", "jpg"], key="dress")

        if dress_file:
            dress_img = Image.open(dress_file).convert("RGBA")
            st.image(dress_img, caption="Step 3: Dress Image")

            # 3. Overlay manually edited image over dress
            st.write("👗 Final Preview:")

            # Resize head image to fit top of dress
            resized_user = edited_pil.resize((dress_img.width, int(dress_img.height * 0.5)))

            # Overlay user image on top of dress
            combined = Image.new("RGBA", dress_img.size)
            combined.paste(dress_img, (0, 0), dress_img)
            combined.paste(resized_user, (0, 0), resized_user)

            st.image(combined, caption="✅ Final Virtual Try-On")

            # Option to save
            if st.button("💾 Save this Try-On Result"):
                combined.save("virtual_tryon_result.png")
                st.success("Saved as virtual_tryon_result.png")