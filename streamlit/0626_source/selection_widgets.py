import streamlit as st

st.title('사용자 선택을 요구하는 대표적 위젯들')

st.header('체크박스', divider='rainbow')

st.code('st.checkbox(label, [, value=False])')

st.markdown('''
<!-- <div>label : 체크박스 옆에 표시될 문자
value : 체크박스 초기 상태. 기본값은 False

리턴되는 값은 T/F </div> -->
''', unsafe_allow_html=True)


checked1 = st.checkbox('체크박스 1')
st.write('체크 박스 상태 : ', checked1)

checked2 = st.checkbox('체크박스 2',
                       value=True)
st.write('체크 박스 상태 : ', checked2)

st.divider()
st.write('')


st.header('라디오 버튼', divider='rainbow')

st.markdown('''
<!-- <div>
    미리 정의된 여러 선택 항목(옵션) 묶음 중 하나를 선택
    </div>-->
'''
, unsafe_allow_html=True)


st.code('st.radio(label, options [, index=0, horizontal=False])')

st.markdown('''
<!-- 
<div>
label : 라디오 버튼에 표시할 문자열
options : 선택항목 라벨을 담고 있는 리스트 또는 튜플.
          선택항목 라벨 갯수만큼 라디오 버튼 선택항목이 생성.
index : 초기 선택 항목 지정. default : 0
horizontal : 선택 항목 라벨 배치 순서. True : 가로 방향, False : 세로방향. default : False

리턴되는 값은 : 선택한 항목의 라벨값
</div>
-->
''', unsafe_allow_html=True)

radio1_options = ['10', '20', '30', '40']
radio1_selected = st.radio('(5 * 5) + 5 는 얼마인가요?', radio1_options)
st.write('선택한 답 : ', radio1_selected)

radio2_options = ['10', '20', '30', '40']
radio2_selected = st.radio('(5 * 5) + 5 는 얼마인가요?', radio1_options, index=2, horizontal=True)
st.write('선택한 답 : ', radio2_selected)

st.divider()

st.header('셀렉트 박스 :blue[selectBox]', divider='rainbow')

st.markdown('```  st.selectbox(label, options [, index=0])  ```')

selectbox1_options = ['한식', '중식', '일식', '양식', '분식']
your_option1 = st.selectbox('내일 뭐 먹지?', selectbox1_options)
st.write('여러분의 선택 : ', your_option1)

# selectbox2_options = ['-'*50, '한식', '중식', '일식', '양식', '분식']
# your_option2 = st.selectbox('내일 뭐 먹지?', selectbox2_options, index=0)
# st.write('여러분의 선택 : ', your_option2)

# [실습] '-----' 선택(출력) 안되게 처리
selectbox3_options = ['-'*50, '한식', '중식', '일식', '양식', '분식']
your_option3 = st.selectbox('내일 뭐 먹지?', selectbox3_options)

if your_option3 == selectbox3_options[0]:
    pass
else :
    st.write('여러분의 선택 : ', your_option3)






