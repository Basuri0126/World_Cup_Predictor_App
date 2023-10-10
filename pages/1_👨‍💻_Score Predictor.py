import pandas as pd
import streamlit as st
import pickle


st.set_page_config(layout='wide')


# Load the pre-trained model
pipe1 = pickle.load(open('pipeline_for_score_pred.pkl', 'rb'))

teams = [
    'Australia',
    'India',
    'Bangladesh',
    'New Zealand',
    'South Africa',
    'England',
    'Netherlands',
    'Afghanistan',
    'Pakistan',
    'Sri Lanka',
    'Scotland',
    'Zimbabwe',
    'West Indies',
    'Ireland',
    'Nepal'
]

cities = ['Abu Dhabi',
          'Adelaide',
          'Ahmedabad',
          'Antigua',
          'Auckland',
          'Bangalore',
          'Barbados',
          'Belfast',
          'Bengaluru',
          'Benoni',
          'Birmingham',
          'Bloemfontein',
          'Bogra',
          'Brisbane',
          'Bristol',
          'Bulawayo',
          'Canberra',
          'Canterbury',
          'Cape Town',
          'Cardiff',
          'Centurion',
          'Chandigarh',
          'Chennai',
          'Chester-le-Street',
          'Chittagong',
          'Christchurch',
          'Colombo',
          'Cuttack',
          'Darwin',
          'Delhi',
          'Dhaka',
          'Dharamshala',
          'Dubai',
          'Dublin',
          'Dunedin',
          'Durban',
          'East London',
          'Faisalabad',
          'Faridabad',
          'Fatullah',
          'Grenada',
          'Guwahati',
          'Guyana',
          'Gwalior',
          'Hambantota',
          'Hamilton',
          'Harare',
          'Hobart',
          'Hyderabad',
          'Indore',
          'Jaipur',
          'Jamaica',
          'Jamshedpur',
          'Johannesburg',
          'Kanpur',
          'Karachi',
          'Kimberley',
          'Kochi',
          'Kolkata',
          'Kuala Lumpur',
          'Lahore',
          'Leeds',
          'London',
          'Lucknow',
          'Manchester',
          'Margao',
          'Melbourne',
          'Mirpur',
          'Mount Maunganui',
          'Multan',
          'Mumbai',
          'Nagpur',
          'Napier',
          'Nelson',
          'Nottingham',
          'Paarl',
          'Pallekele',
          'Perth',
          'Peshawar',
          'Port Elizabeth',
          'Potchefstroom',
          'Pune',
          'Queenstown',
          'Rajkot',
          'Ranchi',
          'Rangiri',
          'Rawalpindi',
          'Sharjah',
          'Southampton',
          'St Kitts',
          'St Lucia',
          'Sydney',
          'Taunton',
          'Trinidad',
          'Vadodara',
          'Visakhapatnam',
          'Wellington']

