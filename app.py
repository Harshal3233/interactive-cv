import streamlit as st

# -------------------------------------------------
# Page Config
# -------------------------------------------------
st.set_page_config(
    page_title="Harshal M Patel | AI Engineer",
    layout="wide",
)

# -------------------------------------------------
# Theme knobs (edit these if you want)
# -------------------------------------------------
ACCENT = "#111111"      # black accent (as you asked)
ACCENT_SOFT = "#f2f2f2" # light background for chips/cards
LINK = "#0b5fff"        # link blue

# -------------------------------------------------
# Styling (Less dull, cleaner hierarchy)
# -------------------------------------------------
st.markdown(
    f"""
<style>
/* Layout */
.block-container {{
    padding-top: 1.4rem;
    padding-bottom: 2.2rem;
    max-width: 1300px;
}}
section[data-testid="stSidebar"] > div {{
    padding-top: 1.4rem;
}}
/* Typography */
.h-name {{
    font-size: 2.4rem;
    font-weight: 900;
    letter-spacing: 0.2px;
    margin: 0;
}}
.h-tag {{
    font-size: 1.05rem;
    font-weight: 650;
    color: rgba(49, 51, 63, 0.78);
    margin-top: 0.2rem;
}}
.h-muted {{
    color: rgba(49, 51, 63, 0.68);
}}
.sec-title {{
    font-size: 1.35rem;
    font-weight: 900;
    margin: 1.25rem 0 0.6rem 0;
}}
/* Divider bar (fix that “blank space near headings”) */
.divider {{
    height: 6px;
    width: 70px;
    background: {ACCENT};
    border-radius: 999px;
    margin: 0.65rem 0 1.1rem 0;
}}
/* Cards */
.card {{
    border: 1px solid rgba(49, 51, 63, 0.14);
    border-radius: 16px;
    padding: 1.05rem 1.1rem;
    margin-bottom: 1rem;
    background: #fff;
}}
.card:hover {{
    border-color: rgba(49, 51, 63, 0.22);
}}
.card-title {{
    font-size: 1.15rem;
    font-weight: 850;
    margin-bottom: 0.15rem;
}}
.card-sub {{
    color: rgba(49, 51, 63, 0.68);
    font-size: 0.95rem;
    margin-bottom: 0.55rem;
}}
/* Pills */
.pill {{
    display: inline-block;
    padding: 0.26rem 0.65rem;
    margin: 0.18rem 0.30rem 0.12rem 0;
    border-radius: 999px;
    border: 1px solid rgba(49, 51, 63, 0.18);
    background: {ACCENT_SOFT};
    font-size: 0.86rem;
    color: rgba(49, 51, 63, 0.88);
}}
/* Sidebar cards */
.side-card {{
    border: 1px solid rgba(49, 51, 63, 0.14);
    border-radius: 16px;
    padding: 0.95rem 0.95rem;
    margin-bottom: 0.9rem;
    background: #fff;
}}
.side-title {{
    font-weight: 850;
    font-size: 1.02rem;
    margin-bottom: 0.45rem;
}}
.small {{
    font-size: 0.92rem;
}}
a {{
    color: {LINK} !important;
    text-decoration: none;
}}
a:hover {{
    text-decoration: underline;
}}
</style>
""",
    unsafe_allow_html=True,
)

# -------------------------------------------------
# Data
# -------------------------------------------------
PROFILE = {
    "name": "Harshal M Patel",
    "tagline": "AI Engineer | Data Science | Software Engineering | Analytics",
    "location": "Rome, Italy (available to relocate)",
    "email": "harshalmpatel2001@gmail.com",
    "phone": "+91 9974890592",
    "linkedin": "https://www.linkedin.com/in/harshal-patel-246306352/",
}

