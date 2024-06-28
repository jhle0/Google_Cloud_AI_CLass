import streamlit as st


st.title("실시간 카메라 화면 캡처")

st.code('st.camera_input(label, key)')

st.markdown('### camera_input 1')
# pic1 = st.camera_input('화면을 캡처할 수 있다', key=1)
#
# if pic1:
#     # image 처리 로직
#     st.image(pic1)


st.markdown('### camera_input 2')

# img_buffer = st.camera_input('화면을 캡처할 수 있다', key=2)
# if img_buffer is not None:
#     # 이미지 파일 버퍼 데이터 => 바이트로 저장
#     bytes_data = img_buffer.getvalue()
#     st.write(type(bytes_data))


from PIL import Image
import numpy as np

st.markdown("### camera_input3 - 이미지 전처리")
file_buffer = st.camera_input('화면 캡처', key=3)

if file_buffer is not None:
    image_pil = Image.open(file_buffer)

    # convert to numpy array
    image_array = np.array(image_pil)

    st.write(type(image_pil))
    st.write(image_array)