stadium = ['Adelaide Oval', "Antigua Recreation Ground, St John's",
           'Arbab Niaz Stadium', 'Arnos Vale Ground, Kingstown',
           'Arun Jaitley Stadium', 'Bangabandhu National Stadium',
           'Barabati Stadium', 'Barsapara Cricket Stadium', 'Basin Reserve',
           'Bay Oval', 'Beausejour Stadium, Gros Islet', 'Bellerive Oval',
           'Bharat Ratna Shri Atal Bihari Vajpayee Ekana Cricket Stadium',
           'Boland Park', 'Brabourne Stadium',
           'Bready Cricket Club, Magheramason',
           'Brisbane Cricket Ground, Woolloongabba', 'Buffalo Park',
           'Bulawayo Athletic Club', 'Cambusdoon New Ground',
           'Captain Roop Singh Stadium', 'Castle Avenue', 'Chevrolet Park',
           'Chittagong Divisional Stadium',
           'Civil Service Cricket Club, Stormont',
           'Clontarf Cricket Club Ground', 'Cobham Oval (New)',
           'County Ground',
           'Daren Sammy National Cricket Stadium, Gros Islet',
           'Darren Sammy National Cricket Stadium, Gros Islet',
           'Darren Sammy National Cricket Stadium, St Lucia',
           'De Beers Diamond Oval', 'Diamond Oval', 'Docklands Stadium',
           'Dr. Y.S. Rajasekhara Reddy ACA-VDCA Cricket Stadium',
           'Dubai International Cricket Stadium', 'Eden Gardens', 'Edgbaston',
           'Fatorda Stadium', 'Gaddafi Stadium',
           'Galle International Stadium', 'Goodyear Park',
           'Grange Cricket Club Ground, Raeburn Place',
           'Grange Cricket Club, Raeburn Place',
           'Greater Noida Sports Complex Ground', 'Green Park',
           'Greenfield International Stadium', 'Gymkhana Club Ground',
           'Hagley Oval', 'Harare Sports Club', 'Headingley',
           'Himachal Pradesh Cricket Association Stadium',
           'Holkar Cricket Stadium', 'ICC Academy',
           'Indian Petrochemicals Corporation Limited Sports Complex Ground',
           'Iqbal Stadium', 'JSCA International Stadium Complex',
           'Jade Stadium', 'John Davies Oval', 'Keenan Stadium',
           'Kennington Oval', 'Kensington Oval', 'Kensington Oval, Barbados',
           'Khan Shaheb Osman Ali Stadium', 'Kingsmead',
           'Kinrara Academy Oval', "Lord's", 'M Chinnaswamy Stadium',
           'MA Aziz Stadium', 'MA Chidambaram Stadium, Chepauk',
           'Madhavrao Scindia Cricket Ground',
           'Maharani Usharaje Trust Cricket Ground',
           'Maharashtra Cricket Association Stadium',
           'Mahinda Rajapaksa International Cricket Stadium, Sooriyawewa',
           'Malahide', 'Mangaung Oval', 'Mannofield Park', 'Manuka Oval',
           'Marrara Cricket Ground', 'McLean Park',
           'Melbourne Cricket Ground', 'Multan Cricket Stadium',
           'Nahar Singh Stadium', 'Narayanganj Osmani Stadium',
           'Narendra Modi Stadium', 'National Cricket Stadium, Grenada',
           'National Stadium', 'Nehru Stadium', 'New Wanderers Stadium',
           'Newlands', 'Niaz Stadium, Hyderabad', 'OUTsurance Oval',
           'Old Trafford', 'P Saravanamuttu Stadium',
           'Pallekele International Cricket Stadium', 'Perth Stadium',
           'Providence Stadium', 'Providence Stadium, Guyana',
           'Punjab Cricket Association IS Bindra Stadium, Mohali',
           "Queen's Park Oval, Port of Spain", "Queen's Park Oval, Trinidad",
           'Queens Sports Club', 'Queenstown Events Centre',
           'R Premadasa Stadium',
           'Rajiv Gandhi International Cricket Stadium, Dehradun',
           'Rajiv Gandhi International Stadium, Uppal',
           'Rangiri Dambulla International Stadium',
           'Rawalpindi Cricket Stadium', 'Reliance Stadium',
           'Riverside Ground', 'Sabina Park, Kingston',
           'Saurashtra Cricket Association Stadium', 'Sawai Mansingh Stadium',
           'Saxton Oval', 'Sector 16 Stadium', 'Seddon Park', 'Sedgars Park',
           'Senwes Park', 'Shaheed Chandu Stadium',
           'Sharjah Cricket Association Stadium', 'Sheikh Abu Naser Stadium',
           'Sheikhupura Stadium', 'Sher-e-Bangla National Cricket Stadium',
           'Shere Bangla National Stadium', 'Sinhalese Sports Club Ground',
           'Sir Vivian Richards Stadium, North Sound', 'Sophia Gardens',
           'Sportpark Het Schootsveld', "St George's Park",
           'St Lawrence Ground', 'SuperSport Park', 'Sydney Cricket Ground',
           'Sylhet International Cricket Stadium',
           'The Cooper Associates County Ground', 'The Rose Bowl',
           'The Village, Malahide', 'The Wanderers Stadium', 'Titwood',
           'Trent Bridge', 'University Oval', 'VRA Ground',
           'Vidarbha C.A. Ground', 'Vidarbha Cricket Association Ground',
           'Vidarbha Cricket Association Stadium, Jamtha', 'W.A.C.A. Ground',
           'Wankhede Stadium', 'Warner Park, Basseterre',
           'Western Australia Cricket Association Ground', 'Westpac Stadium',
           'Willowmoore Park', 'Windsor Park, Roseau',
           'Zahur Ahmed Chowdhury Stadium', 'Zayed Cricket Stadium']

