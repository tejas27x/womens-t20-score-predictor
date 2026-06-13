import streamlit as st
import pickle
import pandas as pd
import numpy as np

# ── Page config ────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Women's T20 Score Predictor",
    page_icon="🏏",
    layout="centered"
)

# ── Custom CSS ─────────────────────────────────────────────────────────────
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Raleway:wght@400;700;900&family=Inter:wght@400;500&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }
    .main { background-color: #0d0d1a; }
    h1, h2, h3 { font-family: 'Raleway', sans-serif; }

    .title-box {
        background: linear-gradient(135deg, #a855f7, #ec4899);
        border-radius: 16px;
        padding: 2rem;
        text-align: center;
        margin-bottom: 2rem;
    }
    .title-box h1 {
        color: white;
        font-size: 2.2rem;
        font-weight: 900;
        margin: 0;
        letter-spacing: -1px;
    }
    .title-box p {
        color: rgba(255,255,255,0.8);
        margin: 0.4rem 0 0;
        font-size: 0.95rem;
    }
    .result-box {
        background: linear-gradient(135deg, #1e1b4b, #312e81);
        border: 2px solid #a855f7;
        border-radius: 16px;
        padding: 2rem;
        text-align: center;
        margin-top: 1.5rem;
    }
    .result-box h2 {
        color: #f0abfc;
        font-size: 1.1rem;
        font-weight: 500;
        letter-spacing: 2px;
        text-transform: uppercase;
        margin: 0 0 0.5rem;
    }
    .result-score {
        font-family: 'Raleway', sans-serif;
        font-size: 4rem;
        font-weight: 900;
        color: white;
        line-height: 1;
    }
    .result-range {
        color: #c4b5fd;
        font-size: 0.9rem;
        margin-top: 0.5rem;
    }
    .stButton > button {
        background: linear-gradient(135deg, #a855f7, #ec4899);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 0.75rem 2rem;
        font-family: 'Raleway', sans-serif;
        font-weight: 700;
        font-size: 1rem;
        width: 100%;
        cursor: pointer;
        transition: opacity 0.2s;
    }
    .stButton > button:hover { opacity: 0.85; }
    .warning-box {
        background: #2d1b00;
        border: 1px solid #f59e0b;
        border-radius: 10px;
        padding: 0.75rem 1rem;
        color: #fcd34d;
        font-size: 0.875rem;
        margin-top: 0.5rem;
    }
</style>
""", unsafe_allow_html=True)

# ── Load model ─────────────────────────────────────────────────────────────
@st.cache_resource
def load_model():
    return pickle.load(open('pipe_female.pkl', 'rb'))

pipe = load_model()

# ── Data ───────────────────────────────────────────────────────────────────
teams = sorted([
    'Australia', 'India', 'Bangladesh', 'New Zealand',
    'South Africa', 'England', 'West Indies', 'Pakistan',
    'Sri Lanka', 'Netherlands', 'Ireland', 'Scotland', 'Zimbabwe'
])

cities = sorted([
    'Sylhet', 'Colombo', 'Dublin', 'Sharjah', 'Sydney',
    'Birmingham', 'Cape Town', 'Karachi', 'Kuala Lumpur', 'Mumbai',
    'Melbourne', 'Canberra', 'St Lucia', 'Dubai', 'Chelmsford',
    'Galle', 'Guyana', 'Wellington', 'East London', 'Benoni',
    'Paarl', 'Potchefstroom', 'Abu Dhabi', 'Navi Mumbai',
    'Dambulla', 'Derby', 'Chennai', 'North Sound',
    'Bridgetown', 'Amstelveen', 'Delhi', 'Taunton',
    'Durban', 'Deventer', 'London', 'Bristol',
    'Hamilton', 'Dhaka', 'Brisbane', 'Brighton',
    'Northampton', 'Gqeberha', 'Mount Maunganui',
    'Gros Islet', 'Murcia', 'Dunedin', 'Bready',
    'Bangalore', 'Belfast', 'Gold Coast', 'Nelson',
    'Almeria', 'Auckland', 'Adelaide', 'Loughborough',
    'Doha', 'Perth', 'Christchurch', 'Johannesburg',
    'Surat', 'Utrecht', 'Hangzhou', 'Guanggong',
    'Lahore', 'Antigua', 'Bangkok', 'Kingstown',
    'Mirpur', 'Multan', 'Trinidad', 'Basseterre',
    'Kirtipur', 'Southampton', 'Thiruvananthapuram',
    'Guwahati', 'Lucknow', 'Queenstown', 'Chattogram',
    'Chester-le-Street', 'Kathmandu', 'Hambantota',
    'Dundee', 'Canterbury', 'Carrara', 'Centurion',
    "St George's", 'Providence', 'Rotterdam', 'Hobart',
    'Edinburgh', 'Cave Hill', 'Visakhapatnam', 'Nagpur',
    'Chandigarh', 'Dharamsala', 'Pietermaritzburg',
    'Nottingham', 'Manchester', 'Mackay', 'Hove',
    'Bloemfontein', 'Kimberley', 'Barbados','Wales'
])

# ── Header ─────────────────────────────────────────────────────────────────
st.markdown("""
<div class="title-box">
    <h1>🏏 Women's T20 Score Predictor</h1>
    <p>ICC Women's T20 World Cup 2026 · ML-Powered Prediction</p>
</div>
""", unsafe_allow_html=True)

# ── Inputs ─────────────────────────────────────────────────────────────────
col1, col2 = st.columns(2)
with col1:
    batting_team = st.selectbox('🏏 Batting Team', teams)
with col2:
    bowling_team = st.selectbox('🎯 Bowling Team', teams)

city = st.selectbox('📍 City', cities)

col3, col4, col5 = st.columns(3)
with col3:
    current_score = st.number_input('Current Score', min_value=0, step=1)
with col4:
    overs = st.number_input('Overs Done', min_value=0.1, max_value=20.0, step=0.1, format="%.1f")
with col5:
    wickets = st.number_input('Wickets Out', min_value=0, max_value=9, step=1)

last_five = st.number_input('Runs in Last 5 Overs', min_value=0, step=1)

# ── Validation ─────────────────────────────────────────────────────────────
if batting_team == bowling_team:
    st.markdown('<div class="warning-box">⚠️ Batting and bowling teams must be different.</div>', unsafe_allow_html=True)

# ── Predict ────────────────────────────────────────────────────────────────
if st.button('Predict Final Score'):
    if batting_team == bowling_team:
        st.error("Please select different teams.")
    elif overs < 5:
        st.warning("Prediction works best after 5 overs.")
    else:
        balls_left   = 120 - int(overs * 6)
        wickets_left = 10 - wickets
        crr          = current_score / overs

        input_df = pd.DataFrame({
            'batting_team'  : [batting_team],
            'bowling_team'  : [bowling_team],
            'city'          : [city],
            'current_score' : [current_score],
            'balls_left'    : [balls_left],
            'wickets_left'  : [wickets_left],
            'crr'           : [crr],
            'last_five'     : [last_five]
        })

        result = pipe.predict(input_df)
        predicted = int(result[0])
        low, high = predicted - 10, predicted + 10

        st.markdown(f"""
        <div class="result-box">
            <h2>Predicted Final Score</h2>
            <div class="result-score">{predicted}</div>
            <div class="result-range">Expected range: {low} – {high}</div>
        </div>
        """, unsafe_allow_html=True)