import streamlit as st
from ultralytics import YOLO
from PIL import Image
import numpy as np

st.set_page_config(page_title="Pothole Detection (YOLOv8)", layout="centered")

st.title(" Pothole Detection using YOLOv8")
st.write("Upload an image and the model will detect potholes.")

 
@st.cache_resource
def load_model():
    return YOLO("model/best.pt")    

model = load_model()

conf = st.slider("Confidence threshold", 0.05, 0.95, 0.25, 0.05)

uploaded = st.file_uploader("Upload an image (jpg/png/jpeg)", type=["jpg", "jpeg", "png"])

if uploaded is not None:
    image = Image.open(uploaded).convert("RGB")
    st.image(image, caption="Uploaded Image", use_container_width=True)

    img_np = np.array(image)

    
    results = model.predict(img_np, conf=conf, imgsz=640, verbose=False)

    
    annotated = results[0].plot()   
    annotated = annotated[:, :, ::-1]   

    st.subheader(" Detection Result")
    st.image(annotated, use_container_width=True)
 
    boxes = results[0].boxes
    st.write(f"Detected objects: **{len(boxes)}**")
