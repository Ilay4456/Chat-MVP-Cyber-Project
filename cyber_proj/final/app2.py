import streamlit as st


from client_class import Client
import socket as py_socket  # only used for exception types

st.set_page_config(page_title="TCP Client", page_icon="🔌", layout="centered")

HOST = "127.0.0.1"
PORT = 12345
RECV_BYTES = 1024
#SOCKET_TIMEOUT_SECONDS = 3.0  # prevents Streamlit from hanging forever on recv()


nba_teamsA = [
    "-Team A-",
    "Atlanta Hawks",
    "Boston Celtics",
    "Brooklyn Nets",
    "Charlotte Hornets",
    "Chicago Bulls",
    "Cleveland Cavaliers",
    "Dallas Mavericks",
    "Denver Nuggets",
    "Detroit Pistons",
    "Golden State Warriors",
    "Houston Rockets",
    "Indiana Pacers",
    "Los Angeles Clippers",
    "Los Angeles Lakers",
    "Memphis Grizzlies",
    "Miami Heat",
    "Milwaukee Bucks",
    "Minnesota Timberwolves",
    "New Orleans Pelicans",
    "New York Knicks",
    "Oklahoma City Thunder",
    "Orlando Magic",
    "Philadelphia 76ers",
    "Phoenix Suns",
    "Portland Trail Blazers",
    "Sacramento Kings",
    "San Antonio Spurs",
    "Toronto Raptors",
    "Utah Jazz",
    "Washington Wizards"
]
nba_teamsB = [
    "-Team B-",
    "Atlanta Hawks",
    "Boston Celtics",
    "Brooklyn Nets",
    "Charlotte Hornets",
    "Chicago Bulls",
    "Cleveland Cavaliers",
    "Dallas Mavericks",
    "Denver Nuggets",
    "Detroit Pistons",
    "Golden State Warriors",
    "Houston Rockets",
    "Indiana Pacers",
    "Los Angeles Clippers",
    "Los Angeles Lakers",
    "Memphis Grizzlies",
    "Miami Heat",
    "Milwaukee Bucks",
    "Minnesota Timberwolves",
    "New Orleans Pelicans",
    "New York Knicks",
    "Oklahoma City Thunder",
    "Orlando Magic",
    "Philadelphia 76ers",
    "Phoenix Suns",
    "Portland Trail Blazers",
    "Sacramento Kings",
    "San Antonio Spurs",
    "Toronto Raptors",
    "Utah Jazz",
    "Washington Wizards"
]


def center_title(text, color="#2563eb"):
    st.markdown(
        f"""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@600&display=swap');

        .custom-title {{
            font-family: 'Poppins', sans-serif;
            text-align: center;
            font-size: 3rem;
            color: {color};
        }}
        </style>

        <h1 class="custom-title">{text}</h1>
        """,
        unsafe_allow_html=True
    )

import streamlit as st

import streamlit as st
import uuid

def styled_text(
    text,
    size="2rem",
    color="#111827",
    font="Poppins",
    weight="600",
    align="center",
    line_height="1.2",
    letter_spacing="0px",
    transform="none",
    shadow=None,
    margin="0",
):
    class_id = f"styled_{uuid.uuid4().hex}"

    st.markdown(
        f"""
        <style>
        @import url('https://fonts.googleapis.com/css2?family={font}:wght@400;600;700&display=swap');

        .{class_id} {{
            font-family: '{font}', sans-serif !important;
            font-size: {size} !important;
            color: {color} !important;
            font-weight: {weight} !important;
            text-align: {align} !important;
            line-height: {line_height} !important;
            letter-spacing: {letter_spacing} !important;
            text-transform: {transform} !important;
            margin: {margin} !important;
            {"text-shadow: " + shadow + " !important;" if shadow else ""}
        }}
        </style>

        <div class="{class_id}">{text}</div>
        """,
        unsafe_allow_html=True
    )


def wide_divider(
    width="100%",        # "60%", "80%", "100%"
    height="6px",        # thickness
    color="#2563eb",
    radius="6px",
    margin="24px auto"
):
    st.markdown(
        f"""
        <div style="
            width: {width};
            height: {height};
            background-color: {color};
            border-radius: {radius};
            margin: {margin};
        "></div>
        """,
        unsafe_allow_html=True
    )


#app itself------------------------------



st.set_page_config(
    page_title="CHAT MVP",
    page_icon="🔌",
    layout="wide"
)

st.markdown(
    """
    <style>
    .stApp {
        background-color: black;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.image(r"cyber_proj/final/chat_logo.png", width=500)
styled_text("Made by Ilay Ben Shimol:", size="1.7rem", color='white')

#titles
styled_text("CHAT", size="8rem", color='#00438c')

styled_text(
    "M.V.P",
    size="15rem",
    color="#da1a32",
    weight="700",
    letter_spacing="4px",
    transform="uppercase",
    shadow="0 6px 20px rgba(0,0,0,0.25)"
)



styled_text("The AI of NBA predictions", size="3.5rem", color='white')

wide_divider(height='10px', color='white')
col1, col2= st.columns([19,10])

with col1:
    styled_text("Predict Result of NBA games using updated NBA data", size="2.8rem", color='white', align='left')

with col2:
    st.image(r"cyber_proj/final/ball_image4.png")


col1, col2, col3 = st.columns([1, 1, 1])

st.markdown(
    """
    <style>
    .stButton > button {
        font-size: 50px;
        padding: 14px 40px;
        border-radius: 12px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

with col2:
    if st.button("Let's Start"):
        st.switch_page("pages/1_sign_in.py")











