

# ---------------------------------------------------------
#                DEFINITION FOR THE APP 
# ---------------------------------------------------------

import streamlit as st 
selectbox = st.selectbox( "choose how would you like to be contact : " , ( "email" , "phone " ))
contact = st.text_input("")
