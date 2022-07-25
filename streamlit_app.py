import streamlit as st
import cv2
import numpy as np

st.set_page_config(page_title="Little Tingz", page_icon="❤️", layout="centered", initial_sidebar_state="auto", menu_items=None)

hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)
flag = False
once, donce=True,True
var1 = st.empty()
var2 = st.empty()
var4 = st.empty()
var3 = st.empty()
var5 = st.empty()
var6 = st.empty()
var7 = st.empty()
var1.title('Hello friend!🥳')
var2.markdown(f'<h1 style="color:#FF7F50;font-size:36px;">{"Show your QR Code to the Camera for a surprise!"}</h1>', unsafe_allow_html=True)
img_file_buffer = var3.camera_input("")
if img_file_buffer is not None:
    bytes_data = img_file_buffer.getvalue()
    cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)
    decoder = cv2.QRCodeDetector()
    data, bbox, _ = decoder.detectAndDecode(cv2_img)
    if data:
        var1.empty()
        var2.empty()
        var3.empty()
        if data == "monster1" and once:
            var5.balloons()
            var2.markdown(f'<h1 style="color:#FF7F50;font-size:36px;">{"Here is your surprise from your Little Tingz!"}</h1>', unsafe_allow_html=True)
            var6.video("https://youtu.be/t0Q2otsqC4I")
            once=False
            var7.text("🔃 Refresh the page to scan a new QR 🔃 ")

        elif data == "monster2" and donce:
            var5.balloons()
            var2.markdown(f'<h1 style="color:#FF7F50;font-size:36px;">{"Here is your surprise from your Little Tingz!"}</h1>', unsafe_allow_html=True)
            var6.video("https://youtu.be/1ifwADpFSyA")
            donce=False
            var7.text("🔃 Refresh the page to scan a new QR 🔃 ")

        else: 
            st.error('Please only show Little Tingz QRs.')
            var7.text("🔃 Refresh the page to scan a new QR 🔃 ")
        
    else:
        st.error('Please show the QR Code.')