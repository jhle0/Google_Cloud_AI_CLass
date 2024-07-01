import streamlit as st

# 다른 모듈 임포트
import basic_button_widget
import download_button_widget
import selection_widgets
import input_widgets
import dataframe_edit
import camera_capture
import layout_container
import layout_divide
import layout_sidebar
import session

# 세션 상태 초기화
if 'page' not in st.session_state:
    st.session_state.page = "Home"

# 페이지 변경 함수
def set_page(page):
    st.session_state.page = page

# 사이드바에 페이지 링크 추가
with st.sidebar:
    st.header("streamlit app")
    if st.button("Home"):
        set_page("Home")
    if st.button("Basic Button Widget"):
        set_page("Basic Button Widget")
    if st.button("Download Button Widget"):
        set_page("Download Button Widget")
    if st.button("Selection Widgets"):
        set_page("Selection Widgets")
    if st.button("Input Widgets"):
        set_page("Input Widgets")
    if st.button("Dataframe Edit"):
        set_page("Dataframe Edit")
    if st.button("Camera Capture"):
        set_page("Camera Capture")
    if st.button("Layout Container"):
        set_page("Layout Container")
    if st.button("Layout Divide"):
        set_page("Layout Divide")
    if st.button("Layout Sidebar"):
        set_page("Layout Sidebar")
    if st.button("Session"):
        set_page("Session")

# 현재 페이지에 따라 적절한 함수를 호출
if st.session_state.page == "Home":
    st.header("Welcome to the Home Page")
elif st.session_state.page == "Basic Button Widget":
    basic_button_widget.run()
elif st.session_state.page == "Download Button Widget":
    download_button_widget.run()
elif st.session_state.page == "Selection Widgets":
    selection_widgets.run()
elif st.session_state.page == "Input Widgets":
    input_widgets.run()
elif st.session_state.page == "Dataframe Edit":
    dataframe_edit.run()
elif st.session_state.page == "Camera Capture":
    camera_capture.run()
elif st.session_state.page == "Layout Container":
    layout_container.run()
elif st.session_state.page == "Layout Divide":
    layout_divide.run()
elif st.session_state.page == "Layout Sidebar":
    layout_sidebar.run()
elif st.session_state.page == "Session":
    session.run()
