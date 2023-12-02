import streamlit as st
import pandas as pd
import numpy as np
import pickle
import json

# Load all files
with open('scaler.pkl', 'rb') as file_1:
  scaler = pickle.load(file_1)

with open('model_knn.pkl', 'rb') as file_2:
  model_knn = pickle.load(file_2)

def run():
    # Membuat Form
    with st.form(key='Form Credit Card Default'):
        limit_balance = st.number_input('Limit Balance', min_value=0, max_value=800000, value=10000)
        pay_1 = st.number_input('Pay 1', min_value=-2, max_value=8, value=-2)
        pay_2 = st.number_input('Pay 2', min_value=-2, max_value=7, value=-2)
        pay_3 = st.number_input('Pay 3', min_value=-2, max_value=7, value=-2)
        pay_4 = st.number_input('Pay 4', min_value=-2, max_value=8, value=-2)
        pay_5 = st.number_input('Pay 5', min_value=-2, max_value=7, value=-2)
        pay_6 = st.number_input('Pay 6', min_value=-2, max_value=7, value=-2)

        submitted = st.form_submit_button('Predict')

    data_inf = {
        'lb': limit_balance,
        'pay_1': pay_1,
        'pay_2': pay_2,
        'pay_3': pay_3,
        'pay_4': pay_4,
        'pay_5': pay_5,
        'pay_6': pay_6,
    }

    data_inf = pd.DataFrame([data_inf])
    st.dataframe(data_inf)

    if submitted:
        # Memisahkan data kategorik dan numerikal
        inf_num = data_inf[['lb']]
        inf_cat = data_inf[['pay_1', 'pay_2', 'pay_3', 'pay_4','pay_5','pay_6']]
        
        # Feature Scaling
        inf_num_scaled = scaler.transform(inf_num)
        inf_final = np.concatenate([inf_num_scaled,inf_cat],axis = 1)

        # Membuat kolom predict 
        y_pred_inf = model_knn.predict(inf_final)
        y_pred_inf

        st.write('Payment Next Month Prediction : ', str(int(y_pred_inf)))

if __name__ == '__main__':
    run()