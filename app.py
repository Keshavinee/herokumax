import streamlit as st
st.write("""
# Maximum of three numbers
""")
a=st.number_input('Enter Number 1:')
b=st.number_input('Enter Number 2:')
c=st.number_input('Enter Number 3:')

maximum = a
if b>maximum:
	maximum = b
if c>maximum:
	maximum = c
	
if st.button('Maximum value'):
	st.write(maximum)
