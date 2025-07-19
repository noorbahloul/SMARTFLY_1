
# ---------------------------------------------------------
#                DEFINITION FOR THE APP 
# ---------------------------------------------------------
import streamlit as st 
st.header('what is SMARTFLY   :question:      ')
st.write (" click on the button to get the answer .")
button = st.button(" answer !" )
if button == True : 
   st.write("Smartfly is a simple website app created using python and streamlit ,it is designed to simulate choosing flight details ,get the definition of commen aviation terms and tips and trics to ensure safe and well orgnized flight.")