city_stadium_mapping = {
    'Abu Dhabi': ['Sheikh Zayed Cricket Stadium'],
    'Adelaide': ['Adelaide Oval'],
    'Ahmedabad': ['Narendra Modi Stadium'],
    'Antigua': ["Antigua Recreation Ground, St John's"],
    'Auckland': ['Eden Park'],
    'Bangalore': ['M Chinnaswamy Stadium'],
    'Barbados': ['Kensington Oval', 'Kensington Oval, Barbados'],
    'Belfast': ['Civil Service Cricket Club, Stormont'],
    'Bengaluru': ['M Chinnaswamy Stadium'],
    'Benoni': ['Willowmoore Park'],
    'Birmingham': ['Edgbaston'],
    'Bloemfontein': ['Mangaung Oval'],
    'Bogra': ['Bogra Stadium'],
    'Brisbane': ['Brisbane Cricket Ground, Woolloongabba'],
    'Bristol': ['County Ground'],
    'Bulawayo': ['Bulawayo Athletic Club'],
    'Canberra': ['Manuka Oval'],
    'Canterbury': ['Bert Sutcliffe Oval', 'Hagley Oval'],
    'Cape Town': ['Newlands'],
    'Cardiff': ['Sophia Gardens'],
    'Centurion': ['SuperSport Park'],
    'Chandigarh': ['Punjab Cricket Association Stadium, Mohali'],
    'Chennai': ['MA Chidambaram Stadium, Chepauk'],
    'Chester-le-Street': ['Riverside Ground'],
    'Chittagong': ['Zahur Ahmed Chowdhury Stadium'],
    'Christchurch': ['Hagley Oval'],
    'Colombo': ['R Premadasa Stadium'],
    'Cuttack': ['Barabati Stadium'],
    'Darwin': ['Marrara Cricket Ground'],
    'Delhi': ['Arun Jaitley Stadium'],
    'Dhaka': ['Shere Bangla National Stadium'],
    'Dharamshala': ['Himachal Pradesh Cricket Association Stadium'],
    'Dubai': ['Dubai International Cricket Stadium'],
    'Dublin': ['Malahide'],
    'Dunedin': ['University Oval'],
    'Durban': ['Kingsmead'],
    'East London': ['Buffalo Park'],
    'Faisalabad': ['Iqbal Stadium'],
    'Faridabad': ['Nahar Singh Stadium'],
    'Fatullah': ['Khan Shaheb Osman Ali Stadium'],
    'Grenada': ['National Cricket Stadium, Grenada'],
    'Guwahati': ['Nehru Stadium'],
    'Guyana': ['Providence Stadium', 'Providence Stadium, Guyana'],
    'Gwalior': ['Captain Roop Singh Stadium'],
    'Hambantota': ['Mahinda Rajapaksa International Cricket Stadium, Sooriyawewa'],
    'Hamilton': ['Seddon Park'],
    'Harare': ['Harare Sports Club'],
    'Hobart': ['Bellerive Oval'],
    'Hyderabad': ['Rajiv Gandhi International Stadium, Uppal'],
    'Indore': ['Holkar Cricket Stadium'],
    'Jaipur': ['Sawai Mansingh Stadium'],
    'Jamaica': ['Sabina Park, Kingston'],
    'Jamshedpur': ['Keenan Stadium'],
    'Johannesburg': ['New Wanderers Stadium'],
    'Kanpur': ['Green Park'],
    'Karachi': ['National Stadium'],
    'Kimberley': ['De Beers Diamond Oval'],
    'Kochi': ['Nehru Stadium'],
    'Kolkata': ['Eden Gardens'],
    'Kuala Lumpur': ['Kinrara Academy Oval'],
    'Lahore': ['Gaddafi Stadium'],
    'Leeds': ['Headingley'],
    'London': ["Lord's", 'The Oval'],
    'Lucknow': ['Bharat Ratna Shri Atal Bihari Vajpayee Ekana Cricket Stadium'],
    'Manchester': ['Old Trafford'],
    'Margao': ['Nehru Stadium'],
    'Melbourne': ['Melbourne Cricket Ground'],
    'Mirpur': ['Shere Bangla National Stadium'],
    'Mount Maunganui': ['Bay Oval'],
    'Multan': ['Multan Cricket Stadium'],
    'Mumbai': ['Wankhede Stadium'],
    'Nagpur': ['Vidarbha Cricket Association Stadium, Jamtha'],
    'Napier': ['McLean Park'],
    'Nelson': ['Saxton Oval'],
    'Nottingham': ['Trent Bridge'],
    'Paarl': ['Boland Park'],
    'Pallekele': ['Pallekele International Cricket Stadium'],
    'Perth': ['Perth Stadium'],
    'Peshawar': ['Arbab Niaz Stadium'],
    'Port Elizabeth': ["St George's Park"],
    'Potchefstroom': ['Oval'],
    'Pune': ['Maharashtra Cricket Association Stadium'],
    'Queenstown': ['Queenstown Events Centre'],
    'Rajkot': ['Saurashtra Cricket Association Stadium'],
    'Ranchi': ['JSCA International Stadium Complex'],
    'Rawalpindi': ['Rawalpindi Cricket Stadium'],
    'Sharjah': ['Sharjah Cricket Association Stadium'],
    'Southampton': ['The Rose Bowl'],
    'St Kitts': ['Warner Park, Basseterre'],
    'St Lucia': ['Darren Sammy National Cricket Stadium, Gros Islet'],
    'Sydney': ['Sydney Cricket Ground'],
    'Taunton': ['County Ground'],
    'Trinidad': ["Queen's Park Oval, Trinidad"],
    'Vadodara': ['Moti Bagh Stadium'],
    'Visakhapatnam': ['Dr. Y.S. Rajasekhara Reddy ACA-VDCA Cricket Stadium'],
    'Wellington': ['Basin Reserve']
}


