import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import joblib

with open('pipe_RF1.pkl', 'rb') as model_file:
  bestgrid_RF = joblib.load(model_file) 


def run():
    
    with st.form(key='form_parameter'):
            Gender = st.selectbox('Gender', ('Female','Male'), index=1)
            age = st.number_input('Age', min_value=16, max_value=80, value=25, help = 'usia customer')
            Customer_Type = st.selectbox('Customer Type', ('Loyal Customer','disloyal Customer'), index=1)
            Type_of_Travel = st.selectbox('Type of Travel', ('Business travel','Personal Travel'), index=1)
            Class = st.selectbox('Class', ('Eco','Business', 'Eco Plus'), index=1)
            Flight_Distance = st.number_input('Flight Distance', min_value=0, max_value=100000,value=0)
            st.markdown('---')

            Inflight_wifi_service = st.number_input('Inflight wifi service',min_value=0,max_value=5, value=1, help= '0 = abstain, 1=Very Bad, 2=Bad, 3=Good, 4= Very Good, 5=Excellent ')
            Departure_or_Arrival_time_convenient = st.number_input('Departure/Arrival time convenient',min_value=0,max_value=5, value=1, help= '0 = abstain, 1=Very Bad, 2=Bad, 3=Good, 4= Very Good, 5=Excellent ')
            Ease_of_Online_booking = st.number_input('Ease of Online booking',min_value=0,max_value=5, value=1, help= '0 = abstain, 1=Very Bad, 2=Bad, 3=Good, 4= Very Good, 5=Excellent ')
            Gate_location = st.number_input('Gate location',min_value=0,max_value=5, value=1, help= '0 = abstain, 1=Very Bad, 2=Bad, 3=Good, 4= Very Good, 5=Excellent ')
            Food_and_drink = st.number_input('Food and drink',min_value=0,max_value=5, value=1, help= '0 = abstain, 1=Very Bad, 2=Bad, 3=Good, 4= Very Good, 5=Excellent ')
            Online_boarding = st.number_input('Online boarding',min_value=0,max_value=5, value=1, help= '0 = abstain, 1=Very Bad, 2=Bad, 3=Good, 4= Very Good, 5=Excellent ')
            Seat_comfort = st.number_input('Seat comfort',min_value=0,max_value=5, value=1, help= '0 = abstain, 1=Very Bad, 2=Bad, 3=Good, 4= Very Good, 5=Excellent ')
            st.markdown('---')

            Inflight_entertainment = st.number_input('Inflight entertainment',min_value=0,max_value=5, value=1, help= '0 = abstain, 1=Very Bad, 2=Bad, 3=Good, 4= Very Good, 5=Excellent ')
            On_board_service = st.number_input('On-board service',min_value=0,max_value=5, value=1, help= '0 = abstain, 1=Very Bad, 2=Bad, 3=Good, 4= Very Good, 5=Excellent ')
            Leg_room_service = st.number_input('Leg room service',min_value=0,max_value=5, value=1, help= '0 = abstain, 1=Very Bad, 2=Bad, 3=Good, 4= Very Good, 5=Excellent ')
            Baggage_handling = st.number_input('Baggage handling',min_value=0,max_value=5, value=1, help= '0 = abstain, 1=Very Bad, 2=Bad, 3=Good, 4= Very Good, 5=Excellent ')
            Checkin_service = st.number_input('Checkin_service',min_value=0,max_value=5, value=1, help= '0 = abstain, 1=Very Bad, 2=Bad, 3=Good, 4= Very Good, 5=Excellent ')
            Inflight_service = st.number_input('Inflight service',min_value=0,max_value=5, value=1, help= '0 = abstain, 1=Very Bad, 2=Bad, 3=Good, 4= Very Good, 5=Excellent ')
            Cleanliness = st.number_input('Cleanliness',min_value=0,max_value=5, value=1, help= '0 = abstain, 1=Very Bad, 2=Bad, 3=Good, 4= Very Good, 5=Excellent ')
            st.markdown('---')

            Departure_Delay_in_Minutes = st.number_input('Departure Delay in Minutes', min_value=0, max_value=5000, value=60, help = 'in minutes')
            Arrival_Delay_in_Minutes = st.number_input('Arrival Delay in Minutes', min_value=0, max_value=5000, value=60, help = 'in minutes')
            st.markdown('---')

            submitted= st.form_submit_button('Predict')

    data_inf = {
            'Gender': Gender,
            'Age': age,
            'Customer Type': Customer_Type,
            'Type of Travel': Type_of_Travel,
            'Class': Class,
            'Flight Distance': Flight_Distance,
            'Inflight wifi service': Inflight_wifi_service,
            'Departure/Arrival time convenient': Departure_or_Arrival_time_convenient,
            'Ease of Online booking': Ease_of_Online_booking,
            'Gate location': Gate_location,
            'Food and drink': Food_and_drink,
            'Online boarding': Online_boarding,
            'Seat comfort': Seat_comfort,
            'Inflight entertainment': Inflight_entertainment,
            'On-board service': On_board_service,
            'Leg room service': Leg_room_service,
            'Baggage handling': Baggage_handling,
            'Checkin service': Checkin_service,
            'Inflight service': Inflight_service,
            'Cleanliness': Cleanliness,
            'Departure Delay in Minutes': Departure_Delay_in_Minutes,
            'Arrival Delay in Minutes': Arrival_Delay_in_Minutes,
    }

    data_inf = pd.DataFrame([data_inf])
    st.dataframe(data_inf)

    if submitted:
            
         y_pred_inf_RF = bestgrid_RF.predict(data_inf)
         

         st.write('## RATING : ' + str(int(y_pred_inf_RF)))
if __name__ == '__main__':
    run()