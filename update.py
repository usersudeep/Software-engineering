import pandas as pd
import streamlit as st
from database import view_all_data, view_only_train_number, edit_dealer_data


def update():
    result = view_all_data()
    # st.write(result) 
    df = pd.DataFrame(result, columns=["Train_No", "Name", "Train_Type", "Source", "Destination", "Availability"]) 
    with st.expander("Current Trains with availabilities"):
        st.dataframe(df)
    list_of_trains = [i[0] for i in view_only_train_number()]
    selected_train = st.selectbox("train to Edit", list_of_trains)
    # selected_result = get_dealer(selected_dealer)
    # st.write(selected_result)
    if selected_train:
        # Layout of Create
        if st.button("Update Train's Availability"):
            edit_dealer_data('Yes', selected_train)
            st.success("Successfully updated Availability of train :: {} to :: {}".format(selected_train, 'Yes'))

    result2 = view_all_data()
    df2 = pd.DataFrame(result2, columns=["Train_No", "Name", "Train_Type", "Source", "Destination", "Availability"])
    with st.expander("Updated Train data"):
        st.dataframe(df2)