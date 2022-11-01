import streamlit as st
import eda
import predict

navigation = st.sidebar.selectbox('pilih halaman : ', ('Exploratory data analysis', 'Predict data '))

if navigation == 'Exploratory data analysis' :
    eda.run()
else:
    predict.run()