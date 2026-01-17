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


if "client" not in st.session_state:
    st.session_state["client"] = None

client = st.session_state["client"]


#app itself


#app color
st.markdown(
    """
    <style>
    .stApp {
        background-color: 0F2854;
    }
    </style>
    """,
    unsafe_allow_html=True
)

#titles
center_title("Chat MVP 🏀")
center_title("The AI Of NBA Predictions")

st.divider()
col1, col2, col3 = st.columns([16, 8, 10])

with col3:
    st.image(r"cyber_proj/final/ball_image1.png", width=600)

with col1:
    st.image(r"cyber_proj/final/ball_image2.png", width=600)

with col2:
    st.markdown(
        "<p style='font-size: 20px;'>Made by Ilay Ben Shimol</p>",
        unsafe_allow_html=True
    )



#for buttons
st.markdown(
    """
    <style>
    .stButton > button {
        font-size: 20px;
        padding: 14px 40px;
        border-radius: 12px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns([1, 1, 1])

with col2:
    if st.button("Connect"):
        if not client:
            client = Client()
            if client:
                st.session_state["client"] = client   # ✅ SAVE
            else:
                st.session_state["client"] = None     # ✅ SAVE





if client:
    st.success("Connected!")

    with st.chat_message("assistant"):
        st.write("Hello and welcome to Chat MVP! My current profession is to predict which nba team will win in a match.")
        st.write("Give it a try! select team A and team B and I will try to give my best prediction.")

    col1, col2 = st.columns(2)
    with col1:
        choice1 = st.selectbox("Team A", nba_teamsA, key="choice1")

    with col2:
        choice2 = st.selectbox("Team B", nba_teamsB, key="choice2")


    col1, col2, col3 = st.columns(3)
    with col2: #middle
        send = st.button("Send Prediction")

    if send:
        with st.chat_message("user"):
            st.write(f"Please predict the winner in a game between {choice1} and {choice2}. Please make the prediction as precise as you can.")
        with st.chat_message("assistant"):
            st.write(f"*Not developed yet*")





else:
    st.error("Unable to connect, please try again")



