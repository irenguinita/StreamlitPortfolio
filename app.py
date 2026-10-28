from datetime import date

import pandas as pd
import plotly.graph_objects as go
import streamlit as st
from PIL import Image, ImageDraw, ImageFont

NAME = "Iren Nathaleigh L. Guinita"
PROGRAM = "BS Computer Science · 3rd Year"
SECTION = "CS365 | Applied AI - F2"
LOCATION = "Cebu, Philippines"
EMAIL = "guinitairen@gmail.com" 
GITHUB = "https://github.com/irenguinita"  
TAGLINE = "Call me Ren. I love learning, being challenged, and sitting at the intersection of things." 
SHORT_ABOUT = "I'm a Junior Computer Science student who wants to build things that are meaningful and fun. I love looking for unique places to apply my skills, ones that require a mix of creativity, curiosity, logic, and people."
BIO = """
Hi! You can call me Ren. I'm a Junior Computer Science student from Cebu Institute of Technology - University. I dabble in software development, leadership, arts and the humanities, and their intersections.
"""
INTERESTS = ["People", "Leadership", "Software Development", "Art and Humanities", "Sleeping", "Music", "Doom Scrolling"] 

AUTOBIOGRAPHY = """
I came from a little sleepy town on the way to the north of Cebu called Catmon. I grew up in the relative suburbs, always surrounded by the trees and plants my mom loved to take care of. I grew up as a shy child (but I'd like to think I grew out of that), and I was always curious about the world and the people around me. I loved observing people and their behavior and how things worked. I enjoyed Encarta Kids (iykyk), the Discovery and National Geographic channels, and the TV show Cats and Dogs 101 (give me a dog breed and little me could tell you all about them). I loved how those shows (and app) were my first gateway to learning and having things explained to me in a way that was fun and engaging and encouraged me to actually learn. I also loved watching that show with the magician who would explain how the magic tricks worked. I loved getting to see behind the curtains and seeing how things worked, and I think that curiosity has stayed with me to this day.

I finished Elementary in the school that's right beside my house (I could hear the bell for the flag and that would be my cue that I needed to go). My high school was a little further away (a 5 minute walk, it was quite a challenge, I needed to cross a river, climb a mountain, and brave the pack of dogs that for some reason still has not learned to recognize me (I'm not a threat, I promise)). The elementary was called Bagalnga Elementary School and my high school Gabriel Jurado Foundation School, Inc. (JHS) and Passionist Sisters' School (Catmon) Inc. (SHS).

On a personal level, my interest lies more with the arts and humanities, but I also have a strong interest in software development especially in terms of where can I apply it in the former. Did you know that the first form of binary came from knitting? I think that that is a really interesting intersection of the two, and I would love to explore more of that. As a crocheter myself, I found that to be part of my inspiration to pursue Computer Science.
"""

LIFE = [ 
    (2006, 1, "Born", "I was born as a rainbow baby, very cool very nice probably very spoiled but I do not remember"),
    (2020, 3, "Pandemic", "Turned my life around, learned a lot of things"),
    (2024, 4, "Graduated high school", "Graduated high school, got dream scholarship, excited for it all"),
    (2024, -1, "Started college", "It was so different. Got challenged, questioned myself and my capabilities. Pushed through anyway."),
    (2025, 1, "2nd Year College", "Got humbled by first year. Decided that college can have a little more fun. Had fun. Joined orgs. Made friends. (Almost got killed by DAA and DSA tho. Almost)"),
    (2026, 5, "3rd Year", "Thriving. Joined competitions, joined more orgs, made friends, became actually interested in software development."),
]

TECHNICAL = {"Python": 5, "Java": 7, "SQL": 7, "Project Management": 8, "Frontend Design": 6,}
EVERYDAY = {"Communication": 5, "Time management": 3, "Teamwork": 9, "Problem solving": 8, "Adaptability": 10}
NICHE = {"Crossing the street": 1, "Intuition": 10, "Eyesight": 2, "Music taste": 10, "Popculture knowledge": 6}  

