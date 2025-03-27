import streamlit as st
import langchain_helper

st.title("Restaurant Name Generator")
cuisine = st.sidebar.selectbox("Pick a Cuisine", ("Indian","Italian","Mexican","Arabic","American"))



if cuisine:
    response = langchain_helper.generate_restaurant_name_and_items(cuisine)
    st.header(response['restaurant_name'].strip())
    menu_item = response['menu_items'].strip().split(",")
    st.write("**Menu Items**")
    for item in menu_item:
        st.write("-", item)
