def run():
    import streamlit as st
    from PIL import Image
    import matplotlib.pyplot as plt
    import pandas as pd
    import numpy as np

    st.subheader('Data Editor ex')

    # 데이터 프레임 및 다양한 데이터 구조를 테이블 형태의 UI에서 편집할 수 있도록 제공.
    # 사용자가 데이터를 편집하고 수정할 수 있는 기능을 제공.

    st.code('''
    st.data_editor(data, [, width=None, height=None, use_container_width=False,
                   hide_index=None, colomn_order=None, column_config=None,
                   num_rows='fixed', disabled=False])
    ''')

    # data : 데이터 에디터 함수로 편집할 데이터
    # width(int) : 데이터 에디터의 원하는 너비. None : 자동 결정
    # height(int) : 데이터 에디터의 원하는 높이 : None : 자동 결정
    # use_container_width : True이면 데이터 에디터 너비를 부모 컨테이너의 너비로 설정
    #                     : 이 값은 width 인자값보다 우선.
    # hide_index(bool) : 인덱스 열을 숨길지 여부 결정. default : None
    # column_order : 열의 표시 순서 결정. None : 원본 데이터 구조를 상속
    # column_config : 열이 표시되는 방식을 구성. 편집 속성을 설정. 딕셔너리 형식으로 구성
    # num_rows : 행 추가 또는 삭제 여부를 지정. \
    #          : fixed - 사용자가 행을 추가하거나 삭제할 수 없다.
    #          : dynamic - 사용자가 행을 추가하거나 삭제 가능, 열 정렬은 비활성화 됨

    df = pd.DataFrame(
        [
            {'명령어': 'st.selectbox', '평점':4, 'is_widget' : True},
            {'명령어': 'st.ballons', '평점':5, 'is_widget' : False},
            {'명령어': 'st.time_input', '평점':3, 'is_widget' : True},
        ]
    )

    st.data_editor(df, height=200, num_rows='fixed', key=1)
    st.divider()
    st.data_editor(df, height=None, num_rows='fixed', key=2)

    st.divider()
    st.data_editor(df, height=200, num_rows='fixed', hide_index=True, key=3)
    st.divider()
    st.data_editor(df, height=None, num_rows='fixed', hide_index=False, key=4)

    st.divider()
    st.data_editor(df, height=200, num_rows='fixed', hide_index=True,
                   column_order=('is_widget', '명령어', '평점'), key=5)
    st.divider()
    st.data_editor(df, height=None, num_rows='fixed', hide_index=False,
                   column_order=None, key=6)

    st.divider()
    edit_df = st.data_editor(df, column_config={
        "명령어" : "Streamlit 명령어",
        "평점" : st.column_config.NumberColumn(
            '여러분이 부여하는 평점',
            help='이 명령어에 몇 점을 부여하시겠습니까?(1-5)',
            min_value=1,
            max_value=5,
            step=1),
        "is_widget":"위젯인가요?",
    },
            disabled=['명령어', 'is_widget'],
            hide_index=True,
            key=7
    )





