import streamlit as st
st.title("Моето първо Streamlit приложение")
name = st.text_input("Как се казваш?")
if name:
   st.write(f"Здравей, {name}!")
date = st.number_input("На колко години си?")


