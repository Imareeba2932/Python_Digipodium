import streamlit as st

msgbox=st.empty()

t1, t2, t3=st.tabs(['About', 'Dataset', 'Visualization'])

t1.text('This is a Sample Text')
name=t1.text_input('Enter your Name')
if t1.button('Submit'):
    t2.write(f'You are known as, {name}')

with st.expander("This is Something Secret, Please don't click"):
    data=[1,3,5,3,5,1,2,2,2,1]
    st.bar_chart(data)

msgbox.text('Enter your Name in the First tab')
