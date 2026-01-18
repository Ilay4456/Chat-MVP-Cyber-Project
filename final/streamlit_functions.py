import streamlit as st


#from client_class import Client
import socket as py_socket  # only used for exception types
import uuid




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




#defs -------------------------------------------------------------------
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



import streamlit as st
import uuid

def styled_text_box(
    text,
    width="100%",
    padding="24px 32px",
    background="#111827",
    border_color="#2563eb",
    border_width="3px",
    border_radius="16px",
    text_size="1.6rem",
    text_color="white",
    font="Poppins",
    weight="500",
    align="center",
    shadow="0 10px 30px rgba(0,0,0,0.35)",
    margin="20px auto",
):
    box_id = f"box_{uuid.uuid4().hex}"

    st.markdown(
        f"""
        <style>
        @import url('https://fonts.googleapis.com/css2?family={font}:wght@400;500;600;700&display=swap');

        .{box_id} {{
            width: {width};
            padding: {padding};
            background: {background};
            border: {border_width} solid {border_color};
            border-radius: {border_radius};
            box-shadow: {shadow};
            margin: {margin};
        }}

        .{box_id} p {{
            margin: 0;
            font-family: '{font}', sans-serif;
            font-size: {text_size};
            color: {text_color};
            font-weight: {weight};
            text-align: {align};
            line-height: 1.4;
        }}
        </style>

        <div class="{box_id}">
            <p>{text}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

