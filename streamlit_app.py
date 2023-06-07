import streamlit as st

def main():
     st.write("testando app")
     if st.button('Say hello'):

         st.write('Why hello there')
     else:
         st.write('Goodbye')

main()
