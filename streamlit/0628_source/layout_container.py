def run():
    import streamlit as st
    import numpy as np
    import time

    st.title('Streamlit Container')
    st.markdown('- 여러 요소들을 담을 수 있는 컨테이너라는 요소를 생성하는 함수')
    st.markdown('- 요소들을 그룹화하고 필요한 시점에 표시하거나 숨길 수 있는 함수')

    st.divider()
    st.code('st.container(use_column_width, scrolls, expand, clear_on_reload)')

    # use_column_width : 컨테이너의 너비를 현재 열의 너비로 설정 여부. default : False
    # scrolls : 컨테이너 스크롤 가능 여부. 기본값 : False
    # expand : 컨테이너 너비를 최대로 확장할 지 여부. default : False
    # clear_on_reload : 스트림릿이 reload 될 때 컨테이너 내부 상태를 지울지 여부.기본값
    #                   default : False

    st.header('st.container 1')
    container = st.container()
    container.write('첫번째 생성한 컨테이너 내부에 출력')
    st.write('컨테이너 외부에 출력')

    st.divider()

    st.header('st.container 2')
    with st.container():
        st.write('두번째 생성한 컨테이너 내부에 출력')
        st.bar_chart(np.random.randn(50, 3))
    st.write('컨테이너 외부에 출력')

    st.divider()

    st.header('st.container 3')
    container3 = st.container()
    container3.write('컨테이너3의 내부')
    st.write('컨테이너 외부')

    # 컨테이너 3에 추가적인 컴포넌트 추가
    container3.write('이 역시 컨테이너3 내부')

    st.divider()

    st.header('st.empty')
    # 비어있는 컨테이너
    container4 = st.empty()

    container4.text('Hello empty container world')

    # 3초 후에 컨테이너 내용을 변경
    time.sleep(3)
    container4.text('wow streamlit module')

    # 3초 후에 컨테이너 내용을 없애기
    time.sleep(3)
    container4.empty()












