import streamlit as st


#from client_class import Client
import socket as py_socket  # only used for exception types
import uuid

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


def styled_input(
    label,
    key,
    placeholder="",
    width="100%",
    height="64px",
    background="#000000",
    border_color="#2563eb",
    border_radius="14px",
    text_color="white",
    font="Poppins",
    font_size="1.4rem",
    weight="500",
    glow=True,
    margin="16px 0",
):
    unique_id = f"input_{uuid.uuid4().hex}"

    st.markdown(
        f"""
        <style>
        @import url('https://fonts.googleapis.com/css2?family={font}:wght@400;500;600;700&display=swap');

        .{unique_id} {{
            width: {width};
            margin: {margin};
        }}

        .{unique_id} label {{
            font-family: '{font}', sans-serif;
            color: {text_color};
            font-size: 1.2rem;
            font-weight: 600;
            margin-bottom: 6px;
            display: block;
        }}

        .{unique_id} input {{
            width: 100%;
            height: {height};
            padding: 0 18px;
            background: {background};
            border: 2px solid {border_color};
            border-radius: {border_radius};
            color: {text_color};
            font-family: '{font}', sans-serif;
            font-size: {font_size};
            font-weight: {weight};
            outline: none;
        }}

        .{unique_id} input::placeholder {{
            color: rgba(255,255,255,0.5);
        }}

        .{unique_id} input:focus {{
            border-color: {border_color};
            box-shadow: {"0 0 0 4px rgba(37,99,235,0.35)" if glow else "none"};
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

    return st.text_input(
        label,
        placeholder=placeholder,
        key=key,
        label_visibility="collapsed"
    )


def styled_password_input(
    label,
    key,
    placeholder="",
    width="100%",
    height="64px",
    background="#000000",
    border_color="#2563eb",
    border_radius="14px",
    text_color="white",
    font="Poppins",
    font_size="1.4rem",
    weight="500",
    glow=True,
    margin="16px 0",
):
    unique_id = f"password_{uuid.uuid4().hex}"

    st.markdown(
        f"""
        <style>
        @import url('https://fonts.googleapis.com/css2?family={font}:wght@400;500;600;700&display=swap');

        .{unique_id} {{
            width: {width};
            margin: {margin};
        }}

        .{unique_id} label {{
            font-family: '{font}', sans-serif;
            color: {text_color};
            font-size: 1.2rem;
            font-weight: 600;
            margin-bottom: 6px;
            display: block;
        }}

        .{unique_id} input {{
            width: 100%;
            height: {height};
            padding: 0 18px;
            background: {background};
            border: 2px solid {border_color};
            border-radius: {border_radius};
            color: {text_color};
            font-family: '{font}', sans-serif;
            font-size: {font_size};
            font-weight: {weight};
            outline: none;
        }}

        .{unique_id} input::placeholder {{
            color: rgba(255,255,255,0.45);
        }}

        .{unique_id} input:focus {{
            border-color: {border_color};
            box-shadow: {"0 0 0 4px rgba(37,99,235,0.35)" if glow else "none"};
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

    return st.text_input(
        label,
        placeholder=placeholder,
        key=key,
        type="password",
        label_visibility="collapsed"
    )

#app itself------------------------------



st.set_page_config(
    page_title="Sign In Page",
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

st.image(r"final/chat_logo.png", width=500)

#titles

styled_text("Sign In", size="8rem", color='#00438c')




styled_text("To experience the power of AI data analysis", size="3.5rem", color='white')

wide_divider(height='10px', color='white')
col1, col2= st.columns([2,1])

with col1:
    styled_text("Sign In/Sign Up", size="2.8rem", color='white', align='left')




#input boxes:
username = styled_input(
    label="Username",
    key="username",
    placeholder="Enter your username",
    border_color="#da1a32"
)

password = styled_password_input(
    label="Password",
    key="password",
    placeholder="Enter your password",
    border_color="#da1a32"
)



col1, col2, col3 = st.columns([1, 1, 1])

st.markdown(
    """
    <style>
    .stButton > button {
        font-size: 85px !important;
        padding: 30px 100px !important;
        border-radius: 30px !important;
        background-color: #da1a32 !important;
        color: white !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)



with col2:
    if st.button("Let's Start"):
        st.switch_page("pages/1_sign_in.py")


cola, colb, colc = st.columns([1,1,1])

with colb:
    st.image(r"final/lebron.jpg")












