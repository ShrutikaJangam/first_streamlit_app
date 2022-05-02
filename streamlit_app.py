import streamlit
streamlit.title('My Mom\'s New Healthy Dinner')
streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 and Blueberry Oatmeal')
streamlit.text('🥗 kale,Spinach and Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free Range Egg')
streamlit.text('🥑🍞 Avocado Toast')
streamlit.header(' 🍌🥭 Build Your Own Fruit Smoothie 🥝🍇') 
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('fruit')
#let's pick a fruit list here so they can pick fruit they want to include
streamlit.multiselect("Pick some fruits:",list(my_fruit_list.index))
#display the table on the page
streamlit.dataframe(my_fruit_list)
