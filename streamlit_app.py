import streamlit
import pandas

streamlit.header('🥗 Breakfast Menu')
streamlit.text('Omega 3 & Blueberry Oatmeal')
streamlit.text('Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list= pandas.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')

fruit_selected=streamlit.multiselect("Pick Some Fruits:",list(my_fruit_list.index))
fruit_to_show=my_fruit_list.loc[fruit_selected]
streamlit.dataframe(fruit_to_show)

import requests
streamlit.header("Fruityvice Fruit Advice!")

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response.json())
# normalize the json data in tbl format
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# display the normalized data
streamlit.dataframe(fruityvice_normalized)
