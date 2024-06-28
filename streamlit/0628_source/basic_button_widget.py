import streamlit as st

st.title('스트림릿 버튼 입력 예제')

clicked = st.button('버튼 1')

st.write('버튼 1 클릭 상태 : ', clicked)

if clicked:
    st.write('버튼 1을 클릭했습니다')
else :
    st.write('버튼 1을 클릭하지 않았습니다')

clicked = st.button('버튼 2')
st.write('버튼 2 클릭 상태 : ', clicked)

if clicked:
    st.write('버튼 2을 클릭했습니다')
else :
    st.write('버튼 2을 클릭하지 않았습니다')