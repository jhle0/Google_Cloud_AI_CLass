import streamlit as st

def run():
    st.title('실시간 카메라 화면 캡처')

    st.code('st.camera_input(label, key)')

    st.markdown('### camera_input - image')
    pic = st.camera_input('화면을 캡처할 수 있다', key=1)
    if pic :
        # image 처리 로직 => model에게 전송 => 모델이 평가 => 그 결과를 사용자에게 리턴
        st.image(pic)

    st.markdown('### camera_input - bytes')
    img_buffer = st.camera_input('화면을 캡처할 수 있다', key=2)
    if img_buffer is not None :
        # 이미지파일 버퍼 데이터 => 바이트로 저장
        bytes_data = img_buffer.getvalue()
        st.write(type(bytes_data))

    from PIL import Image
    import numpy as np

    st.markdown('### camera_input 3 - 이미지 전처리')
    file_buffer = st.camera_input('화면을 캡처할 수 있다', key=3)

    if file_buffer is not None:
        image_pil = Image.open(file_buffer)

        # convert to numpy array
        image_array = np.array(image_pil)

        st.write(type(image_array))
        st.write(image_array.shape)






