import streamlit as st
import eda
import prediction

page = st.sidebar.selectbox('Pilih Halaman: ', ('EDA', 'Predict Credit Card'))

if page == 'EDA':
    eda.run()
else:
    prediction.run()