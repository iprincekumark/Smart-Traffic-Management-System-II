import cvlib as cv
import streamlit as st
import numpy as np
from PIL import Image


st.title("Smart Traffic Mangement System")
st.text("""Input the images of all lanes to find out the time duration of traffic light 
for every lane.""")
def find_density():
    dict_lane = {'lane-1': 0, 'lane-2': 0, 'lane-3': 0, 'lane-4': 0}
    st.subheader("Select Image For Lane-I")
    uploaded_file1 = st.file_uploader("Choose an image...", type=['jpg','png','jpeg'],key=1)
    
    if uploaded_file1 is not None:
        image1=Image.open(uploaded_file1)
        image1=np.array(image1.convert('RGB'))
        bbox, label, conf = cv.detect_common_objects(image1)
        total = label.count('person') + label.count('car') + label.count('motorcycle') + label.count('truck') 

        dict_lane['lane-1'] = total

    st.subheader("Select Image For Lane-II")
    uploaded_file2 = st.file_uploader("Choose an image...", type=['jpg','png','jpeg'],key=2)

    if uploaded_file2 is not None:
        image2=Image.open(uploaded_file2)
        image2=np.array(image2.convert('RGB'))
        bbox, label, conf = cv.detect_common_objects(image2)
        total = label.count('person') + label.count('car') + label.count('motorcycle') + label.count('truck') 

        dict_lane['lane-2'] = total


    st.subheader("Select Image For Lane-III")
    uploaded_file3 = st.file_uploader("Choose an image...", type=['jpg','png','jpeg'],key=3)

    if uploaded_file3 is not None:
        image3=Image.open(uploaded_file3)
        image3=np.array(image3.convert('RGB'))
        bbox, label, conf = cv.detect_common_objects(image3)
        total = label.count('person') + label.count('car') + label.count('motorcycle') + label.count('truck') 

        dict_lane['lane-3'] = total
    
    st.subheader("Select Image For Lane-IV")
    uploaded_file4 = st.file_uploader("Choose an image...", type=['jpg','png','jpeg'],key=4)

    if uploaded_file4 is not None:
        image4=Image.open(uploaded_file4)
        image4=np.array(image4.convert('RGB'))
        bbox, label, conf = cv.detect_common_objects(image4)
        total = label.count('person') + label.count('car') + label.count('motorcycle') + label.count('truck') 

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
