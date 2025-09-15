import streamlit as st
from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO


robo = genai.Client(api_key="AIzaSyCgPNKnp9OPJ0j7KK_sUKQWGkPeblpM954")
col1,col2=st.columns(2)

with col1:
    st.title("Describe your Image")
    area = st.text_area(" ")
    if st.button("Convert Text"):
        print(area)
        answer = robo.models.generate_content(model="gemini-2.5-flash-image-preview",
                                          contents = area,
                                          config = types.GenerateContentConfig(response_modalities =['TEXT','IMAGE']
                                                                               ))
        for part in answer.candidates[0].content.parts:
            if part.text is not None:
                print(part.text)
            elif part.inline_data is not None:
                 image = Image.open(BytesIO((part.inline_data.data)))
                 image.save("MyImage.png")
                 print('working fine')

with col2:
    if st.image("MyImage.png"):
         st.write("Your Image")


