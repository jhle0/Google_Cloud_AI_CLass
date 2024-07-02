import streamlit as st
from PIL import Image

def run():
    ''' 사이드바 선택에 따라서 메인 화면 이미지가 바뀌도록 처리 '''

    st.markdown('#### sidebar 기본 표기법')
    st.code('st.sidebar.widget_name')

    # 사이드바 구성
    st.sidebar.title('This is Sidebar')
    st.sidebar.header('텍스트 요소 확인', divider='rainbow')
    user_id = st.sidebar.text_input('아이디(ID) 입력', value='hong', max_chars=20)
    user_password = st.sidebar.text_input('패스워드(PASSWORD) 입력', value='1234', type='password')

    st.sidebar.header('셀렉트 박스', divider='rainbow')
    selectbox_options=['', '진주 귀걸이를 한 소녀', '별이 빛나는 밤', '절규', '월하정인']
    user_option = st.sidebar.selectbox('좋아하는 작품은 무엇인가요?', selectbox_options, index=0)

    if user_option is None:
        pass
    else :
        st.sidebar.write('당신의 선택 : ', user_option)

    # 메인 화면 구성
    st.title('메인 화면')

    folder = '../data/'

    # selectbox option 선택에 따라서 보여줄 이미지 파일 리스트를 선언
    image_files = ['Vermeer.png', 'Gogh.png', 'Munch.png', 'ShinYoonbok.png']

    # 선택된 항목의 이미지를 메인 화면에 표시
    # 사용자가 셀렉트 박스를 선택한 인덱스 번호 인식
    selectbox_options_index = selectbox_options.index(user_option)

    if selectbox_options_index != 0 :
        image_file = image_files[selectbox_options_index-1] # 선택한 항목에 맞는 이미지 파일 지정
        image_local = Image.open(folder+image_file)   # 그 이미지 파일을 로컬 서버 폴더에서 호출
        st.image(image_local, caption=user_option)
    else :
        for i in image_files:
            st.image(Image.open(folder+i))

    # 이미지 크기 고정
    st.markdown('''
    <style>
    img {
        width : 300px;
    }
    </style>
    ''', unsafe_allow_html=True)








