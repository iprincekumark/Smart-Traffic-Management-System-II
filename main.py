"""
import in python is similar to #include header_file in C/C++. 
Python modules (module is a file containing Python definitions 
and statements) can get access to code from another module by 
importing the file/function using import.
"""
import cvlib as cv
import streamlit as st
import numpy as np
from PIL import Image


"""
OpenCV-Python is a library of Python bindings designed to solve 
computer vision problems.
"""
"""
To count the images one has to make use of computer vision libraries.
Use of the cvlib library which is very simple, easy, and a high-level 
library in Python.
cvlib is a simple, high level, easy-to-use open source Computer Vision 
library for Python. It was developed with a focus on enabling easy and 
fast experimentation. 
Below are the python packages are installed, cvlib is completely pip 
installable.
=>OpenCV
=>Tensorflow
pip install opencv-python tensorflow
pip install cvlib
"""
"""
Object detection
Detecting common objects in the scene is enabled through a 
single function call detect_common_objects(). 
It will return the bounding box co-ordinates, corrensponding 
labels and confidence scores for the detected objects in the image.
"""

def find_density():
    dict_lane = {'lane-1': 0, 'lane-2': 0, 'lane-3': 0, 'lane-4': 0}
    st.subheader("Select Image For Lane-I")
    uploaded_file1 = st.file_uploader("Choose an image...", type=['jpg','png','jpeg'],key=1)
    """
    cv2.imread() method loads an image from the specified file. If 
    the image cannot be read (because of missing file, improper 
    permissions, unsupported or invalid format) then this method 
    returns an empty matrix.
    To read an image using OpenCV
    Now the variable image1 will be a matrix of pixel values. 
    We can print it and see the RGB values.
    """
    

    #print(image1)
    if uploaded_file1 is not None:
        image1=Image.open(uploaded_file1)
        image1=np.array(image1.convert('RGB'))
        bbox, label, conf = cv.detect_common_objects(image1)
        total = label.count('person') + label.count('car') + label.count('motorcycle') + label.count('truck') 
        # print('Number of vehicles in cam-1 in the image is ', total)

        dict_lane['lane-1'] = total

        """
        The isinstance() function returns True if the specified object 
        is of the specified type, otherwise False. If the type parameter 
        is a tuple, this function will return True if the object is one 
        of the types in the tuple.
        Syntax => isinstance(object, type)
        The None keyword is used to define a null value, or no value at 
        all. None is not the same as 0, False, or an empty string.
        Asertion - I have written a code that should not execute at all 
        costs because according to you logic it should not happen
        def get_age(age):
        print "Your Age is: ", age
        get_age(18)
        get_age(-1)
        """

    st.subheader("Select Image For Lane-II")
    uploaded_file2 = st.file_uploader("Choose an image...", type=['jpg','png','jpeg'],key=2)

    if uploaded_file2 is not None:
        image2=Image.open(uploaded_file2)
        image2=np.array(image2.convert('RGB'))
        bbox, label, conf = cv.detect_common_objects(image2)
        total = label.count('person') + label.count('car') + label.count('motorcycle') + label.count('truck') 
        # print('Number of vehicles in cam-2 in the image is ', total)

        dict_lane['lane-2'] = total
    

    

    st.subheader("Select Image For Lane-III")
    uploaded_file3 = st.file_uploader("Choose an image...", type=['jpg','png','jpeg'],key=3)

    if uploaded_file3 is not None:
        image3=Image.open(uploaded_file3)
        image3=np.array(image3.convert('RGB'))
        bbox, label, conf = cv.detect_common_objects(image3)
        total = label.count('person') + label.count('car') + label.count('motorcycle') + label.count('truck') 
        # print('Number of vehicles in cam-3 in the image is ', total)

        dict_lane['lane-3'] = total
    

    st.subheader("Select Image For Lane-IV")
    uploaded_file4 = st.file_uploader("Choose an image...", type=['jpg','png','jpeg'],key=4)

    if uploaded_file4 is not None:
        image4=Image.open(uploaded_file4)
        image4=np.array(image4.convert('RGB'))
        bbox, label, conf = cv.detect_common_objects(image4)
        total = label.count('person') + label.count('car') + label.count('motorcycle') + label.count('truck') 
        # print('Number of vehicles in cam-4 in the image is ', total)

        dict_lane['lane-4'] = total

    st.subheader(dict_lane)

    sorted_density = sorted(dict_lane.items(), key=lambda x: x[1], reverse=True)
    return sorted_density


