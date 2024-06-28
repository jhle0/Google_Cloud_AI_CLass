'''
<요구사항>

1) 이름을 입력받는 텍스트 입력 필드 추가
2) 나이를 입력받는 텍스트 입력 필드 추가
3) 성별을 선택할 수 있는 라디오 버튼 추가
4) 입력된 정보를 바탕으로 맞춤형 환영 메시지와 나이에 따른 간단한 메시지 표시

'''

import streamlit as st

st.title('텍스트 요소 기반 APP')

# 1) 이름을 입력받는 텍스트 입력 필드 추가
name = st.text_input('이름을 입력하세요')

# 2) 나이를 입력받는 텍스트 입력 필드 추가
age = st.text_input('나이를 입력하세요')

# 3) 성별을 선택할 수 있는 라디오 버튼 추가
gender = st.radio('성별을 선택하세요', ('Male', 'Female', 'Other'))

# 4) 입력된 정보를 바탕으로 맞춤형 환영 메시지와 나이에 따른 간단한 메시지 표시
if name and age:
    st.write(f'<h2>{name} 님 어서오세요</h2', unsafe_allow_html=True)

    try :
        age = int(age)
        if age <= 19 :
            st.write('미성년 이시네요. 부모 동의가 필요합니다.')
        else :
            st.write('환영합니다.')
    except ValueError:
        st.error('나이는 숫자로 입력하세요')

    st.write(f'gender : {gender}')








