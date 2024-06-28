'''
<요구사항>
1) CSV 파일을 업로드할 수 있는 기능 구현
2) 업로드된 데이터를 데이터 프레임으로 표시
3) 데이터 프레임의 열 이름을 선택할 수 있는 드롭다운 메뉴 추가
4) 선택된 열의 히스토그램을 그리기
'''

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title('데이터 시각화 APP')

# 1) CSV 파일을 업로드할 수 있는 기능 구현
upload_file = st.file_uploader('CSV File upload', type='csv')
if upload_file is not None:
    # 2) 업로드된 데이터를 데이터 프레임으로 표시
    df = pd.read_csv(upload_file)
    st.write('데이터 미리보기', df)

    # 3) 데이터 프레임의 열 이름을 선택할 수 있는 드롭박스 메뉴 추가
    column = st.selectbox('위 데이터 프레임에 있는 컬럼을 선택하세요', df.columns)

    # 4) 선택된 열의 히스토그램을 그리기
    if column :
        fig, ax = plt.subplots()
        df[column].hist(bins=30, ax=ax)
        ax.set_title(f'Histogram of {column}')
        ax.set_xlabel(column)
        ax.set_ylabel('Frequency')
        st.pyplot(fig)