PROJECTS = [
    {
        "title": "Pinoy Party",
        "course": "DOST ESports Challenge (Game Jam)",
        "role": "Project Lead, Artist, Front-end, QA",
        "tools": ["Godot", "Aseprite"],
        "summary": "Pinoy Party is a multiplayer Godot 4 party game inspired by classic Filipino street games! Gather your friends, roll the dice on the virtual board, and compete in fast-paced minigames to see who will be crowned the ultimate champion.",
        "link": "https://github.com/Zephyrdoestech/Pinoy-Party",
    },
    {
        "title": "Sir Serato Simulator",
        "course": "CSIT228 Object-Oriented Programming 2",
        "role": "Backend and Frontend developer, QA",
        "tools": ["Java"],
        "summary": "Sir Serato Simulator is a high-stake arcade classroom management simulator game where you act as the iconic teacher, Sir Jay Vince Serato, proctoring a set of students that are taking your quizzes. Of course, being a teacher comes with its own set of problems. You must be vigilant in ensuring that your students do not attempt to cheat or else you will lose your patience and your sanity. ",
        "link": "https://github.com/binggbongg/CSIT228-Capstone-Sir-Jay-Simulator",
    },
    {
        "title": "TaraTeknoy",
        "course": "Mobile Development",
        "role": "Full stack developer, QA",
        "tools": ["Kotlin"],
        "summary": "A centralized Android application for campus event discovery and management for Technologians",
        "link": "https://github.com/irenguinita/tarateknoy",
    },
]

PLUM = "#3C0932"
PLUM_MID = "#7A3B6B"
ROSE = "#B5779F"
BLUSH = "#E8D5E1"
FONT = "Lora, Georgia, serif"

