import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt



def run():
    #tittle
    st.title('Exploratory Data Analysis')
    #subheader
    st.subheader('EDA For Analyst Dataset Airline Satifaction')

    #description
    st.write('This page made by Didit eko')

    #garis lurus
    st.markdown('---')

    #magic syntax
    '''
    Pada page kali ini, penulis ingin membuat analisa prediksi kenyamanan penumpang terhadap airline.
    Dataset yang digunakan adalah Airline Satisfaction, dan berasal dari Kaggle.com
    '''

    #show datafram
    df = pd.read_csv('airline.csv')
    st.dataframe(df)

    #histo
    st.write('### Satisfaction Historam')
    satisfaction = df.groupby(['satisfaction'])[['satisfaction']].count()
    satisfaction.plot(kind='bar', figsize=(10,6), color='darkorange')
    plt.xlabel('satifaction')
    plt.ylabel('data count')
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot()

    #histo
    st.write('### Gender')
    fig = plt.figure(figsize=(10,7))
    sns.countplot('Gender', hue= 'satisfaction', data=df, palette='husl')
    st.pyplot(fig)

    # show his type customer
    st.write('### Customer Type')
    fig = plt.figure(figsize=(12,7))
    sns.countplot('Customer Type', hue= 'satisfaction', data=df, palette='seismic_r')
    st.pyplot(fig)

    #Type of Travel
    st.write('### Type of Travel')
    fig = plt.figure(figsize=(12,7))
    sns.countplot('Type of Travel', hue= 'satisfaction', data=df, palette='Set1_r')
    st.pyplot(fig)

    # show his class
    st.write('### Class')
    fig = plt.figure(figsize=(12,7))
    sns.countplot('Class', hue= 'satisfaction', data=df, palette='Set1')
    st.pyplot(fig)

    # show his type age
    st.write('### Age')
    fig = plt.figure(figsize=(20,10))
    sns.countplot('Age', hue= 'satisfaction', data=df, palette='spring_r')
    st.pyplot(fig)

    # Inflight wifi service
    st.write('### Inflight wifi service')
    wifi=df[['Inflight wifi service']].groupby(['Inflight wifi service']).size().sort_values(ascending=False).reset_index()
    wifi.plot(kind='pie',y=0, autopct='%1.1f%%',  title = "Inflight wifi service",
    startangle=50, shadow=False, cmap='cool', labels=wifi['Inflight wifi service'], legend = False, fontsize=14, figsize=(8, 8))
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot()

    # pie chart column time convenient
    st.write('### Departure/Arrival time convenient')
    convenient = df.groupby(['Departure/Arrival time convenient'])[['Departure/Arrival time convenient']].count()
    convenient.plot(kind='pie',y=0, autopct='%1.1f%%', startangle=90, shadow=False, legend= False, figsize=(8, 8), cmap='plasma_r')      
    plt.title('Departure/Arrival time convenient')
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot()

    # pie chart column ease online booking
    st.write('### Ease of Online booking')
    booking = df.groupby(['Ease of Online booking'])[['Ease of Online booking']].count()
    booking.plot(kind='pie',y=0, autopct='%1.1f%%', startangle=90, shadow=False, legend= False, figsize=(8, 8), cmap='rainbow_r')      
    plt.title('Ease of Online booking')
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot()

    # pie chart column
    st.write('### Pie Chart Columns')
    gate = df.groupby(['Gate location'])[['Gate location']].count()
    food = df.groupby(['Food and drink'])[['Food and drink']].count()
    boarding = df.groupby(['Online boarding'])[['Online boarding']].count()
    clean = df.groupby(['Cleanliness'])[['Cleanliness']].count()
    fig = plt.figure(figsize=(26, 5))

    plt.subplot(1,4,1)
    gate.iloc[:,0].plot(kind='pie', autopct='%1.1f%%', startangle=90, shadow=False, cmap='YlGnBu')      
    plt.title('Gate location')
    plt.ylabel('')
    plt.axis('equal') # Sets the pie chart to look like a circle.

    plt.subplot(1,4,2)
    food.iloc[:,0].plot(kind='pie', autopct='%1.1f%%', startangle=90, shadow=False, cmap='spring_r')      
    plt.title('Food and drink')
    plt.ylabel('')
    plt.axis('equal') # Sets the pie chart to look like a circle.

    plt.subplot(1,4,3)
    boarding.iloc[:,0].plot(kind='pie', autopct='%1.1f%%', startangle=90, shadow=False, cmap='summer')      
    plt.title('Online boarding')
    plt.ylabel('')
    plt.axis('equal') # Sets the pie chart to look like a circle.

    plt.subplot(1,4,4)
    clean.iloc[:,0].plot(kind='pie', autopct='%1.1f%%', startangle=90, shadow=False, cmap='cool_r')      
    plt.title('Cleanliness')
    plt.ylabel('')
    plt.axis('equal') # Sets the pie chart to look like a circle.
    st.pyplot(fig)

    # pie chart column
    st.write('### Pie Chart Columns')
    seat = df.groupby(['Seat comfort'])[['Seat comfort']].count()
    entertaiment = df.groupby(['Inflight entertainment'])[['Inflight entertainment']].count()
    on_board = df.groupby(['On-board service'])[['On-board service']].count()
    fig = plt.figure(figsize=(26, 5))

    plt.subplot(1,3,1)
    seat.iloc[:,0].plot(kind='pie', autopct='%1.1f%%', startangle=90, shadow=False, cmap='magma')      
    plt.title('Seat comfort')
    plt.ylabel('')
    plt.axis('equal') # Sets the pie chart to look like a circle.

    plt.subplot(1,3,2)
    entertaiment.iloc[:,0].plot(kind='pie', autopct='%1.1f%%', startangle=90, shadow=False, cmap='viridis')      
    plt.title('Inflight entertainment')
    plt.ylabel('')
    plt.axis('equal') # Sets the pie chart to look like a circle.

    plt.subplot(1,3,3)
    on_board.iloc[:,0].plot(kind='pie', autopct='%1.1f%%', startangle=90, shadow=False, cmap='winter')      
    plt.title('On-board service')
    plt.ylabel('')
    plt.axis('equal') # Sets the pie chart to look like a circle.
    st.pyplot(fig)

    # pie chart column
    st.write('### Pie Chart Columns')
    leg = df.groupby(['Leg room service'])[['Leg room service']].count()
    bagage = df.groupby(['Baggage handling'])[['Baggage handling']].count()
    checkin = df.groupby(['Checkin service'])[['Checkin service']].count()
    inflight = df.groupby(['Inflight service'])[['Inflight service']].count()

    fig = plt.figure(figsize=(26, 5))

    plt.subplot(1,4,1)
    leg.iloc[:,0].plot(kind='pie', autopct='%1.1f%%', startangle=90, shadow=False, cmap='winter_r')      
    plt.title('Leg room service')
    plt.ylabel('')
    plt.axis('equal') # Sets the pie chart to look like a circle.

    plt.subplot(1,4,2)
    bagage.iloc[:,0].plot(kind='pie', autopct='%1.1f%%', startangle=90, shadow=False, cmap='PuRd')      
    plt.title('Baggage handling')
    plt.ylabel('')
    plt.axis('equal') # Sets the pie chart to look like a circle.

    plt.subplot(1,4,3)
    checkin.iloc[:,0].plot(kind='pie', autopct='%1.1f%%', startangle=90, shadow=False, cmap='Purples')      
    plt.title('Checkin service')
    plt.ylabel('')
    plt.axis('equal') # Sets the pie chart to look like a circle.

    plt.subplot(1,4,4)
    inflight.iloc[:,0].plot(kind='pie', autopct='%1.1f%%', startangle=90, shadow=False, cmap='RdYlGn')      
    plt.title('Inflight service')
    plt.ylabel('')
    plt.axis('equal') # Sets the pie chart to look like a circle.
    st.pyplot(fig)

    #Delay
    st.write('### Departure Delay vs arrival Delay')
    fig = plt.figure(figsize=(10,9))
    sns.scatterplot(x='Departure Delay in Minutes', y='Arrival Delay in Minutes', hue = 'satisfaction', data=df)
    plt.title('Departure Delay vs arrival Delay')
    st.pyplot(fig)

if __name__ == '__main__':
    run()