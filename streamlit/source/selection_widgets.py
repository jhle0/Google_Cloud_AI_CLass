import streamlit as st
def run():

    st.title("Check_Box")

    st.code('st.checkbox(label, [, value=False])')

    st.markdown('''
    <!--
        label : 체크박스 옆에 표시될 문잘
        value : 체크박스 초기 상태 (기본값 False)
        return 값 T/F 
    --> 
    ''', unsafe_allow_html=True)



    checked1 = st.checkbox('check-box1')
    st.write('체크 박스 상태: ', checked1)

    checked2 = st.checkbox('check-box2', value=True)
    st.write('체크 박스 상태: ', checked2)


    st.markdown('---')


    st.title("Radio Button")

    st.code('st.radio(label, options [index=0, horizontal=False])')

    st.markdown('''
    <!--
    label : 라디오 버튼에 표시할 문자열
    options : 선택항목 라벨을 담고 있는 리스트 또는 튜플
              선택항목 라벨 갯수만큼 라디오 버튼 선택항목이 생성
    index : 초기 선택 항목 지정, (default = 0)
    horizontal : 선택 항목 라벨 배치 순서, True: 가로, False : 세로방향, default: False
    
    return 값-> 선택한 항목의 라벨값
    -->
    ''', unsafe_allow_html=True)


    radio1_options = ['10', '20', '30', '40']
    radio1_selected = st.radio('(5 * 5) + 5 는 얼마인가요?', radio1_options)
    st.write("선택한 답: ", radio1_selected)


    radio2_options = ['10', '20', '30', '40']
    radio2_selected = st.radio('(5 * 5) + 5 는 얼마인가요?', radio2_options, horizontal=True)
    st.write("선택한 답: ", radio2_selected)


    st.divider()
    st.title("Select Box")

    st.code('st.selectbox(label, options [, index=])')

    selectbox1_options = ['한식', '중식', '일식', '양식', '분식']
    your_option1 = st.selectbox("내일 뭐 먹지?", selectbox1_options)
    st.write('여러분의 선택', your_option1)


    # selectbox2_options = ['-'*50,'한식', '중식', '일식', '양식', '분식']
    # your_option2 = st.selectbox("내일 뭐 먹지?", selectbox2_options, )
    # st.write('여러분의 선택', your_option2)


    selectbox2_options = ['한식', '중식', '일식', '양식', '분식']
    your_option2 = st.selectbox("내일 뭐 먹지?", selectbox2_options, index=None, placeholder="Select contact method...")
    st.write('여러분의 선택:', your_option2)

