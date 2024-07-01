# 목적 : 스트림 코드의 동작을 제어
#
# 스트림릿은 코드를 실행한 후 앱을 재실행하거나, 입력 위젯을 조작하면
# 전체 코드를 처음부터 끝까지 다시 실행하는 구조
#
# 코드가 한 번 실행된 상태를 세션이라고 부름
#
# 일반적인 변수는 세션 간 공유되지 X
#
# 세션 상태(session_state)를 이용해 해결 가능
#     : 이전 세션에서 변경한 상태를 저장하고 그대로 유지

import streamlit as st

def run():
    st.header('Session State')
    st.divider()

    # 세션 상태 초기화 : 기본 구조 key - value(숫자, 문자, 논리, 리스트)
    if 'count' not in st.session_state:
        st.session_state['count'] = 0

    if 'registered' not in st.session_state:
        st.session_state['registered'] = []

    # 텍스트 입력 위젯
    user_input = st.text_input('이름', placeholder='이름을 입력하세요', key='name')

    # 버튼 입력 위젯
    clicked = st.button('등록')

    if clicked:
        st.session_state['count'] = st.session_state['count'] + 1
        st.write('버튼 클릭: ', st.session_state['count'])

        name = st.session_state['name']
        st.session_state['registered'].append(name)
        st.write('등록 이름 리스트: ', st.session_state['registered'])



    # 콜백(callback) : 특정 함수를 다른 함수의 인자로 전달하고, 이후에 미리 정해진 조건을 충족하거나 이벤트가 발생했을 때 해당 함수를 호출하는 패턴
    #               : 이 때 전달하는 특정함수를 콜백함수
    st.header("callback")
    st.divider()

    if 'lang' not in st.session_state:
        st.session_state['lang'] = '영어'

    # 콜백 함수
    def btn_callback(lang):
        st.session_state['lang'] = lang

    # 라디오 버튼
    radio_options = ['영어', '스페인어', '일본어']
    radio_selected = st.radio("한국어를 어떤 언어로 번역하겠습니까? ", radio_options)

    # 버튼 위젯(이벤트가 일어날 위젯), args에 콜백 함수 인수 지정
    clicked = st.button('선택', on_click=btn_callback, args=[radio_selected])

    # 콜백 함수를 호출한 결과 출력
    st.write(f"한국어를 {st.session_state['lang']}으로 번역하도록 선택했음")






