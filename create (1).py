import streamlit as st
from database import add_data
def create():
    col1, col2 = st.columns(2)
    with col1:
        Train_No = st.text_input("Train Number")
        Name = st.text_input("Train Name:")
        Train_Type = st.text_input("Train Type:")
    with col2:
        Source = st.selectbox("Source", ["Bangalore", "Chennai", "Mumbai", "Mangaluru"])
        Destination = st.selectbox("Destination", ["Bangalore", "Chennai", "Mumbai", "Mangaluru"])
        Availability = st.selectbox("Availability", ["Yes", "No"])
    if st.button("Add Train Details"):
        add_data(Train_No, Name, Train_Type, Source, Destination, Availability)
        st.success("Successfully added Train with Number: {}".format(Train_No))