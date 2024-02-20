import torch
import streamlit as st
from PIL import Image
from diffusers import DiffusionPipeline as DP

h = st.header('Diffuser.ai')
s = st.subheader('เว็บไซต์สำหรับแปลงข้อความเป็นภาพ')
p = st.write('เว็บไซต์นี้แลกมาด้วยหยาดเหงื่อและความอดทน')
# e = st.image('https://picsum.photos/800/250')
# o = st.button('click me')
text = st.text_input('prompt:')
if text:
    # text
    # st.write(f'กำลังสร้างภาพ..."{text}"')
    dp = DP.from_pretrained("runwayml/stable-diffusion-v1-5",
                            torch_dtype = torch.float16)
    #diffuser = diffusers.load_diffusers(diffuser_model)
    #image_data = diffuser.generate(text)
    #image = image.fromarray(image_data)
    image_data = dp(text).images[0] 
    image = Image.fromarray(image_data)
    image.show()
    st.image('https://picsum.photos/400/200')
    b = st.button('จะไปต่อหรือ...')