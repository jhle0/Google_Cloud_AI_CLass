import streamlit as st

st.title("example streamlit button")


# button 동시 클릭 X (하나만 선택 가능 - radiobutton 식)

clicked = st.button('button1')

st.write("button1 clicked state:", clicked)

if clicked:
    st.write("clicked")
else:
    st.write("not clicked")


clicked = st.button('button2')

st.write("button2 clicked state:", clicked)

if clicked:
    st.write("clicked")
else:
    st.write("not clicked")