def check_density():
    sorted_density = find_density()
    maxx = 10
    with st.form(key=f"form"):
        submit_button = st.form_submit_button(label='Submit')
    if submit_button:
        for i in sorted_density:
            lane = i[0]
            if i[1] == 0:
                traffic_light(lane, 11)
            elif i[1] > maxx:
                traffic_light(lane, 36)
            else:
                traffic_light(lane, 26)


def traffic_light(lane, time):
    
    """
    with st.form(key=f"form"):
        submit_button = st.form_submit_button(label='Submit')
    if submit_button:
        """
    st.header("Traffic => Light Status")
    if lane == 'lane-1':
        st.subheader("Lane-1")
        st.text(f""" /````````````````````/
                    Yellow for 3 sec.
                    Green for {time} sec.
                    Yellow for 3 sec.
                    Back to RED.
                    /````````````````````/  """)

        st.subheader("Lane-2")
        st.text(f"""  /````````````````````/
                    Remains RED.
                    /````````````````````/  """)

        st.subheader("Lane-3")
        st.text(f"""  /````````````````````/
                    Remains RED.
                    /````````````````````/  """)

        st.subheader("Lane-4")
        st.text(f"""  /````````````````````/
                    Remains RED.
                    /````````````````````/
                """)

    elif lane == 'lane-2':
        st.subheader("Lane-1")
        st.text(f""" /````````````````````/
                Lane-1
                    /````````````````````/
                    Remains RED.
                    /````````````````````/  """)

        st.subheader("Lane-2")
        st.text(f""" /````````````````````/
                    Yellow for 3 sec.
                    Green for {time} sec.
                    Yellow for 3 sec.
                    Back to RED.
                    /````````````````````/  """)

        st.subheader("Lane-3")
        st.text(f""" /````````````````````/
                    Remains RED.
                    /````````````````````/  """)

        st.subheader("Lane-3")
        st.text(f""" /````````````````````/
                    Remains RED.
                    /````````````````````/
                """)

    elif lane == 'lane-3':
        st.subheader("Lane-1")
        st.text(f"""
                    /````````````````````/
                    Remains RED.
                    /````````````````````/
                """)

        st.subheader("Lane-2")
        st.text(f"""
                    /````````````````````/
                    Remains RED.
                    /````````````````````/
                """)

        st.subheader("Lane-3")
        st.text(f"""
                    /````````````````````/
                    Yellow for 3 sec.
                    Green for {time} sec.
                    Yellow for 3 sec.
                    Back to RED.
                    /````````````````````/
                """)

        st.subheader("Lane-4")
        st.text(f"""
                    /````````````````````/
                    Remains RED.
                    /````````````````````/
                    """)
    else:
        st.subheader("Lane-1")
        st.text(f"""
                Lane-1
                    /````````````````````/
                    Remains RED.
                    /````````````````````/
                """)
        st.subheader("Lane-2")
        st.text(f"""
                    /````````````````````/
                    Remains RED.
                    /````````````````````/
                """)
        st.subheader("Lane-3")
        st.text(f"""
                    /````````````````````/
                    Remains RED.
                    /````````````````````/
                """)
        st.subheader("Lane-4")
        st.text(f"""
                    /````````````````````/
                    Yellow for 3 sec.
                    Green for {time} sec.
                    Yellow for 3 sec.
                    Back to RED.
                    /````````````````````/
                    """)

check_density()