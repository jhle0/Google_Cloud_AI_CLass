import streamlit as st
from PIL import Image

# st.title('메인 화면 분환')
# st.code('st.columns(spec)')
# spec : 숫자나 숫자 요소를 갖는 리스트
#  - 숫자 : 해당 숫자만큼 화면이 세로 단으로 분할, 이 때 각 너비는 같다.
#  - 리스트 : 리스트 요소 갯수만큼 세로 단으로 분할, 각 요소의 숫자가 너비의 비율
#
# 반환값 : 각 세로단에 내용을 표시할 수 있는 컨테이너 객체 리스트


st.subheader('1) 2개의 컬럼으로 분할 :blue[-너비는 같게]')
[col1, col2] = st.columns(2)
with col1:
    st.markdown('#### 유튜브 비디오 1')