ABOUT = (
    "Driven by curiosity for technology and a passion for transforming data into meaningful insights, "
    "I bring analytical thinking, technical proficiency, and clear communication. My background across "
    "multiple institutions strengthened my adaptability and broadened my problem-solving approach. "
    "With strength in data management, model building and deployment, predictive analysis, and storytelling through data, "
    "along with sales and mentorship experience, I aim to deliver impactful, data-driven solutions with elegance."
)

EXPERIENCE = [
    {
        "title": "IT & Marketing Support",
        "org": "Vinayak Infotech (Ahmedabad, India)",
        "dates": "May 2024 – 2025",
        "bullets": [
            "Installed and configured computer systems and hardware.",
            "Mentored software team in Java and Python (advanced and libraries).",
            "Streamlined marketing workflows through technical support.",
        ],
        "tags": ["Python", "Java", "Mentorship", "IT Support", "Process Improvement"],
    },
    {
        "title": "Software Engineer",
        "org": "Cignex Datamatics (Gujarat, India)",
        "dates": "Aug 2022 – Jul 2023",
        "bullets": [
            "Developed testing scripts using Jira and collaborated with QA teams.",
            "Resolved bugs and improved system performance for multinational clients.",
            "Worked on Java-based systems in testing environments.",
        ],
        "tags": ["Java", "Jira", "QA", "Client Collaboration"],
    },
    {
        "title": "Software Engineering Intern",
        "org": "Axis Ray Technology (Gujarat, India)",
        "dates": "Jun 2022 – Dec 2022",
        "bullets": [
            "Built proficiency in Java, Advanced Java, and SQL-based data integration.",
            "Worked on real-world projects with cross-national teams.",
            "Mentored peers and supported successful delivery.",
        ],
        "tags": ["Advanced Java", "SQL", "Collaboration", "Mentorship"],
    },
    {
        "title": "Sales Executive",
        "org": "AURA ETHNICS",
        "dates": "Jan 2022 – Jun 2022",
        "bullets": [
            "Analyzed Google Analytics data to optimize online sales and customer journeys.",
            "Improved traffic and conversions by adjusting listings and promotions.",
            "Delivered personalized in-store customer experiences using brand storytelling.",
        ],
        "tags": ["Analytics", "Sales", "Customer Engagement", "Storytelling"],
    },
]

PROJECTS = [
    {
        "title": "Rome Airbnb Analysis and Price Prediction",
        "mini_desc": "Explored Rome Airbnb listings, visualized hotspots on an interactive map, and used an SVM classifier to predict price categories.",
        "subtitle": "EDA + interactive maps + SVM classification",
        "stack": ["Python (Advanced)", "EDA", "SVM", "Streamlit", "Data Storytelling"],
        "objective": "Analyze Airbnb listings in Rome, identify key price drivers, and classify listings into price categories.",
        "highlights": [
            "Room type and neighborhood are the strongest drivers of price.",
            "Central areas (Centro Storico, Trastevere) show significantly higher prices.",
            "Review count has weak correlation with price.",
            "Dashboard visualizes market hotspots and trends with clear explanations.",
        ],
        "github": "https://github.com/Harshal3233/rome-airbnb-streamlit",
        "live": "https://rome-airbnb-app-bsr6lkugduccvbrwmjfksk.streamlit.app/",
    },
    {
        "title": "Explainable ML for Agricultural Production (FAOSTAT + SHAP)",
        "mini_desc": "Built an interpretable Random Forest regression and used SHAP to explain cross-country differences in agricultural production drivers.",
        "subtitle": "Random Forest regression + SHAP explainability",
        "stack": ["Python (Advanced)", "Random Forest", "SHAP", "Streamlit", "Explainable AI"],
        "objective": "Compare crop-driven vs country-driven production patterns across Italy, France, Germany, and Spain using explainable ML.",
        "highlights": [
            "Italy and Spain appear predominantly crop-driven systems.",
            "France shows combined crop + scale-driven country effects.",
            "Germany demonstrates a more balanced influence structure.",
            "SHAP supports transparency and stakeholder-friendly interpretation.",
        ],
        "github": "https://github.com/Harshal3233/fao-shap-dashboard",
        "live": "https://fao-shap-dashboard-fyfzpqshuzcpfvz79m6xio.streamlit.app/",
    },
]

