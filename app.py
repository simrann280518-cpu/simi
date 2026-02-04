import streamlit as st

st.title("hi ishu" )

st.write("beta")

age =st.slider("select the age" , 1 ,100)

if st.button("select"):
    st.write("simran fauji" , age )