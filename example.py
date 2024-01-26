import pandas as pd
import streamlit as st
import plotly.express as px

data = pd.read_csv('/Users/sharo/OneDrive/Desktop/vehicles_us.csv')
data.info()
print(data.head)
print(data['price'].describe())

data = pd.read_csv('/Users/sharo/OneDrive/Desktop/vehicles_us.csv')
import plotly.express as px

import streamlit as st
st.title('Choose your car')
st.subheader('Use this app to select great car based on your preferences')

import urllib.request
from PIL import Image

urllib.request.urlretrieve(
    'https://images.drive.com.au/driveau/image/upload/c_fill,f_auto,g_auto,h_1080,q_auto:eco,w_1920/v1/cms/uploads/pkkkhkljf7tvzitqzs6u', 
    'image.jpg')
img = Image.open("image.jpg")

st.image(img)

st.caption(':red[Choose your parametr here]')


price_range = st.slider(
    "what is your price range?",
    value=(100000,375000))

actual_range = [100000, 375000]

high_rating=st.checkbox('Only high rating')

data = pd.read_csv('/Users/sharo/OneDrive/Desktop/vehicles_us.csv')

if high_rating:
    filtered_data=data[data.price.isin(actual_range)]
    filtered_data=filtered_data[data_rating>= 1.50000]
else:
    filtered_data = data[data['price'].isin(actual_range)]
    
    st.write('Here are your options with a split by price and condition')
    
    fig = px.scatter(filtered_data, x="price", y="condition")
    st.plotly_chart(fig)

