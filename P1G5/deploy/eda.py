import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def run():
    st.title('Credit Card Default Data Exploratory')
    # Memanggil data csv
    data = pd.read_csv('P1G5_Set_1_zaky_ramdhani.csv')
    st.dataframe(data)

    # Menampilkan 5 data teratas
    st.caption('Data Head')
    st.table(data.head(5))
    # Menampilkan 5 data terbawah
    st.caption('Data Tail')
    st.table(data.tail(5))

    # Membuat Barplot
    st.write('#### Plot Sex')
    fig = plt.figure(figsize=(15, 5))
    sns.countplot(x='sex', data=data)
    st.pyplot(fig)

    # Membuat Histogram
    st.write('#### Histogram of Limit Balance')
    fig = plt.figure(figsize=(15, 5))
    sns.histplot(data['limit_balance'], bins=30, kde=True)
    st.pyplot(fig)

    # Membuat Histogram Berdasarkan Input User
    st.write('#### Histogram berdasarkan Input User')
    pilihan = st.selectbox('Pilih column : ', ('limit_balance', 'age', 'bill_amt_1', 'bill_amt_2', 'bill_amt_3', 'bill_amt_4', 'bill_amt_5', 'bill_amt_6', 'pay_amt_1', 'pay_amt_2', 'pay_amt_3', 'pay_amt_4', 'pay_amt_5', 'pay_amt_6'))
    fig = plt.figure(figsize=(15, 5))
    sns.histplot(data[pilihan], bins=30, kde=True)
    st.pyplot(fig)

if __name__ == '__main__':
    run()