st.title("World Cup 1st Innings Score Predictor")

col1, col2 = st.columns(2)

with col1:
    st.markdown("<h3 style='margin: 0; padding: 0;''>Select batting team</h3>", unsafe_allow_html=True)
    batting_team = st.selectbox('', sorted(teams))

available_bowling_teams = sorted([team for team in teams if team != batting_team])

with col2:
    st.markdown("<h3 style='margin: 0; padding: 0;''>Select bowling team</h3>", unsafe_allow_html=True)
    bowling_team = st.selectbox('', sorted(available_bowling_teams), key='bowling')

st.markdown("<h3 style='margin: 0; padding: 0;''>Select City</h3>", unsafe_allow_html=True)
selected_city = st.selectbox('', sorted(cities))

col3, col4 = st.columns(2)

with col3:
    st.markdown("<h3 style='margin: 0; padding: 0;''>Current Score</h3>", unsafe_allow_html=True)
    current_score = st.number_input("", key='Current_score', value=0, step=1, format='%d')
with col4:
    st.markdown("<h3 style='margin: 0; padding: 0;''>Overs done (overs > 10)</h3>", unsafe_allow_html=True)
    overs = st.number_input('', key='Over_done')

col4, col5 = st.columns(2)
with col4:
    st.markdown("<h3 style='margin: 0; padding: 0;''>Wicket Fall</h3>", unsafe_allow_html=True)
    wicket = st.number_input('', value=0, step=1, format='%d')
with col5:
    # Check if the user selected a city
    if selected_city:
        st.markdown("<h3 style='margin: 0; padding: 0;''>Select Stadium</h3>", unsafe_allow_html=True)
        selected_stadium = st.selectbox('', sorted(city_stadium_mapping[selected_city]))
    else:
        st.info('Please select a city first.')

st.markdown("<h3 style='margin: 0; padding: 0;''>Runs Score in Last 10 Overs</h3>", unsafe_allow_html=True)
last_ten = st.number_input('', key='Runs Score in Last 10 Overs', value=0, step=1, format='%d')

if selected_city == 'Lucknow':
    selected_city = 'Kanpur'
    selected_stadium = 'Green Park'

if st.button('Predict'):
    # Validate inputs
    if current_score < last_ten:
        st.error("Error: Current score cannot be less than runs scored in the last 5 overs.")
    elif overs <= 10:
        st.error("Error: Overs should be greater than 10.")
    elif wicket < 0 or wicket >= 10:
        st.error("Error: Number of wickets should be between 0 and 10.")
    else:
        ball_left = 300 - overs * 6
        wicket_fall = 10 - wicket
        curr_run_rate = current_score / overs

        input_data = pd.DataFrame(
            {'batting_team': [batting_team], 'bowling_team': [bowling_team], 'city': [selected_city],
             'current_score': [current_score], 'balls_left': [ball_left], 'wickets_left': [wicket_fall],
             'crr': [curr_run_rate], 'last_ten': [last_ten], 'venue': [selected_stadium]
             }
        )
        result = pipe1.predict(input_data)
        # st.success(f"Predicted Score: {result[0]}")
        st.markdown(
            f'<div style="color: white; padding: 5px; border-radius: 5px; text-align: center;">'
            f'<h2>Predicted Score</h2>'
            f'<h1>{round(result[0])}</h1>'
            f'</div>',
            unsafe_allow_html=True
        )

