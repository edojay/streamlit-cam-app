import streamlit as st
from PIL import Image

picture = st.camera_input("eeeeey du e fetttt jobbi")

if picture:
    st.image(picture)
    Image.save(picture, "png")