import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("데이터 시각화 애플리케이션")
st.divider()

uploaded_file = st.file_uploader("CSV 파일을 업로드하세요", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("업로드된 데이터:")
    st.dataframe(df)

    column = st.selectbox("데이터 프레임으로 보고싶은 열을 선택하세요", df.columns, index=None,  placeholder="열 선택")

    if column:
        fig, ax = plt.subplots()
        ax.hist(df[column], bins=20, edgecolor='k')
        ax.set_title(f'{column} 히스토그램')
        ax.set_xlabel(column)
        ax.set_ylabel('Frequency')
        st.pyplot(fig)
else:
    st.write("CSV 파일을 업로드하세요.")
