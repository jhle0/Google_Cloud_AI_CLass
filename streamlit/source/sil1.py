import streamlit as st

st.title("실습 1")
st.divider()

user_name = st.text_input('name : ', placeholder="이름을 입력하세요")
user_age = st.text_input('age : ', placeholder="나이를 입력하세요")
sex_options = ['남', '여']
user_sex = st.radio('성별을 선택하세요', sex_options)

if user_name and user_age and user_sex:
        age = int(user_age)
        st.write(f"환영합니다, {user_name}님!")
        if user_sex == '남':
            st.write(f"당신은 {age}살 남성이시네요.")
        else:
            st.write(f"당신은 {age}살 여성이시네요.")
else:
    st.write("모든 정보를 입력해주세요.")