SKILLS = {
    "Programming & Data": [
        "Python (Advanced & Libraries)", "Advanced Java", "SQL",
        "EDA", "K-Means", "Regression", "Random Forest", "SVM", "Neural Networks",
        "Data Management", "Model Building & Deployment", "Predictive Analysis"
    ],
    "Tools": ["Streamlit", "VS Code", "Jupyter Notebook", "GitHub", "Jira", "MS Excel", "Google Workspace"],
    "Web & Design": ["HTML", "CSS", "JavaScript", "Figma", "Interactive Dashboards"],
}

EDUCATION = [
    {
        "title": "International Master in Data Science (Ongoing)",
        "meta": "Rome Business School | Rome, Italy",
        "bullets": [
            "Hands-on projects and Oracle labs to strengthen applied data science.",
            "Industry excursions with IBM and Owkin.",
        ],
    },
    {
        "title": "B.Tech in Computer Engineering (First Class Distinction)",
        "meta": "Swarrnim Institute of Technology & Startup | Gujarat, India | 2020 – 2024",
        "bullets": [
            "Debate Champion (2020–2021).",
            "University Student Council Member (2020–2024).",
            "Hackathon participation; supported Blood Donation Camp organization (2023).",
        ],
    },
]

LANGUAGES = "English (Native/Bilingual), Hindi (Native), Italian (Basic – improving)"

# -------------------------------------------------
# Helpers
# -------------------------------------------------
def pills(items):
    return "".join([f"<span class='pill'>{x}</span>" for x in items])

def section_header(title: str):
    st.markdown(f"<div class='sec-title'>{title}</div>", unsafe_allow_html=True)
    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

