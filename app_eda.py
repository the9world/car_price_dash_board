import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def run_app_eda():
    st.subheader('데이터 분석')
    
    df= pd.read_csv("data/Car_Purchasing_Data.csv", encoding= "ISO-8859-1")
    print(df)
    
    if st.checkbox('데이터 프레임 보기') :
        st.dataframe(df)

    st.subheader('기본 통계 데이터')
    st.dataframe(df.describe())
    
    st.subheader('최대 / 최소 데이터 확인하기')
    # st.selectbox('컬럼을 선택하세요', df.columns) # 문자열 컬럼 제외 해야함
    column = st.selectbox('컬럼을 선택하세요', df.columns[ 3 : ] )

    st.success('최대 데이터') # 유저가 선택한 컬럼의 최소, 최대 값을 보여줌
    st.dataframe( df.loc[df[column]== df[column].max(), ] )    
    st.success('최소 데이터')
    st.dataframe( df.loc[df[column]== df[column].min(), ] )
    
    st.subheader('컬럼 별 히스토그램') 
    # column = st.selectbox('컬럼을 선택하세요', df.columns[ 3 : ] ) # 이대로는 line 20과 동일하여 error 발생
    column = st.selectbox('히스토그램 확인할 컬럼을 선택하세요', df.columns[ 3 : ] ) # 숫자 데이터만 보기
    bins = st.number_input('빈의 갯수를 입력하세요. 10 ~ 30', 10, 30, 20) # bins의 갯수를 유저에게 받음
    
    fig= plt.figure() # 영역 잡아주기
    df[column].hist(bins=bins) # df[유저가 선택한 컬럼(변수) 입력]
    plt.title(column + " Histogram") # 그래프 타이틀
    plt.xlabel(column) # x축 이름
    plt.ylabel("count") # y축 이름
    st.pyplot(fig)
    
    # 유저에게 컬럼 선택권을 줌 (상관계수, corr)
    st.subheader('상관 관계 분석')
    column_list= st.multiselect('상관분석 하고싶은 컬럼을 선택하세요', df.columns[ 3 : ] ) # 숫자 데이터만 보기
    # 여러개 하려면 list로 해야함 : data=df[column_list].corr() 상관계수
    
    # 2개 이상 선택하면 히스토그램 출력하기
    if len(column_list) >= 2:
        fig2 = plt.figure()
        sns.heatmap(data=df[column_list].corr(), annot=True, vmin=-1, vmax=1,
                cmap='coolwarm', fmt='.2f', linewidths= 0.5)
        st.pyplot(fig2)    
    else:
        st.error('2개 이상 선택하세요')