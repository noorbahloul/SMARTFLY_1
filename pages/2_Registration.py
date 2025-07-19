
# ---------------------------------------------------------
#                   REGISTRATION CODE 
# ---------------------------------------------------------

import streamlit as st 
import datetime 


st.header('   Registraition Tabs :    :memo: :white_check_mark:')

tab1,tab2 = st.tabs([" PERSONEL INFORMATIONS "," FLIGHT DETAILS  "])

# ---------------------------------------------------------
#              INPUT PERSONEL INFORMATIONS 
# ---------------------------------------------------------
with tab1 :
    st.write (" please enter your informations :")
    Firstname = st.text_input (" enter your firstname :")
    Lastname = st.text_input (" enter your lastname :")
    Age = st.slider('enter your age : ' ,0,130,25)

    button1 = st.button (" confirm .", key="confirm_button_1")
    if button1 == True :
        st.write(f'Welcome {Firstname} {Lastname} on SMARTFLY , pleaseswitch to the next tab. ')


# ---------------------------------------------------------
#                  INPUT FIGHT DETAILS      
# ---------------------------------------------------------
with tab2 :
     # ---------------------------------------------------------
     #                   DEPARTURE AND DESTINATION 
     # ---------------------------------------------------------
    st.write (" FROM > TO  :")
    airports = [
                                # Algerian Airports
    "Algiers Houari Boumediene Airport, Algiers",
    "Oran Ahmed Ben Bella Airport, Oran",
    "Constantine Mohamed Boudiaf Airport, Constantine",
    "Annaba Rabah Bitat Airport, Annaba",
    "Tlemcen Zenata – Messali El Hadj Airport, Tlemcen",
    "Béjaïa Soummam – Abane Ramdane Airport, Béjaïa",
    "Ghardaïa Noumérat Moufdi Zakaria Airport, Ghardaïa",
    "Tamanrasset Aguenar – Hadj Bey Akhamok Airport, Tamanrasset",
    "Hassi Messaoud Oued Irara – Krim Belkacem Airport, Hassi Messaoud",
    "Batna Mostéfa Ben Boulaid Airport, Batna",
                                # Middle Eastern Airports
    "Dubai International Airport, Dubai",
    "Doha Hamad International Airport, Doha",
    "King Khalid International Airport, Riyadh",
    "King Abdulaziz International Airport, Jeddah",
    "Beirut Rafic Hariri International Airport, Beirut",
    "Kuwait International Airport, Kuwait City",
    "Muscat International Airport, Muscat",
    "Queen Alia International Airport, Amman",
    "Baghdad International Airport, Baghdad",
    "Bahrain International Airport, Manama",
                                 # European Airports
    "Paris Charles de Gaulle Airport, Paris",
    "Frankfurt Airport, Frankfurt",
    "Amsterdam Schiphol Airport, Amsterdam",
    "Madrid-Barajas Adolfo Suárez Airpor, Madrid",
    "Rome Leonardo da Vinci–Fiumicino Airport, Rome",
    "London Heathrow Airport, London",
    "Vienna International Airport, Vienna",
    "Brussels Airport, Brussels",
    "Zurich Airport, Zurich",
    "Istanbul Airport, Istanbul"
    ] 
    DEPARTURE = st.selectbox (' enter your departure airport :   ' , options=airports)
    DESTINATION = st.selectbox (' enter your destination airport : ' , options=airports)

     # ---------------------------------------------------------
     #           DEPARTURE AND DESTINATION DATES 
     # ---------------------------------------------------------
    st.write (" select departure and return day :")
    DEPARTUREDAY = st.date_input (" enter the departure day  :")
    RETURNDAY = st.date_input (" enter return day  :")

     # ---------------------------------------------------------
     #                   PRIORITY OPTIONS 
     # ---------------------------------------------------------
    st.write (" choose which standard you prioritize or prefer  :")
    button_A = st.button ("SPEED ")
    if button_A == True :  
       st.write("1_Transavia : Popular low-cost airline in Europe and North Africa")
       st.write("2_Vueling : Spanish budget carrier serving Europe and North Africa")
       st.write ("3_ easyJet: Major European low-cost airline with wide route network")
       st.write(" 4_Wizz Air: Low-cost carrier focused on Central, Eastern & Southern Europe")
       st.write(" 5_Pegasus Airlines : Turkish budget airline flying Europe-Middle East routes")
       st.write(" 6_Flydubai: Dubai-based low-cost airline operating Middle East & regional flights")
    button_B = st.button ("COMFORT ")
    if button_B == True :  
       st.write("1_Emirates: Renowned for luxury, spacious cabins, and excellent service.")
       st.write("2_Qatar Airways: An award-winning airline with premium cabins and great comfort.")
       st.write ("3_Turkish Airlines: Provides high service standards with comfortable economy and business class options ")
       st.write("4_Air France: Brings French elegance with good comfort and lounges.")
       st.write("5_British Airways: Offers strong premium cabins and good onboard comfort.")
    button_C = st.button ("SPEED")
    if button_C == True :  
       st.write("1_Air France — Efficient transcontinental routes, especially between Europe and North America/Africa.")
       st.write("2_Turkish Airlines — Large network with modern fleet, often offering direct flights cutting down travel time .")
       st.write ("3_Emirates — Operates modern aircraft like the Airbus A380 and Boeing 777, known for efficient routes and quick turnaround times.")
       st.write("4_Qatar Airways — Flies long-haul routes with the Boeing 777 and Airbus A350, noted for fast and efficient services.")
       st.write("5_British Airways — Known for fast transatlantic routes and short connection times.")
     
    st.write("to get more informations about airlines check the link bellow : ")
    button_D = st.link_button( "links  " , "https://www.airlines-inform.com" )
    st.write(" after you had a look on recommended airlines ,choose one : ")
    AIRLINE = st.text_input ("enter airline name : ")

    
     # ---------------------------------------------------------
     #                      LUGGGAGE 
     # ---------------------------------------------------------
    radio = st.radio( "do you have carry on  : " , ( "YES" , "NO" , "STILL NOT CONFERM "  ))
    LUGGGAGE = st.slider('how much weight do you carry  : ' ,0,30,10)
    st.write (" you can not carry more than 20 kg or you will have to pay extra money for the extra weight .")
    
    button2 = st.button (" confirm .", key="confirm_button_2")
    if button2 == True :
        st.write (f'You’re flying from {DEPARTURE} to {DESTINATION} with { AIRLINE } Good choice!   :white_check_mark:   ')
    else :
        st.write("check again !")
