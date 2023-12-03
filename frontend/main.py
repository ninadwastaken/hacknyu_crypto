import streamlit as st
from read_add_user_memo_data import read_user

st.header("SafeSpend")

with st.form(key="email_form"):
    store_name = st.text_input("store name")
    product_name = st.text_input("product name")
    product_cost = st.text_input("product cost")
    receiver_venmo_id = st.text_input("receiver venmo id")
    user_id = st.text_input("user_id")

    col1,col2 = st.columns(2)

    with col1:
        submit_button1 = st.form_submit_button("pay using discretionary money")


    with col2:
        submit_button2 = st.form_submit_button("pay using unlocked savings money")
        user = read_user(user_id)

    if submit_button1:
        user = read_user(user_id)

    if submit_button2:
        user = read_user(user_id)



