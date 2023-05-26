import streamlit as st

def run_app_home():
    st.subheader('안녕하세요, 감사해요, 잘 있어요, 다시 만나요')
    st.text('좋은 서비스를 제공하겠습니다.')
    
    st.text('이 앱은 고객 데이터와 자동차 구매 데이터에 대한 내용입니다.')
    st.text('데이터 분석도 가능하고, 고객 정보를 넣으면 구매 차량 가격도 예측합니다.')
    img_url= 'https://www.motorgraph.com/news/photo/201905/22564_72789_5839.jpg'
    st.image(img_url)
    
    