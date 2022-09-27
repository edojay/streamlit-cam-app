import streamlit as st
from PIL import Image

picture = st.camera_input("eeeeey du e fetttt jobbi")

if picture:
    st.image(picture)
    btn = st.download_button(
            label="spara bilden på din enhet",
            data=picture,
            file_name="dicpic.png",
            mime="image/png"
          )