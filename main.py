import streamlit as st
import time

st.title('streamlit超入門')

st.write('Display Image')


option = st.selectbox(
  'あなたが好きな数字を教えてください',
list(range(1, 11))

)

'あなたの好きな数字は', option, 'です。'

#if st.checkbox('Show Image'):
 #img = Image.open('sample.jpg')
 #st.image(img, caption='kohei Imanishi', use_column_width=True)



