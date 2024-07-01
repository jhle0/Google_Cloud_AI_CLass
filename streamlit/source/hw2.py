## 실습1
# import streamlit as st
#
# # 세션 상태 초기화
# if 'name' not in st.session_state:
#     st.session_state['name'] = ''
# if 'age' not in st.session_state:
#     st.session_state['age'] = ''
#
# # 사이드바 입력
# st.sidebar.header("정보 입력")
# st.sidebar.text_input("이름을 입력하세요", key='name', placeholder="이름")
# st.sidebar.text_input("나이를 입력하세요", key='age', placeholder="나이")
#
# # 메인 화면
# st.title("사용자 정보")
# st.write(f"사용자 이름: {st.session_state['name']}")
# st.write(f"사용자 나이: {st.session_state['age']}")
#
# # 버튼을 클릭하면 이름과 나이를 리셋
# if st.button("리셋"):
#     st.session_state['name'] = ''
#     st.session_state['age'] = ''



# 실습 2
import streamlit as st

# 세션 상태 초기화
if 'name' not in st.session_state:
    st.session_state['name'] = ''
if 'age' not in st.session_state:
    st.session_state['age'] = ''

# 콜백 함수 정의
def update_info():
    st.session_state['name'] = st.session_state['input_name']
    st.session_state['age'] = st.session_state['input_age']

def reset_info():
    st.session_state['name'] = ''
    st.session_state['age'] = ''
    st.session_state['input_name'] = ''
    st.session_state['input_age'] = ''

# 사이드바 입력
st.sidebar.header("정보 입력")
st.sidebar.text_input("이름을 입력하세요", key='input_name', placeholder="이름", on_change=update_info)
st.sidebar.text_input("나이를 입력하세요", key='input_age', placeholder="나이", on_change=update_info)

# 버튼
st.sidebar.button("Update", on_click=update_info)
st.sidebar.button("Reset", on_click=reset_info)

# 메인 화면
st.title("사용자 정보")
st.write(f"현재 입력된 이름: {st.session_state['name']}")
st.write(f"현재 입력된 나이: {st.session_state['age']}")