def experience_card(e):
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown(f"<div class='card-title'>{e['title']}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='card-sub'>{e['org']} • {e['dates']}</div>", unsafe_allow_html=True)
    st.write("\n".join([f"- {b}" for b in e["bullets"]]))
    st.markdown(pills(e["tags"]), unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

def project_card(p, show_full=False):
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown(f"<div class='card-title'>{p['title']}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='card-sub'>{p['subtitle']}</div>", unsafe_allow_html=True)

    # Small description (you asked for this)
    st.markdown(f"<div class='small'>{p['mini_desc']}</div>", unsafe_allow_html=True)
    st.markdown("<div style='height:0.4rem'></div>", unsafe_allow_html=True)

    st.markdown(pills(p["stack"]), unsafe_allow_html=True)

    c1, c2 = st.columns(2)
    with c1:
        st.link_button("GitHub Repo", p["github"], use_container_width=True)
    with c2:
        st.link_button("Live Streamlit App", p["live"], use_container_width=True)

    if show_full:
        st.markdown("<div style='height:0.5rem'></div>", unsafe_allow_html=True)
        st.markdown("**Objective**")
        st.write(p["objective"])
        st.markdown("**Key Highlights**")
        st.write("\n".join([f"- {h}" for h in p["highlights"]]))

    st.markdown("</div>", unsafe_allow_html=True)

# -------------------------------------------------
# Sidebar (Make it useful, not idle)
# -------------------------------------------------
with st.sidebar:
    st.markdown("<div class='side-card'>", unsafe_allow_html=True)
    st.markdown("<div class='side-title'>Profile</div>", unsafe_allow_html=True)
    st.markdown(f"**{PROFILE['name']}**", unsafe_allow_html=True)
    st.markdown(f"<span class='small'>{PROFILE['tagline']}</span>", unsafe_allow_html=True)
    st.markdown(f"<div class='h-muted small'>{PROFILE['location']}</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='side-card'>", unsafe_allow_html=True)
    st.markdown("<div class='side-title'>Quick Links</div>", unsafe_allow_html=True)
    st.link_button("LinkedIn", PROFILE["linkedin"], use_container_width=True)
    st.link_button("Rome Airbnb App", PROJECTS[0]["live"], use_container_width=True)
    st.link_button("FAO SHAP App", PROJECTS[1]["live"], use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='side-card'>", unsafe_allow_html=True)
    st.markdown("<div class='side-title'>Skills Snapshot</div>", unsafe_allow_html=True)
    st.markdown(pills(["Python", "SQL", "EDA", "SVM", "Random Forest", "SHAP", "Streamlit"]), unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='side-card'>", unsafe_allow_html=True)
    st.markdown("<div class='side-title'>Contact</div>", unsafe_allow_html=True)
    st.markdown(f"<span class='small'> {PROFILE['email']}</span>", unsafe_allow_html=True)
    st.markdown(f"<span class='small'> {PROFILE['phone']}</span>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("### Navigation")
    section = st.radio(
        "Go to",
        ["Overview", "Experience", "Projects", "Skills", "Education", "Languages"],
        index=0,
        label_visibility="collapsed",
    )

# -------------------------------------------------
# Header (Main)
# -------------------------------------------------
st.markdown(f"<div class='h-name'>{PROFILE['name']}</div>", unsafe_allow_html=True)
st.markdown(f"<div class='h-tag'>{PROFILE['tagline']}</div>", unsafe_allow_html=True)
st.markdown(f"<div class='h-muted'>{PROFILE['location']}</div>", unsafe_allow_html=True)
st.write(f" {PROFILE['email']}   |    {PROFILE['phone']}   |    {PROFILE['linkedin']}")

# Strong black divider bar under header (visual punch)
st.markdown("<div class='divider' style='width:110px; height:7px;'></div>", unsafe_allow_html=True)

# -------------------------------------------------
# Sections (scrollable, no weird blank gaps)
# -------------------------------------------------
if section == "Overview":
    section_header("About Me")
    st.write(ABOUT)

    section_header("Featured Projects")
    for p in PROJECTS:
        project_card(p, show_full=False)

    section_header("What I Deliver")
    st.markdown(
        pills([
            "Data Management",
            "EDA + Storytelling",
            "Model Building",
            "Deployment (Streamlit)",
            "Predictive Analysis",
            "Stakeholder-friendly Insights",
        ]),
        unsafe_allow_html=True,
    )

elif section == "Experience":
    section_header("Professional Experience")
    for e in EXPERIENCE:
        experience_card(e)

elif section == "Projects":
    section_header("Projects")
    st.markdown(
        "<div class='h-muted small'>Each project includes a quick summary + full objective and highlights.</div>",
        unsafe_allow_html=True
    )
    st.markdown("<div style='height:0.6rem'></div>", unsafe_allow_html=True)
    for p in PROJECTS:
        project_card(p, show_full=True)

elif section == "Skills":
    section_header("Skills")
    for k, items in SKILLS.items():
        st.markdown(f"**{k}**")
        st.markdown(pills(items), unsafe_allow_html=True)
        st.markdown("<div style='height:0.5rem'></div>", unsafe_allow_html=True)

elif section == "Education":
    section_header("Education")
    for ed in EDUCATION:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown(f"<div class='card-title'>{ed['title']}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='card-sub'>{ed['meta']}</div>", unsafe_allow_html=True)
        st.write("\n".join([f"- {b}" for b in ed["bullets"]]))
        st.markdown("</div>", unsafe_allow_html=True)

elif section == "Languages":
    section_header("Languages")
    st.write(LANGUAGES)

# Footer (subtle)
st.markdown("<div style='height:0.8rem'></div>", unsafe_allow_html=True)
st.markdown(
    "<div class='h-muted small'>Tip: Add this Streamlit URL to your PDF CV and LinkedIn “Featured” section.</div>",
    unsafe_allow_html=True
)
