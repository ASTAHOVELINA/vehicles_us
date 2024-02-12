import pandas as pd
import streamlit as st
import plotly.express as px

data=pd.read_csv('vehicles_us.csv')
data.info()
print(data.head)
print(data['price'].describe())

import plotly.express as px

st.title('Choose your car')
st.subheader('Use this app to select great car based on your preferences')

import urllib.request
from PIL import Image
urllib.request.urlretrieve(
  'https://hips.hearstapps.com/hmg-prod/images/10best-cars-group-cropped-1542126037.jpg',
   "gfg.png")
  
img = Image.open("gfg.png")

st.image(img)
st.caption(':red[Choose your parametr here]')


price_range = st.slider(
    "what is your price range?",
    value=(1,375000))

actual_range=list(range(price_range[0],price_range[1]+1))

model_year=st.checkbox('Only cars after 2018')


if model_year:
    filtered_data=data[data.price.isin(actual_range)]
    filtered_data=filtered_data[filtered_data['model_year']>= 2018]
else:
    filtered_data = data[data['price'].isin(actual_range)]
st.write('Here are your options with a split by price and condition')
fig = px.scatter(filtered_data, x="price", y="condition")
st.plotly_chart(fig)

#Conclusion from the scatterplot with a split by price and condition
st.write('Conclusion about the depandancy of price from condition:')
st.write('1) Absolute majority of the cars with new, like new, excellent and good condition have pretty much the same prices')
st.write('2) The prices for new, like new, excellent and good condition cars are mostly less then 60 000 $')
st.write('3) The prices for salvage and fair condition cars are mostly less then 20 000 $')

#Histogram showing the average price by model
fig2 = px.histogram(filtered_data, title="Average price by model", x="price", color='condition')
st.plotly_chart(fig2)


st.write('Conclusion about the average prices by the model:')
st.write('1) The average prices of most of the models are below 10 000 $')
st.write('2) The most expensive model is Mercedes-benz Sprinter 2500 with the average price of 34900$')
st.header('Overall Conclusion')
st.write('We have tested the following three hypotheses:')
st.write('1) The prices of the cars are strongly dependent on the car condition')
st.write('2) There majority of cars are in the middle price range ')
st.header('After analyzing the data, we concluded:')
st.write('1) There is a dependancy of price from condition.') 
st.write('Although cars with new, like new, excellent and good condition have aproximately the same price range from 1 to 60 000 $.')
st.write('The prices for salvage and fair condition cars are much lower and mostly less then 20 000 $')
st.write('So, the first hypotheses is approved.')
st.write('2) The average prices of most of the models are below 10 000 $.')
st.write('The middle price is 12 132 $.')
st.write('So we need to conclude that the second hypotheses is not right and the average car price is lower then the middle price range.')
