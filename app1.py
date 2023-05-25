import streamlit as st
from app_module.app1_home import run_app_home
from app_module.app_eda import run_app_eda
from app_module.app_ml import run_app_ml

def main():
    st.title("자동차 가격 예측 앱")
    menu= ['Home', 'EDA', 'ML']
    choice = st.sidebar.selectbox('메뉴', menu)
    
    if choice==menu[0]:
        run_app_home()
    if choice==menu[1]:
        run_app_eda()
    

    
if __name__=='__main__':
    main()