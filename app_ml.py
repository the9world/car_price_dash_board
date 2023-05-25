import numpy as np
import streamlit as st
import joblib
# from model.regessor import 

def run_app_ml():
    st.subheader('자동차 금액 예측')
    
    # 성별, 나이, 연봉, 카드빚, 자산을 유저한테 입력 받는다.
    gender= st.radio('성별 선택', ['남자', '여자'])
    if gender =='남자' :
        gender = 0 # 유저 입력 값을 이진수로 변환
    else :
        gender = 1
    
    age = st.number_input('나이 입력', 18, 100) # 유저에게 입력 받을 나이(숫자)
    salary = st.number_input('연봉 입력', 5000, 1000000) # 파라미터 최소, 최대범위
    debt = st.number_input('카드 빚', 0, 1000000)
    worth = st.number_input('자산 입력', 1000, 10000000)
    
    # 턴을 누르면 예측한 금액을 표시한다.
    if st.button('금액 예측'): 
        new_data = np.array( [ gender, age, salary, debt, worth ] ) # 여러개면 꼭 []
        new_data = new_data.reshape(1, 5) # 입력 받은 값을 2차원으로 변환 : 1행 5열
    
        # regressor 불러오기, 학습한 데이터 가져오기
        regressor = joblib.load('model/regressor.pkl')
        y_pred = regressor.predict(new_data)
        print(y_pred)
                
        # 28220달러 짜리 차량 구매 가능합니다. 출력
        print(y_pred[0]) # 왜 y_pred[0]이 숫자?
        print( round( y_pred[0] ) ) # 반올림
        price = ( round( y_pred[0] ) )
        
        # st.text(f'{y_pred:.2f}달러짜리 차량 구매 가능합니다.') # 이거 안되는 듯?
        # st.text(str(price) + '달러짜리 차량 구매 가능합니다.')
        # st.text('{}달러 짜리 차량 구매 가능합니다.').format(y_pred)
        st.text(f"{int(y_pred)}달러 짜리 차량 구매 가능합니다.")
        # price는 round(반올림) 해서 int없어도 됨, y_pred는 int 필요 
    
    # 버튼을 누르면 예측한 금액을 표시한다.