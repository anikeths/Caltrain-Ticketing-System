# -*- coding: utf-8 -*-
"""Caltrain Streamlit.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lY3rmkxwU7OUyh33owLAUchla3v094zr
"""

# Caltrain program with Streamlit



Stations_dictionary = dict({
            'Zone-1':['San Francisco','22nd Street','Bayshore','South San Francisco','San Bruno'],
             'Zone-2':['Millbrae Transit Center','Broadway','Burlingame','San Mateo','Hayward Park','Hillsdale','Belmont','San Carlos','Redwood City'],
             'Zone-3':['Menlo Park','Palo Alto','Stanford', 'California Ave.','San Antonio','Mountain View','Sunnyvale'],
             'Zone-4':['Lawrence','Santa Clara','College Park','San Jose Diridon','Tamien'],
            'Zone-5':['Capitol','Blossom Hill'],
            'Zone-6':['Morgan Hill','San Martin','Gilroy']
})

import streamlit as st
from PIL import  Image
image = Image.open('A Train.jpeg')
image = image.resize((800,1500))


col1, col2 = st.columns(2)

with col1:
    st.header('A-Train welcomes you aboard!')
    st.header('Our Mission: We present to you: ')
    st.header('Our Compound WE:')
    st.header('-Takes you forward!')
    st.header('-Makes sure that your HOMELANDing experience is safe and as fast as STARLIGHT itself.')

with col2 and col3:   
    st.image(image,caption = 'We take u forward!')
# st.image('https://www.cbr.com/the-boys-best-homelander-quotes/')

def getKey(dct,value):
  return [key for key in dct if (value in dct[key])]

try:
  entry_station = st.text_input('Enter your entry station')
except ValueError:
  st.error('Enter an input')

try:
  entry_zone=getKey(Stations_dictionary,entry_station)[0]
except IndexError:
  st.error('Enter an input')


try:
  exit_station = st.text_input('Enter your exit station')
except IndexError:
  st.error('Enter an input')

try:
 exit_zone = getKey(Stations_dictionary,exit_station)[0]
except IndexError:
  st.error('Enter an input')

# st.markdown(entry_zone,exit_zone)

# st.radio(label = 'Zone-1', options = ['R1','R2','R3'])
# st.radio(label = 'Zone-2', options = ['R1','R2','R3'])
# st.radio(label = 'Zone-2', options = ['R1','R2','R3'])
# st.radio(label = 'Zone-2', options = ['R1','R2','R3'])
# st.radio(label = 'Zone-2', options = ['R1','R2','R3'])
# st.radio(label = 'Zone-2', options = ['R1','R2','R3'])

# st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

price_dictionary = dict({'Zone-1': 1, 'Zone-2':2,'Zone-3':3,'Zone-4':4, 'Zone-5':5,'Zone-6':6})


zone_difference = abs(price_dictionary[entry_zone] - price_dictionary[exit_zone])
print(zone_difference)

ticket_price = 0
if zone_difference == 0:
  ticket_price = 3.75
elif zone_difference == 1:
  ticket_price = 6
elif zone_difference == 2:
  ticket_price = 8.25
elif zone_difference == 3:
  ticket_price = 10.5
elif zone_difference == 4:
  ticket_price = 12.75
elif zone_difference == 5:
  ticket_price = 15


# print(ticket_price)
st.markdown(ticket_price)

# !pip install streamlit


