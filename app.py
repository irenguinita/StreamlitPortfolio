from datetime import date

import pandas as pd
import plotly.graph_objects as go
import streamlit as st
from PIL import Image, ImageDraw, ImageFont

NAME = "Iren Nathaleigh L. Guinita"
PROGRAM = "BS Computer Science · 3rd Year"
SECTION = "CS365 | Applied AI - F2"
LOCATION = "Cebu, Philippines"
EMAIL = "guinitairen@example.com" 
GITHUB = "https://github.com/irenguinita"  
TAGLINE = "Call me Ren. I love learning, being challenged, and sitting at the intersection of things." 
SHORT_ABOUT = "I'm a Junior Computer Science student who wants to build things that are meaningful and fun. I love looking for unique places to apply my skills, ones that require a mix of creativity, curiosity, logic, and people."
BIO = """
TODO: Write a few sentences in your own words. Who are you, what are you studying,
and what kind of problems do you enjoy solving? This is your full "About" section.

Hi! You can call me Ren. I'm a Junior Computer Science student from Cebu Institute of Technology - University. 

"""
INTERESTS = ["People", "Leadership", "Fuzzy logic", "Data analysis", "Hackathons"]  # TODO

AUTOBIOGRAPHY = """
TODO: Tell your story in your own words: where you come from, what shaped you,
where you studied, what you love doing, and where you're headed. A few paragraphs is plenty.
"""

# Life line: (year, score from -5 low to +5 high, short title, what happened)
LIFE = [  # TODO: replace every row with your real highs and lows
    (2012, 3, "Childhood high (TODO)", "TODO: what happened and why it mattered."),
    (2015, -3, "A low point (TODO)", "TODO: what happened and what you learned."),
    (2018, 2, "A turning point (TODO)", "TODO: what changed."),
    (2021, -2, "Another dip (TODO)", "TODO: what happened."),
    (2024, 4, "Started BS Computer Science", "TODO: why you chose CS."),
    (2026, 3, "Junior year", "TODO: what you're working toward now."),
]

# Skills are rated 0-10. Rename, add or remove skills freely (keep 4 or more per chart).
TECHNICAL = {"Python": 7, "Java": 7, "SQL": 7, "C#": 5, "Web dev": 5, "Data analysis": 6}
EVERYDAY = {"Communication": 7, "Time management": 5, "Teamwork": 8, "Problem solving": 7, "Adaptability": 6}
NICHE = {"Crossing the street": 9, "Intuition": 7, "Eyesight": 3, "Music taste": 9, "Parallel parking": 4}  # TODO

PROJECTS = [  # Edit the TODO parts to match what you actually did
    {
        "title": "Blottr",
        "emoji": "🗺️",
        "course": "Information Management 2",
        "role": "TODO: e.g. database designer and backend developer",
        "tools": ["SQL", "Spatial database", "Python"],
        "summary": "A spatial incident and crime blotter management platform for Cebu.",
        "outcome": "TODO: what was delivered and what you'd improve.",
        "link": "",
    },
    {
        "title": "DFA to Java Programs",
        "emoji": "🤖",
        "course": "CS313 Automata Theory",
        "role": "TODO: solo implementer",
        "tools": ["Java", "DFA design"],
        "summary": "Turned DFAs over {a, b} strings into working Java programs, using both switch-case and table-driven approaches.",
        "outcome": "TODO: what you learned comparing the two approaches.",
        "link": "",
    },
    {
        "title": "Automated Test Report Generator",
        "emoji": "📊",
        "course": "Knowles Hackathon",
        "role": "TODO: your role on the team",
        "tools": ["Python", "Pandas", "Reporting"],
        "summary": "Hackathon track for the QA department: generating historical test performance reports automatically.",
        "outcome": "TODO: the result of the hackathon.",
        "link": "",
    },
]

# =====================================================================
# Palette (centered on #3C0932) and page setup
# =====================================================================
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


# =====================================================================
# Sidebar: short about + contact form
# =====================================================================
with st.sidebar:
    st.image(get_photo(), use_container_width=True)
    st.subheader(NAME)
    st.caption(f"{PROGRAM}\n\n{SECTION}")
    st.write(SHORT_ABOUT)
    st.markdown(f"📍 {LOCATION}  \n📧 {EMAIL}  \n🔗 [GitHub]({GITHUB})")
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

# =====================================================================
# Top: full About (static)
# =====================================================================
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

tab_story, tab_skills, tab_projects = st.tabs(["📖 Autobiography", "🕸️ Skills", "🚀 Projects"])

# =====================================================================
# Autobiography with a life-line chart (ups and downs)
# =====================================================================
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

# =====================================================================
# Skills: three spider charts
# =====================================================================
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
        st.plotly_chart(radar("Niche", NICHE, ROSE, "rgba(181,119,159,0.30)"))
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

# =====================================================================
# Projects
# =====================================================================
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
                st.subheader(f"{p['emoji']} {p['title']}")
                st.caption(p["course"])
                st.write(p["summary"])
                st.markdown(f"**Role:** {p['role']}")
                st.markdown("**Tools:** " + ", ".join(f"`{t}`" for t in p["tools"]))
                st.markdown(f"**Outcome:** {p['outcome']}")
                if p["link"]:
                    st.link_button("View project", p["link"])

st.divider()
st.caption(f"© {date.today().year} {NAME} · {SECTION}")