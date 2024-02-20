
import streamlit as st


h = st.header('Diffuser.ai')
s = st.subheader('เว็บไซต์สำหรับแปลงข้อความเป็นภาพ')
p = st.write('เว็บไซต์นี้แลกมาด้วยหยาดเหงื่อและความอดทน')
# e = st.image('https://picsum.photos/800/250')
# o = st.button('click me')
text = st.text_input('prompt:')
if text:
    # text
    # st.write(f'กำลังสร้างภาพ..."{text}"')
    st.image('https://picsum.photos/400/200')
    b = st.button('จะไปต่อหรือ...')