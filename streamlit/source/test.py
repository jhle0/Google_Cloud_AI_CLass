# 데이터 출력

# 텍스트 요소, 미디어 요소, 데이터 요소
## 데이터 요소 : 정보를 전달하고 설명
## 미디어 요소 : 이미지, 오디오, 비디오 파일을 출력
## 데이터 요소 : 데이터 프레임 및 테이블 형식으로 데이터를 표시

import streamlit as st

# 1. 텍스트 요소

# # title > header > subheader
# # st.title : 기본적으로 생각하는 제목 크기
# st.title("Hello. This is \'st.title\'")
#
# # st.header : st.title 보다 작은 제목
# st.header("This is \'st.header\'")
#
# # st.subheader : 가장 작은 제목
# st.subheader("This is \'st.subheader\'")
#
#
# # markdown : 일반 텍스트에 글자색, 글씨체 등의 시각효과를 주는 코드
#
# # markdown 일부 형식
# # - 진하게 : 별표(**) 또는 언더바(__)
# # ex) **bold**, __bold__
# # - 기울기 : 별표(*) 또는 언더바(_)
# # ex) *기울기*, _기울기_
# # - 색상 : :color[텍스트] 형식
# # ex) :red[빨강], :blue[파랑]
#
# # st.markdown
# st.markdown("This is **markdown**")
# st.markdown("This sent is :red[RED], _:blue[BLUE]_")

# # st.text
# # st.text : 가장 기본적인 글쓰기 형식 - 마크다운 지원 x
# st.text("this is \'st.text\'")


# # st.caption
# # st.caption - 캡션, 부제, 각주 등에 사용
#
# st.title("What is caption?")
# st.caption("this is \'st.caption\'")


# # 실습 1
# st.title("Streamlit 소개")
# st.header("Streamlit이란?")
# st.subheader("개요")
# st.text('''Steamlit은 데이터 과학자와 머신러닝 엔지니어가 간단한 Python 스크립트를 사용하여 대화형
# 웹 애플리케이션을 쉽게 만들 수 있도록 도와주는 오픈 소스 프레임워크입니다.
# 이를 통해 사용자는 데이터 분석, 시각화 모델 배포 등을 빠르게 구현할 수 있습니다.\n''')
#
# st.subheader("주요 기능")
# st.text("Streamlit은 다음과 같은 기능들을 제공합니다")
#
# st.markdown("- __빠른 개발__: 몇 줄의 코드만으로 데이터 애플리케이션을 개발할 수 있습니다. ")
# st.markdown("- __자동화된 UI 생성__: 코드에 따라 자동으로 웹 인터페이스가 생성됩니다.")
# st.markdown("- __실시간 업데이트__: 데이터가 변경되면 실시간으로 애플리케이션이 업데이트 됩니다.")
# st.markdown("- __확장성__: 다양한 Python 라이브러리와 쉽게 통합할 수 있습니다")



# # st.code
# # st.code : 코드 블록
#
# # st.code(body, language="python")
#
# code = '''def text()
#     print("Hello, Streamlit")'''
#
# st.code(code, language="python", line_numbers=True)
# # line_numbers : 줄 번호 표시



# st.divider
# st.divider: 구분선

st.title("Introduce Streamlit")
st.divider()
st.header("What is Streamlit?")



