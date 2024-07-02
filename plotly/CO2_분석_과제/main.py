import streamlit as st
import pandas as pd
import numpy as np

import plotly.express as px
import plotly.graph_objects as go




# 표
df = pd.read_csv("/Users/ljeonghyeon/Documents/Google_Cloud_AI/plotly/CO2_분석_과제/CO2_Emissions.csv")
ex_df = df.head().T
st.dataframe(ex_df)



# 제목 & 설명
st.title("차량 CO2 배축에 관한 데이터 분석")
st.text('''안녕하세요. 이 웹페이지는 Python Streamlit 라이브러리를 사용하여 만든 간단한 데이터 분석 
웹 대시보드입니다. 이 페이지에서는 일부 변수의 분포나 변수 간의 상관 관계를 시각화 할 수 있습니다.''')




# sidebar
st.sidebar.title('분석하고 싶은 데이터 선택')
st.sidebar.divider()

options = ['COMPACT', 'SUV - SMALL', 'MID-SIZE', 'TWO-SEATER', 'MINICOMPACT', 'SUBCOMPACT', 'FULL-SIZE']
vehicle_class = st.sidebar.multiselect('분석하고 싶은 차량 등급을 선택:', options)

engine_size = st.sidebar.slider(
    '분석하려는 엔진 크기 선택 (Liter):',
    min_value=0.9,
    max_value=8.4,
    value=(1.6, 6.0),
    step=0.1
)

# 필터링된 데이터프레임
filtered_df = df[(df['Vehicle Class'] == vehicle_class) &
                 (df['Engine Size(L)'] >= engine_size[0]) &
                 (df['Engine Size(L)'] <= engine_size[1])]






# 1) 엔진 크기 분석
st.divider()
st.subheader("엔진 크기 분석")
[col1, col2] = st.columns(2)
with col1:
    st.text('''자동차 제조업체별 엔진 크기의 상자 그림. 
제조업체는 각 브랜드에 대해 어떤 유형의 엔진 
크기를 가장 많이 생산합니까?''')

with col2:
    # 엔진 크기와 제조업체별로 그룹화하여 CO2 배출량의 평균 계산
    engine_make_avg_co2 = filtered_df.groupby(['Engine Size(L)', 'Make'])['CO2 Emissions(g/km)'].mean().reset_index()

    # Plotly를 사용하여 시각화
    fig = px.scatter(engine_make_avg_co2, x='Engine Size(L)', y='CO2 Emissions(g/km)', color='Make',
                     title='Engine Size vs CO2 Emissions by Manufacturer',
                     labels={'Engine Size(L)': 'Engine Size (Liter)', 'CO2 Emissions(g/km)': 'CO2 Emissions (g/km)'})

    st.plotly_chart(fig)





# 2) 엔진 소비 분석
st.divider()
st.subheader("연료 소비 분석")
col1, col2 = st.columns(2)
with col1:
    st.text('''엔진 크기에 따른 연비를 보여주는 산점도 
그래프입니다. 동일한 엔진 크기 내에서 연료 효율이 
더 낮은 제조업체는 어디입니까? 
동일한 엔진 크기 내에서 어느 제조업체의 
연료 효율이 더 높습니까?''')
    fuel_options = ['Fuel Consumption City (L/100 km)', 'Fuel Consumption Hwy (L/100 km)', 'Fuel Consumption Comb (L/100 km)']
    fuel_select = st.selectbox("Y축 선택", fuel_options)

with col2:
    fig = px.scatter(
        filtered_df,
        x='Engine Size(L)',
        y=fuel_select,
        color='Make',
        title='Engine Size vs Fuel Consumption by Manufacturer',
        labels={
            'Engine Size(L)': 'Engine Size (Liter)',
            fuel_select: fuel_select
        }
    )

    st.plotly_chart(fig)






# 3) 탄소 배출 분석
st.divider()
st.subheader("탄소 배출 분석")
col1, col2 = st.columns(2)
with col1:
    st.text('''연비와 탄소배출량의 상관관계를 제조사별 색상으로 
구분하여 나타낸 산점도 그래프입니다. 
동일한 연비 범위 내에서 어느 제조업체의 탄소 
배출량이 더 높을 수 있습니까?''')
    CO2_options = ['Fuel Consumption City (L/100 km)', 'Fuel Consumption Hwy (L/100 km)', 'Fuel Consumption Comb (L/100 km)']
    CO2_select = st.selectbox("X축 선택", CO2_options)

with col2:
    fig = px.scatter(
        filtered_df,
        x=CO2_select,
        y='CO2 Emissions(g/km)',
        color='Make',
        title='Fuel Consumption vs CO2 Emissions by Manufacturer',
        labels={
            CO2_select: CO2_select,
            'CO2 Emissions(g/km)': 'CO2 배출량 (g/km)'
        }
    )
    st.plotly_chart(fig)






