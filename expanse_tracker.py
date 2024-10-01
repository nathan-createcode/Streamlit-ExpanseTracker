import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Inisialisasi DataFrame untuk menyimpan data pengeluaran
if 'expenses' not in st.session_state:
    st.session_state['expenses'] = pd.DataFrame(columns=['Amount', 'Category', 'Detail', 'Date'])

# Judul aplikasi
st.title("my money waster tracker app ")

# Input data pengeluaran
st.header("Input Expense")
amount = st.number_input("Enter amount:", min_value=0, step=1)
category = st.selectbox("Select category:", ['Food', 'Drink', 'Transport', 'Entertainment', 'Other'])

# Input detail pengeluaran untuk setiap kategori
detail = st.text_input("Enter detail about your expense:")

date = st.date_input("Select date:", value=datetime.today())

# Tombol untuk menambahkan data pengeluaran
if st.button("Add Expense"):
    # Gunakan kategori yang ditentukan oleh pengguna
    final_category = category
    new_data = pd.DataFrame({'Amount': [amount], 'Category': [final_category], 'Detail': [detail], 'Date': [date]})
    st.session_state['expenses'] = pd.concat([st.session_state['expenses'], new_data], ignore_index=True)
    st.success("Expense added successfully!")

# Menampilkan data dalam bentuk tabel
st.header("Expense Data")
if not st.session_state['expenses'].empty:
    st.dataframe(st.session_state['expenses'])

    # Menampilkan data dalam bentuk grafik
    st.header("Expense Summary by Category")
    summary = st.session_state['expenses'].groupby('Category')['Amount'].sum()

    # Membuat pie chart untuk visualisasi
    fig, ax = plt.subplots()
    ax.pie(summary, labels=summary.index, autopct='%1.1f%%')
    st.pyplot(fig)

    # Grafik batang pengeluaran per tanggal
    st.header("Expense Over Time")
    st.line_chart(st.session_state['expenses'].set_index('Date')['Amount'])
else:
    st.write("No expenses to show yet.")
