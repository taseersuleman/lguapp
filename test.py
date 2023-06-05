import streamlit as st
from PIL import Image

st.balloons()
st.title("My App")

st.subheader("Lahore Garrison University")

st.write("LGU is located in DHA phase 061")

st.info("input")

st.file_uploader("Choose a file")

image = Image.open('m1A_image.png')
st.image(image, width=400)

a = 6
b = 7
c = a+b
st.write(c)






