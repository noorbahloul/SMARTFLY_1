
# ---------------------------------------------------------
#                TRAVEL TIPS DISPLAY CODE 
# ---------------------------------------------------------
import streamlit as st
import random 
st.header(' TRAVEL TIPS AND TRICS   :heavy_check_mark:  :hourglass:   ')
tips= [
                        "Arrive at the airport at least 2 to 3 hours before your flight.",

                        "Keep your passport, ticket, and ID in an easy-to-reach place.",

                        "Label your luggage with your name and contact information.",

                        "Pack light and follow the baggage rules (weight and size).", 

                        "Keep important items (money, phone, charger) in your carry-on.",

                        "Wear comfortable clothes and shoes for long flights.",

                        "Stay hydrated – drink water during the flight.",

                        "Avoid heavy meals before flying to feel better in the air.",

                        "Bring a neck pillow and earplugs for comfort during the flight.",

                        "Follow the airline safety rules and listen to the crew."

                         ]
        
random_tips = random.sample(tips,1)           
with st.expander('TIPS AND TRICS ') :
    with st.container (border=True) :
         st.subheader ("this expander  offers you some essentiel tips and trics to ensure a safe efficient and comfortebl flight : ")
         button = st.button("tip")
         if button==True :
            for tip in random_tips:
              st.write ( {tip}) 
         else :
             st.write (" click to pick .")

