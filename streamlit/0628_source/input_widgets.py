import streamlit as st

def run():
    st.title('대표적 입력 위젯')

    st.header('텍스트 입력', divider='rainbow')

    st.code('st.text_input(label, value="", max_chars=None, type="default")')

    # value : 텍스트 입력 창에 초기에 보이는 문자열.
    # max_chars : 최대로 입력할 수 있는 문자의 개수.
    # type : 입력 텍스트의 형식. password - 문자가 가려져서 나옴.
    #
    # 리턴되는 값은 문자열

    user_id = st.text_input('아이디(ID) 입력', value='This is id field', max_chars=20)
    user_password = st.text_input('패스워드(Password 입력)', value='This is pw field', type='password')

    if user_id == 'hong' :
        if user_password == '1234':
            st.write('로그인 되었습니다. 서비스를 이용할 수 있습니다.')
        else :
            st.write('<h4>잘못된 패스워드 입니다. 다시 입력하세요</h4>', unsafe_allow_html=True)
    else :
        st.write('없는 ID 입니다. 회원 가입을 하거나 올바른 ID를 입력하세요')

    st.divider()

    st.header('Text Area', divider='rainbow')

    st.code('st.text_area(label, value, height, mar_chars, on_change, disabled, label_visibility)')

    # value : 처음 표시되는 텍스트
    # height : 픽셀 단위로 표현되는 UI 높이
    # max_chars : 허용되는 최대 문자 수
    # on_change : text_area 값이 변경될 때 호출되는 callback 함수 지정
    # disabled : 텍스트 영역 비활성화. default : False
    # label_visibility : 라벨의 가시성

    txt = st.text_area("This is Text Area", "최초 표시되는 값")

    st.write(f'현재 area에 사용된 문자 개수는 {len(txt)} 개.')

    st.divider()

    st.header('Chat Input', divider='rainbow')

    st.code('st.chat_input(placeholder, max_chars, disabled, on_submit)')

    # prompt = st.chat_input('안녕하세요 무엇을 도와드릴까요')
    #
    # if prompt:
    #     st.write(f'사용자 입력 : {prompt}')

    st.divider()

    st.header('날짜 입력', divider='rainbow')

    st.code('st.date_input(label, value="default", min_value, max_value, format="YYYY/MM/dd", disabled)')

    date = st.date_input('당신의 생일은 언제 인가요?')
    st.write(date)

    st.divider()

    st.header('File Input', divider='rainbow')

    st.code('st.file_uploader(label, type=None, accept_multiple_files=False)')

    # type : 허용하는 파일의 확장자를 지정하는 옵션. 지정하지 않으면 모든 파일을 허용. 리스트 형태로 여러 확장자 지정 가능
    # accept_multiple_files=True : 여러 개의 파일을  동시에 업로드 가능.

    from io import StringIO

    upload_file = st.file_uploader('Text 파일을 선택하세요', type='txt')
    if upload_file is not None:
        #텍스트 파일을 읽어서 문자열로 변환
        stringio = StringIO(upload_file.getvalue().decode('utf-8'))
        string_data = stringio.read()
        # 일부만 출력
        st.write(string_data[:20])

    upload_file2 = st.file_uploader('MP3 파일을 선택하세요', type='mp3')
    if upload_file2 is not None:
        #바이너리 파일을 읽어서 바이트 변환
        byte_data = upload_file2.getvalue()
        st.write(byte_data[:100])


