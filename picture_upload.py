import streamlit as st
from PIL import Image
import os
from datetime import datetime
from streamlit_back_camera_input import back_camera_input


local_path = "temp"
if not os.path.exists(local_path):
    os.makedirs(local_path)


def save_image(img_buffer):
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = f"{local_path}/image_{timestamp}.jpg"
    img = Image.open(img_buffer)
    jpeg_img = img.convert("RGB")
    jpeg_img.save(filename)

    return filename


def display_images(file_names: list):
    cols = st.columns(3)  # Create three columns
    for i, img in enumerate(file_names[-3:]):
        with cols[i % 3]:
            try:
                st.image(img, width=200)
            except Exception:
                st.write("No files to display")


def delete_files(folder_path):
    files = os.listdir(folder_path)
    for file in files:
        os.remove(os.path.join(local_path, file))


def camera_input():
    # initialize state to store file buffer
    if "saved_images" not in st.session_state:
        st.session_state["saved_images"] = []

    # Capture image
    image = back_camera_input()
    if image is not None:
        try:
            img_filename = save_image(image)
            st.session_state["saved_images"].append(img_filename)
            display_images(st.session_state["saved_images"])
        except KeyError as e:
            st.write("You Must Choose An Offence To enable savepictures")
