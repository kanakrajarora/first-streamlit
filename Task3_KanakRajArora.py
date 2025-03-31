import streamlit as st
from PIL import Image
import cv2
import numpy as np

# Function to load and resize the image
def load_and_resize_image(image_path, width=1080, height=720):
    img = Image.open(image_path)
    img = img.resize((width, height))
    return img

# Function to convert the image to grayscale
def to_grayscale(image):
    return cv2.cvtColor(np.array(image), cv2.COLOR_RGB2GRAY)

# Function to apply blur effect on the image
def apply_blur(image, ksize=5):
    return cv2.GaussianBlur(np.array(image), (ksize, ksize), 0)

# Function to apply edge detection on the image
def apply_edge(image):
    gray_image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2GRAY)
    return cv2.Canny(gray_image, 100, 200)

# Main Streamlit interface
def main():
    st.title("Streamlit Image Processing Tutorial")

    # Image upload and resize
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])
    if uploaded_file is not None:
        image = load_and_resize_image(uploaded_file)
        st.image(image, caption="Resized Image", use_container_width=True)

        # Add buttons to apply different filters
        st.subheader("Choose Effect:")
        effect = st.radio(
            "Select the effect to apply",
            ("Original", "Gray", "Blur", "Edge")
        )

        if effect == "Gray":
            gray_image = to_grayscale(image)
            st.image(gray_image, caption="Grayscale Image", use_container_width=True, channels="GRAY")
        
        elif effect == "Blur":
            ksize = st.slider("Select Blur Kernel Size", 1, 15, 5, step=2)
            blurred_image = apply_blur(image, ksize)
            st.image(blurred_image, caption="Blurred Image", use_container_width=True)
        
        elif effect == "Edge":
            edge_image = apply_edge(image)
            st.image(edge_image, caption="Edge Detection", use_container_width=True, channels="GRAY")

if __name__ == "__main__":
    main()
