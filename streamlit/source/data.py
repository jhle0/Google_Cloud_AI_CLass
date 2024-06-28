# import streamlit as st
#
# # 3. 데이터 요소
#
# # st.dataframe
# # st.dataframe : 데이터 프레임
#
# import pandas as pd
#
# st.subheader("MENU")
# df_menu = pd.DataFrame({"name": ['아메리카노', '라떼', '스무디', '밑크티'],
#                         "price": [4500, 8000, 9000, 7500]
#                         })
#
# # st.dataframe(df_menu)
# # st.dataframe(df_menu, width=150, height=180)
#
# # use_container_width : 페이지 열 너비에 맞춰 자동으로 크기 조절
# st.dataframe(df_menu, width=150, height=180, use_container_width=True)
#
#
# # st.table
# # st.table : 정적인 데이터 프레임
# st.subheader("MENU")
#
# list_menu = ['아메리카노', '라떼', '스무디', '밀크티']
#
# st.table(list_menu)




# 실습 2
import streamlit as st
import pandas as pd

st.title("영화 관리 시스템")
st.divider()
st.header("영화 목록")
st.subheader("추천 영화 목록")
st.text("다음은 추천 영화 목록과 각 영화의 감독 밑 개봉 연도입니다.")

df_movie = pd.DataFrame({"영화명": ["인셉션", "인터스텔라", "기생충", "어벤져스"],
                        "감독": ["크리스퍼놀란", "크리스퍼놀란", "봉준호", "조스웨던"],
                         "개봉연도": ["2010", "2020", "2000", "2020"]
                         })
st.dataframe(df_movie, height=178,use_container_width=True)

video_url = "https://youtu.be/DFvFGLomqeg?si=h6KgMzjn5EH4vTCg"
st.video(video_url)