st.set_page_config(page_title=f"{NAME} | Portfolio", page_icon="🍇", layout="wide")

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,400;0,600;0,700;1,400&display=swap');

    html, body, .stApp,
    .stApp *:not([data-testid="stIconMaterial"]):not(.material-icons) {
        font-family: 'Lora', Georgia, 'Times New Roman', serif !important;
    }
    .stApp { background-color: #FBF7FA; }
    [data-testid="stSidebar"] { background-color: #F1E4EC; }
    .stApp, .stApp p, .stApp li, .stApp label, .stApp h1, .stApp h2, .stApp h3,
    .stApp h4, .stApp [data-testid="stMetricValue"], .stApp [data-testid="stCaptionContainer"] {
        color: #3C0932;
    }
    .stButton > button, .stFormSubmitButton > button, .stDownloadButton > button, .stLinkButton > a {
        background-color: #3C0932; border: none; border-radius: 8px;
    }
    .stButton > button:hover, .stFormSubmitButton > button:hover, .stDownloadButton > button:hover {
        background-color: #5A1C4D;
    }
    .stButton button p, .stFormSubmitButton button p, .stDownloadButton button p, .stLinkButton a p {
        color: #FBF7FA !important;
    }
    [data-baseweb="tab-highlight"] { background-color: #3C0932 !important; }
    button[aria-selected="true"] p { font-weight: 700; }
    </style>
    """,
    unsafe_allow_html=True,
)

if "messages" not in st.session_state:
    st.session_state.messages = []


def make_placeholder_photo(initials: str) -> Image.Image:
    """Clearly labeled stand-in until you add photo.jpg next to app.py."""
    img = guinita.png
    d = ImageDraw.Draw(img)
    try:
        big = ImageFont.load_default(size=120)
        small = ImageFont.load_default(size=24)
    except TypeError:
        big = small = ImageFont.load_default()
    d.text((200, 180), initials, fill="#FBF7FA", font=big, anchor="mm")
    d.text((200, 340), "placeholder photo", fill=BLUSH, font=small, anchor="mm")
    return img


def get_photo():
    try:
        return Image.open("guinita.png")
    except FileNotFoundError:
        return make_placeholder_photo("IG")


def radar(title, data, line, fill):
    labels, vals = list(data.keys()), list(data.values())
    fig = go.Figure(
        go.Scatterpolar(
            r=vals + vals[:1],
            theta=labels + labels[:1],
            fill="toself",
            fillcolor=fill,
            line=dict(color=line, width=2),
            marker=dict(size=6, color=line),
            hovertemplate="%{theta}: %{r}/10<extra></extra>",
        )
    )
    fig.update_layout(
        title=dict(text=title, x=0.5, font=dict(size=18)),
        polar=dict(
            bgcolor="rgba(0,0,0,0)",
            radialaxis=dict(range=[0, 10], tickvals=[2, 4, 6, 8, 10], gridcolor=BLUSH,
                            linecolor=BLUSH, tickfont=dict(size=9)),
            angularaxis=dict(gridcolor=BLUSH, linecolor=BLUSH, tickfont=dict(size=12)),
        ),
        showlegend=False,
        paper_bgcolor="rgba(0,0,0,0)",
        font=dict(family=FONT, color=PLUM),
        margin=dict(l=60, r=60, t=70, b=30),
        height=380,
    )
    return fig

with st.sidebar:
    st.image(get_photo(), use_container_width=True)
    st.subheader(NAME)
    st.caption(f"{PROGRAM}\n\n{SECTION}")
    st.write(SHORT_ABOUT)
    st.markdown(f"📍{LOCATION}  \n📧 {EMAIL}  \n🔗 [GitHub]({GITHUB})")
    st.divider()

    st.subheader("Say hello")
    with st.form("contact_form", clear_on_submit=True):
        sender = st.text_input("Your name")
        email = st.text_input("Your email")
        topic = st.selectbox("Topic", ["Say hi", "Feedback on the site", "Collaboration", "Other"])
        rating = st.slider("How do you like the site?", 1, 5, 4)
        message = st.text_area("Message", height=100)
        ok_reply = st.checkbox("You may reply to me")
        submitted = st.form_submit_button("Send")

    if submitted:
        if not sender or not message:
            st.error("Please add your name and a message.")
        else:
            st.session_state.messages.append(
                {"when": date.today().isoformat(), "from": sender, "email": email,
                 "topic": topic, "rating": rating, "message": message}
            )
            st.success(f"Thanks, {sender}! Your message was sent." + (" I'll reply soon." if ok_reply else ""))
            st.balloons()
    if st.session_state.messages:
        st.caption(f"Messages sent this session: {len(st.session_state.messages)}")

col_photo, col_text = st.columns([1, 2.2], gap="large")
with col_photo:
    st.image(get_photo())
with col_text:
    st.title(NAME)
    st.markdown(f"*{TAGLINE}*")
    st.caption(f"{PROGRAM}  ·  {LOCATION}  ·  {SECTION}")
    st.markdown(BIO)
    st.markdown("**Interests:** " + "  ".join(f"`{i}`" for i in INTERESTS))
    m1, m2, m3 = st.columns(3)
    m1.metric("Year level", "3rd")
    m2.metric("Projects", len(PROJECTS))
    m3.metric("Top technical skill", max(TECHNICAL, key=TECHNICAL.get))

st.divider()

tab_story, tab_skills, tab_projects = st.tabs(["Autobiography", "Skills", "Projects"])

with tab_story:
    st.header("My story")
    st.markdown(AUTOBIOGRAPHY)

    st.subheader("The highs and lows")
    LIFE_SORTED = sorted(LIFE, key=lambda r: r[0])
    years = [r[0] for r in LIFE_SORTED]
    scores = [r[1] for r in LIFE_SORTED]
    titles = [r[2] for r in LIFE_SORTED]
    descs = [r[3] for r in LIFE_SORTED]

    fig = go.Figure()
    fig.add_hline(y=0, line=dict(color=PLUM_MID, dash="dot", width=1))
    fig.add_trace(
        go.Scatter(
            x=years, y=scores, mode="lines+markers+text",
            text=titles,
            textposition=["top center" if s >= 0 else "bottom center" for s in scores],
            textfont=dict(size=12, color=PLUM),
            line=dict(color=PLUM, width=3, shape="spline", smoothing=0.8),
            marker=dict(size=12, color=[PLUM if s >= 0 else ROSE for s in scores],
                        line=dict(color=PLUM, width=2)),
            fill="tozeroy", fillcolor="rgba(60,9,50,0.07)",
            hovertext=descs,
            hovertemplate="<b>%{text}</b> (%{x})<br>%{hovertext}<extra></extra>",
        )
    )
    fig.update_layout(
        height=460,
        showlegend=False,
        paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
        font=dict(family=FONT, color=PLUM),
        margin=dict(l=20, r=20, t=30, b=30),
        xaxis=dict(tickformat="d", showgrid=False, linecolor=PLUM_MID),
        yaxis=dict(range=[-5.8, 5.8], tickvals=[-5, 0, 5], ticktext=["Low", "Okay", "High"],
                   gridcolor=BLUSH, zeroline=False),
    )
    st.plotly_chart(fig)

    pick = st.selectbox("Zoom in on a moment", titles)
    idx = titles.index(pick)
    with st.container(border=True):
        st.markdown(f"**{years[idx]} · {titles[idx]}**")
        st.write(descs[idx])

with tab_skills:
    st.header("Skills")
    st.write("Rated honestly by me, from 0 to 10. Hover over a point to see its score.")

    c1, c2, c3 = st.columns(3, gap="medium")
    with c1:
        st.plotly_chart(radar("Technical", TECHNICAL, PLUM, "rgba(60,9,50,0.25)"))
        st.caption(f"Strongest: **{max(TECHNICAL, key=TECHNICAL.get)}**")
    with c2:
        st.plotly_chart(radar("Everyday", EVERYDAY, PLUM_MID, "rgba(122,59,107,0.25)"))
        st.caption(f"Strongest: **{max(EVERYDAY, key=EVERYDAY.get)}**")
    with c3:
        st.plotly_chart(radar("Personal", NICHE, ROSE, "rgba(181,119,159,0.30)"))
        st.caption(f"Strongest: **{max(NICHE, key=NICHE.get)}**")

    all_skills = pd.DataFrame(
        [(k, v, "Technical") for k, v in TECHNICAL.items()]
        + [(k, v, "Everyday") for k, v in EVERYDAY.items()]
        + [(k, v, "Niche") for k, v in NICHE.items()],
        columns=["Skill", "Level (0-10)", "Group"],
    )
    with st.expander("See all the numbers"):
        st.dataframe(all_skills, hide_index=True)
    st.download_button(
        "⬇️ Download my skills (CSV)",
        all_skills.to_csv(index=False).encode("utf-8"),
        file_name="skills.csv",
        mime="text/csv",
    )

with tab_projects:
    st.header("Projects")
    all_tools = sorted({t for p in PROJECTS for t in p["tools"]})
    tool_filter = st.multiselect("Filter by tool", all_tools)
    shown = [p for p in PROJECTS if not tool_filter or set(tool_filter) & set(p["tools"])]
    if not shown:
        st.warning("No projects use those tools.")

    cols = st.columns(len(shown) or 1, gap="medium")
    for col, p in zip(cols, shown):
        with col:
            with st.container(border=True):
                st.subheader(f"{p['title']}")
                st.caption(p["course"])
                st.write(p["summary"])
                st.markdown(f"**Role:** {p['role']}")
                st.markdown("**Tools:** " + ", ".join(f"`{t}`" for t in p["tools"]))
                if p["link"]:
                    st.link_button("View project", p["link"])

st.divider()
st.caption(f"© {date.today().year} {NAME} · {SECTION}")