import streamlit as st
import pickle
import sklearn
import pandas as pd
import numpy as np
from PIL import Image
model = pickle.load(open('model.pkl', 'rb'))

st.title('NBA Player Salary Prediction')
st.sidebar.header('Player Data')
image = Image.open('bb.jpg')
st.image(image, '')

# FUNCTION
def user_report():
  rating = st.sidebar.slider('Rating', 67,100, 67 )


  team_mapping = {
    'Brooklyn Nets': 0,
    'Los Angeles Clippers': 1,
    'Los Angeles Lakers': 2,
    'Indiana Pacers': 3,
    'Milwaukee Bucks': 4,
    'Philadelphia 76ers': 5,
    'Orlando Magic': 6,
    'New Orleans Pelicans': 7,
    'New York Knicks': 8,
    'Chicago Bulls': 9,
    'Toronto Raptors': 10,
    'Minnesota Timberwolves': 11,
    'Houston Rockets': 12,
    'Memphis Grizzlies': 13,
    'Detroit Pistons': 14,
    'Sacramento Kings': 15,
    'Phoenix Suns': 16,
    'Miami Heat': 17,
    'San Antonio Spurs': 18,
    'Atlanta Hawks': 19,
    'Denver Nuggets': 20,
    'Golden State Warriors': 21,
    'Dallas Mavericks': 22,
    'Boston Celtics': 23,
    'Portland Trail Blazers': 24,
    'Washington Wizards': 25,
    'Oklahoma City Thunder': 26,
    'Cleveland Cavaliers': 27,
    'Utah Jazz': 28,
    'Charlotte Hornets': 29
}
  # Dropdown for 'Team'
  team_options = ['Brooklyn Nets',
    'Los Angeles Clippers',
    'Los Angeles Lakers',
    'Indiana Pacers',
    'Milwaukee Bucks',
    'Philadelphia 76ers',
    'Orlando Magic',
    'New Orleans Pelicans',
    'New York Knicks',
    'Chicago Bulls',
    'Toronto Raptors',
    'Minnesota Timberwolves',
    'Houston Rockets',
    'Memphis Grizzlies',
    'Detroit Pistons',
    'Sacramento Kings',
    'Phoenix Suns',
    'Miami Heat',
    'San Antonio Spurs',
    'Atlanta Hawks',
    'Denver Nuggets',
    'Golden State Warriors',
    'Dallas Mavericks',
    'Boston Celtics',
    'Portland Trail Blazers',
    'Washington Wizards',
    'Oklahoma City Thunder',
    'Cleveland Cavaliers',
    'Utah Jazz',
    'Charlotte Hornets']
  # team = st.sidebar.selectbox('Team', team_options, format_func=lambda x: team_mapping[x])
  team_sel = st.sidebar.selectbox('Team', list(team_mapping.keys()))
  team = team_mapping[team_sel]


  position_mapping = {'G':0, 'F':1, 'C':2, 'F-C':3, 'G-F':4, 'F-G':5, 'C-F':6}
  postion_options = ['G', 'F', 'C', 'F-C', 'G-F', 'F-G', 'C-F']
  position_sel = st.sidebar.selectbox('Position', list(position_mapping.keys()))
  position = position_mapping[position_sel]

  # country = st.sidebar.slider('Country', 0,3, 1 )
  country_mapping = {"USA":0, "OTHERS":1, "CANADA":2, "AUSTRALIA":3}
  country_options = ['USA','OTHERS','CANADA','AUSTRALIA']
  country_sel = st.sidebar.selectbox('Country', list(country_mapping.keys()))
  country = country_mapping[country_sel]

  weight = st.sidebar.slider("Height",170,284,180)
  height = st.sidebar.slider("Height",177,218,180)


  user_report_data = {
      'rating':rating,
      'team':team,
      'position':position,
      'height':height,
      'weight':weight,
      'country':country
  }
  report_data = pd.DataFrame(user_report_data, index=[0])
  return report_data

user_data = user_report()
st.header('Player Data')
st.write(user_data)

salary = model.predict(user_data)
st.subheader('Predicted Player Salary')
st.subheader('$'+str(np.round(salary[0], 2)))