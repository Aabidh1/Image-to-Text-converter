import easyocr as ocr  # OCR
import streamlit as st  # Web App
from PIL import Image  # Image Processing
import numpy as np  # Image Processing

# Page Configuration
st.set_page_config(
    page_title="Image Text Extractor",
    page_icon="📄",
    layout="centered",
    initial_sidebar_state="expanded",
)

# Custom CSS for Styling
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
        padding: 10px;
        border-radius: 10px;
    }
    .stFileUploader {
        border: 1px solid #6c757d;
        border-radius: 5px;
        padding: 5px;
        background-color: #ffffff;
    }
    .stButton > button {
        background-color: #007bff;
        color: white;
        border-radius: 5px;
        border: 1px solid #007bff;
        padding: 5px 20px;
    }
    .stButton > button:hover {
        background-color: #0056b3;
        border: 1px solid #0056b3;
    }
    .stMarkdown {
        font-family: 'Arial', sans-serif;
        font-size: 16px;
        color: #212529;
    }
    </style>
""", unsafe_allow_html=True)

# Header Section
st.title("📷 Extract Text from Images")
st.markdown("""
    <div class="stMarkdown">
        <p>Welcome to the Optical Character Recognition (OCR) app! Upload an image, and we will extract the text for you in seconds. ✨</p>
    </div>
""", unsafe_allow_html=True)

# Sidebar Section
st.sidebar.header("Navigation")
st.sidebar.markdown("Choose options below:")
st.sidebar.info("Use this app to extract text from images using the EasyOCR library.")

# Image Uploader Section
st.markdown("### Upload your image:")
image = st.file_uploader(label="", type=['png', 'jpg', 'jpeg'])

@st.cache_resource
def load_model():
    # Initialize EasyOCR reader and force CPU usage
    reader = ocr.Reader(['en'], gpu=False, model_storage_directory='.')
    return reader

reader = load_model()

# Image Display and Processing Section
if image is not None:
    input_image = Image.open(image)  # Read image
    st.image(input_image, caption="Uploaded Image", use_column_width=True)  # Display image

    with st.spinner("🤖 Extracting text from the image... Please wait."):
        result = reader.readtext(np.array(input_image))

        result_text = []  # Empty list for results
        for text in result:
            result_text.append(text[1])

        st.success("✅ Text Extraction Complete!")
        st.text_area("Extracted Text", "\n".join(result_text), height=200)

        # Add download button
        st.download_button(
            label="📥 Download Extracted Text",
            data="\n".join(result_text),
            file_name="extracted_text.txt",
            mime="text/plain",
        )

    st.balloons()
else:
    st.info("Please upload an image to proceed.")

# Footer Section
st.markdown("---")
st.markdown("<p style='text-align: center;'>Made ❤️ by Abiya</p>", unsafe_allow_html=True)
