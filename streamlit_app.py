import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.header('🥗 Breakfast Menu')
streamlit.text('Omega 3 & Blueberry Oatmeal')
streamlit.text('Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list= pandas.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')

fruit_selected=streamlit.multiselect("Pick Some Fruits:",list(my_fruit_list.index))
fruit_to_show=my_fruit_list.loc[fruit_selected]
streamlit.dataframe(fruit_to_show)


#import requests
def get_fruityvice_data(this_fruit_choice):
   fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
   fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
   return fruityvice_normalized
  
streamlit.header("Fruityvice Fruit Advice!")
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error("Please select a fruit to get information")
  else:
    back_from_function=get_fruityvice_data(fruit_choice)
    streamlit.dataframe(back_from_function)
   
except URLError as e:
  streamlit.error()



# normalize the json data in tbl format

# display the normalized data

fruit_choice = streamlit.text_input('What fruit would you like information about?','Jackfruit')
streamlit.stop()
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("insert into fruit_load_list values ('from streamlit')")
my_data_row = my_cur.fetchall()
streamlit.text("Table data")
streamlit.text(my_data_row)
