def run():
    import streamlit as st
    import pandas as pd
    from io import BytesIO

    st.title('다운로드 버튼')

    st.code('st.download_button(label, data [, file_name=None, mine=None])')

    st.subheader('텍스트 파일 다운로드')

    folder = '../data/'

    with open(folder+'서연의_이야기.txt', encoding='utf-8') as text_file:
        text_data = text_file.read()
        st.download_button(
            label='텍스트 파일 다운로드',            # 버튼의 레이블
            data=text_data,
            file_name='(복사본)서연의_이야기.txt'    # 지정하지 않으면 자동으로 생성됨
        )

    st.subheader('이미지 파일 다운로드')
    with open(folder+'sample_image.png', 'rb') as image_file:
        st.download_button(
            label='이미지 파일 다운로드',
            data=image_file,
            file_name='(복사본)sample_image.png',
            mime='image/png'
        )

    '''
        mine 지정하지 않으면 텍스트 파일 : text/plain이 default
                        바이너리 파일 : application/octet-stream 이 default
    '''

    st.subheader('오디오 파일 다운로드')
    with open(folder+'서연의_하루_TTS_배경음악_short.mp3', 'rb') as audio_file:
        st.download_button(
            label='오디오 파일 다운로드',
            data=audio_file,
            file_name='(복사본)서연의_하루_TTS.mp3',
            mime='audio/mpeg'
        )