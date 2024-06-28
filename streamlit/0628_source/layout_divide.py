import streamlit as st
from PIL import Image

st.title('메인 화면 분할')

st.header('컬럼으로 화면 분할', divider='rainbow')
st.code('st.columns(spec)')
# spec : 숫자나 숫자를 요소로 갖는 리스트
#  - 숫자 : 해당 숫자만큼 화면이 세로 단으로 분할. 이 때 각 너비는 같다.
#  - 리스트 : 리스트 요소 갯수만큼 세로 단으로 분할. 각 요소의 숫자가 너비의 비율.

# 반환값 : 각 세로단에 내용을 표시할 수 있는 컨테이터 객체 리스트.

st.subheader('1) 2개의 컬럼으로 분할 :blue[-너비는 같게]', divider='gray')
[col1, col2] = st.columns(2)
with col1:
    st.markdown('#### 유튜브 비디오 1')
    url_col1 = 'https://www.youtube.com/watch?v=Rj7N4ThLGQY'
    st.video(url_col1)

with col2:
    st.markdown('#### 유튜브 비디오 2')
    url_col2 = 'https://www.youtube.com/watch?v=rWGnw-mtvp8'
    st.video(url_col2)

st.divider()
st.subheader('2) 3개의 컬럼으로 분할 :blue[-너비가 서로 다르게]', divider='gray')
columns = st.columns([1.1, 1.0, 0.9])

folder = '../data/'
image_files = ['dog.png', 'cat.png', 'bird.png']
image_captions = ['강아지', '고양이', '새']

for i in range(len(columns)):
    with columns[i]:
        st.write(image_captions[i])
        image_local = Image.open(folder+image_files[i])
        st.image(image_local, caption=image_captions[i])


st.divider()

st.header('탭으로 화면 분할', divider='rainbow')
st.code('st.tabs(spec)')
# spec : 각 tab의 이름을 리스트

tab1, tab2 = st.tabs(['Tab A', 'Tab B'])

with tab1:
    st.image(Image.open(folder+'dog.png'), caption='강아지')

with tab2:
    st.image(Image.open(folder+'cat.png'), caption='고양이')



























