def run():
    import streamlit as st

    st.title("Input widgets")

    st.header("Text Input")
    st.divider()

    st.code('st.text_input(label, value="", max_chars=None, type="default")')

    # value : 텍스트 입력 창에 초기에 보이는 문자열
    # max_chars : 최대로 입력할 수 있는 문자의 개수
    # type : 입력 텍스트의 형식 (password - 문자가 *으로 나옴)

    # return 값 : 사용자가 입력한 문자열

    user_ID = st.text_input('ID : ', placeholder="This is id field", max_chars=20)
    user_password = st.text_input("Password: ", placeholder="This is password", type='password')

    if user_ID == 'hong':
        if user_password == '1234':
            st.write('Login complete')
        else:
            st.write('<h4>Wrong password</h4>', unsafe_allow_html=True)
    else:
        st.write('Wrong ID')



    st.header("Text Area")
    st.divider()

    st.code('st.text_area(label, value, height, mar_chars, on_change, disalbled, label_visibility)')

    txt = st.text_area("This is text area", placeholder="최초 표시되는 값")

    st.write("현재 area 문자 개수: ", len(txt))




    st.header("Chat Input")
    st.divider()

    st.code('st.chat_input(placeholder, max_chars, disabled, on_submit')

    prompt = st.chat_input("안녕하세요 무엇을 도와드릴 까요")




    import streamlit as st
    import pandas as pd
    import numpy as np
    import pydeck as pdk

    chart_data = pd.DataFrame(
        np.random.randn(1000, 2) / [50, 50] + [33.459574223653, 126.56120234738],
        columns=['lat', 'lon'])

    st.pydeck_chart(pdk.Deck(
        map_style=None,
        initial_view_state=pdk.ViewState(
            latitude=37.76,
            longitude=-122.4,
            zoom=11,
            pitch=50,
        ),
        layers=[
            pdk.Layer(
                'HexagonLayer',
                data=chart_data,
                get_position=[33.459574223653, 126.56120234738],
                radius=200,
                elevation_scale=4,
                elevation_range=[0, 10000],
                pickable=True,
                extruded=True,
            ),
            pdk.Layer(
                'ScatterplotLayer',
                data=chart_data,
                get_position='[lon, lat]',
                get_color='[200, 30, 0, 160]',
                get_radius=200,
            ),
        ],
    ))
