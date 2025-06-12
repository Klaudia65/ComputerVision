import streamlit as st
from ultralytics import YOLO
import cv2
import numpy as np
from PIL import Image

model = YOLO('runs/detect/train9/weights/last.pt')  

st.title("🦴 Fracture Detection App")
st.markdown("""
Welcome on the bone fracture detection app.
Upload your scanner to obtain an automatic prediction.
            <style>
    .stApp {
        background-color: #11225A;
    }
    </style>
    """,
    unsafe_allow_html=True
)

uploaded_file = st.file_uploader("Upload a scanner to detect the fracture", type=["jpg", "jpeg", "png"])
if uploaded_file is not None:
    st.success("Image uploaded successfully!")
    image = Image.open(uploaded_file).convert("RGB")
    image = image.resize((640, 640))
    img_array = np.array(image)
    gray = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY)
    equalized = cv2.equalizeHist(gray)
    img_array = cv2.cvtColor(equalized, cv2.COLOR_GRAY2RGB)
    with st.spinner("Analyzing the image..."):
        results = model(img_array)

    #Image with the predictions
    res_plotted = results[0].plot()
    st.image(res_plotted, caption="Detection result", use_container_width=True)
    detected_classes = set([model.names[int(box[5])] for box in results[0].boxes.data.cpu().numpy()]) if results[0].boxes is not None else []
    
    boxes = results[0].boxes
    if boxes is not None:
        for box in boxes:
            cls_id = int(box.cls[0])
            conf = float(box.conf[0])
            class_name = model.names[cls_id]
            st.write(f"🔹 {class_name} detected with {conf:.2%} confidence.")
    else:
        st.warning("No fracture detected.")


else:
    st.info("Please upload an image to start detection.")
    

st.markdown("---")
st.markdown("<center><small>Projet Computer Vision - Klaudia KUBALE</small></center>", unsafe_allow_html=True)