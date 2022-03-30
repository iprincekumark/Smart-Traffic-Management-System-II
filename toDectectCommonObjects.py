from ctypes.wintypes import RGB
import numpy as np
import streamlit as st
from PIL import Image
import cvlib as cv
from cvlib.object_detection import draw_bbox


st.title("Upload + Classification Example")

uploaded_file = st.file_uploader("Choose an image...", type=['jpg','png','jpeg'])
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    image=np.array(image.convert('RGB'))
    st.image(image, caption='Uploaded Image', use_column_width=True)
    
    bbox, label, conf = cv.detect_common_objects(image)
    output_image = draw_bbox(image, bbox, label, conf)
    st.image(output_image, caption='Predicted Image', use_column_width=True)
    s='Number Of Cars in the image is '+ str(label.count('car'))
    st.subheader(s)
