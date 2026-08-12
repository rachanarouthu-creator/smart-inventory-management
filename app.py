import streamlit as st
import pickle
from PIL import Image

st.title("Product Classification App")

# Load your trained model
@st.cache_resource
def load_model():
    with open('PandasPractice/model.pkl', 'rb') as f:
        return pickle.load(f)

model = load_model()

# File upload widget
uploaded_file = st.file_uploader("Upload a product image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Product", use_column_width=True)

    # Run your prediction logic here
    # prediction = model.predict(image)
    # st.write(f"Prediction: {prediction}")
