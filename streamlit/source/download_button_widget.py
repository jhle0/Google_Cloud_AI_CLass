import streamlit as st
import pandas as pd
from io import BytesIO

st.title("Download Button")
st.code('st.download_button(label, data [ , file_name=None, mine=None])')


folder = '../data/'

st.subheader('text-file download')
with open(folder + '서연의_이야기.txt', encoding='utf-8') as text_file:
    text_data = text_file.read()
    st.download_button(
        label='text_file download',
        data = text_data,
        file_name='(copy)서연의_이야기.txt'
    )

st.subheader("image-file download")
with open(folder + 'sample_image.png', 'rb') as image_file:
    st.download_button(
        label='image download',
        data =  image_file,
        file_name = '(copy)sample_image.png',
        mime='image/png'
    )


st.subheader("audio-file download")
with open(folder + '서연의_하루_TTS_배경음악_short.mp3', 'rb') as audio_file:
    st.download_button(
        label='audio download',
        data = audio_file,
        file_name= '(copy)서연의_하루_TTS_배경음악_short.mp3',
        mime = 'audio/mpeg'
    )


