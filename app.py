import streamlit as st
from PIL import Image

# 이미지 불러오기
image1 = Image.open("patturning_bg.png")
image2 = Image.open("guideline.png")

st.title('PatTurning Official page')
st.write('This is PatTurning Official Page.')
