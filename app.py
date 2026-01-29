import streamlit as st
import streamlit.components.v1 as components

# -------------------------------------------------
# Page Config
# -------------------------------------------------
st.set_page_config(
    page_title="Harshal M Patel | AI Engineer",
    layout="wide",
)

# -------------------------------------------------
# Brand / UI tokens (professional)
# -------------------------------------------------
BRAND = {
    "bg": "#ffffff",
    "text": "#111827",        # slate-900
    "muted": "#6b7280",       # gray-500
    "border": "rgba(17, 24, 39, 0.12)",
    "soft": "rgba(17, 24, 39, 0.04)",
    "accent": "#2563eb",      # blue-600
    "accent2": "#7c3aed",     # violet-600
    "chip": "rgba(37, 99, 235, 0.10)",
}

# -------------------------------------------------
# CSS (clean + impressive, no loud bars)
# -------------------------------------------------
st.markdown(
    f"""
<style>
/* Layout */
.block-container {{
    padding-top: 1.5rem;
    padding-bottom: 2.5rem;
    max-width: 1200px;
}}
section[data-testid="stSidebar"] > div {{
    padding-top: 1.1rem;
}}

/* Typography */
h1, h2, h3 {{
    letter-spacing: 0.2px;
}}
.small-muted {{
    color: {BRAND["muted"]};
    font-size: 0.95rem;
}}
.kicker {{
    color: {BRAND["muted"]};
    font-weight: 650;
    font-size: 0.98rem;
    margin-top: -0.25rem;
}}

/* Hero banner */
.hero {{
    border: 1px solid {BRAND["border"]};
    border-radius: 18px;
    padding: 1.15rem 1.2rem;
    background:
        radial-gradient(1200px 200px at 20% -20%, {BRAND["chip"]}, transparent 60%),
        radial-gradient(1200px 200px at 90% 0%, rgba(124, 58, 237, 0.10), transparent 55%),
        {BRAND["bg"]};
}}
.hero-title {{
    font-size: 2.15rem;
    font-weight: 900;
    color: {BRAND["text"]};
    margin-bottom: 0.15rem;
}}
.hero-tag {{
    font-size: 1.05rem;
    font-weight: 700;
    color: rgba(17, 24, 39, 0.78);
}}
.hero-meta {{
    color: {BRAND["muted"]};
    margin-top: 0.25rem;
}}

/* Section header */
.section-title {{
    font-size: 1.35rem;
    font-weight: 900;
    margin: 1.6rem 0 0.55rem 0;
    color: {BRAND["text"]};
}}
.section-line {{
    height: 2px;
    width: 88px;
    border-radius: 999px;
    background: linear-gradient(90deg, {BRAND["accent"]}, {BRAND["accent2"]});
    margin-bottom: 0.95rem;
}}

/* Cards */
.card {{
    border: 1px solid {BRAND["border"]};
    border-radius: 18px;
    padding: 1.05rem 1.1rem;
    background: {BRAND["bg"]};
    margin-bottom: 0.95rem;
}}
.card:hover {{
    border-color: rgba(17, 24, 39, 0.20);
}}
.card-title {{
    font-size: 1.10rem;
    font-weight: 900;
    margin-bottom: 0.10rem;
    color: {BRAND["text"]};
}}
.card-sub {{
    color: {BRAND["muted"]};
    font-size: 0.95rem;
    margin-bottom: 0.55rem;
}}

/* Pills */
.pill {{
    display: inline-block;
    padding: 0.23rem 0.62rem;
    margin: 0.16rem 0.28rem 0.10rem 0;
    border-radius: 999px;
    border: 1px solid {BRAND["border"]};
    background: {BRAND["soft"]};
    font-size: 0.84rem;
    color: rgba(17, 24, 39, 0.85);
}}

/* Sidebar cards */
.side-card {{
    border: 1px solid {BRAND["border"]};
    border-radius: 18px;
    padding: 0.95rem 0.95rem;
    background: {BRAND["bg"]};
    margin-bottom: 0.85rem;
}}
.side-title {{
    font-weight: 900;
    color: {BRAND["text"]};
    margin-bottom: 0.45rem;
    font-size: 1.02rem;
}}
.navbtn {{
    display: block;
    padding: 0.55rem 0.75rem;
    border: 1px solid {BRAND["border"]};
    border-radius: 12px;
    background: {BRAND["bg"]};
    color: {BRAND["text"]};
    font-weight: 700;
    text-decoration: none !important;
    margin: 0.35rem 0;
}}
.navbtn:hover {{
    border-color: rgba(17, 24, 39, 0.22);
    background: {BRAND["soft"]};
}}
.badge {{
    display: inline-block;
    padding: 0.22rem 0.55rem;
    border-radius: 999px;
    background: rgba(37, 99, 235, 0.12);
    color: rgba(37, 99, 235, 0.95);
    font-weight: 800;
    font-size: 0.82rem;
    margin-right: 0.4rem;
}}

/* Hide Streamlit anchor markdown spacing a bit */
.anchor {{
    height: 1px;
    margin-top: -70px;
    padding-top: 70px;
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
    "AI Engineer with a strong foundation in data management, predictive analysis, and model development. "
    "I combine analytical thinking with clear communication and a product mindset: explore the data, build the model, "
    "explain the story, and ship something usable."
)

EXPERIENCE = [
    {
        "role": "IT & Marketing Support",
        "company": "Vinayak Infotech",
        "meta": "Ahmedabad, India • May 2024 – 2025",
        "bullets": [
            "Installed and configured computer systems and hardware.",
            "Mentored software team in Java and Python (advanced and libraries) and supported testing tasks.",
            "Streamlined marketing workflows through technical support and process improvements.",
        ],
        "tags": ["Python", "Java", "Mentorship", "IT Support", "Process Improvement"],
    },
    {
        "role": "Software Engineer",
        "company": "Cignex Datamatics",
        "meta": "Gujarat, India • Aug 2022 – Jul 2023",
        "bullets": [
            "Developed testing scripts using Jira and collaborated with QA teams.",
            "Resolved bugs and improved system performance for multinational clients.",
            "Worked on Java-based systems and testing environments to enhance reliability.",
        ],
        "tags": ["Java", "Jira", "QA", "Client Collaboration"],
    },
    {
        "role": "Software Engineering Intern",
        "company": "Axis Ray Technology",
        "meta": "Gujarat, India • Jun 2022 – Dec 2022",
        "bullets": [
            "Built proficiency in Java, Advanced Java, and SQL-based data integration.",
            "Worked on real-world projects with cross-national teams.",
            "Supported peers through mentoring and collaborative delivery.",
        ],
        "tags": ["Advanced Java", "SQL", "Collaboration", "Mentorship"],
    },
    {
        "role": "Sales Executive",
        "company": "AURA ETHNICS",
        "meta": "Jan 2022 – Jun 2022",
        "bullets": [
            "Used Google Analytics insights to optimize online sales and customer journeys.",
            "Improved traffic and conversions by adjusting listings and promotions.",
            "Delivered personalized in-store customer experiences using brand storytelling.",
        ],
        "tags": ["Analytics", "Sales", "Customer Engagement", "Storytelling"],
    },
]

PROJECTS = [
    {
        "title": "Rome Airbnb Analysis and Price Prediction",
        "one_liner": "EDA + interactive mapping + SVM classifier to categorize listing prices in Rome.",
        "summary": (
            "Built a data storytelling dashboard to understand Airbnb pricing in Rome. "
            "Explored the dataset with EDA, mapped price hotspots, and trained an SVM classifier to predict price categories."
        ),
        "impact": [
            "Identified room type + neighborhood as primary price drivers.",
            "Highlighted premium zones (Centro Storico, Trastevere) using map-based insights.",
            "Delivered a stakeholder-friendly dashboard with clear charts and explanations.",
        ],
        "stack": ["Python (Advanced)", "EDA", "SVM", "Streamlit", "Data Storytelling"],
        "github": "https://github.com/Harshal3233/rome-airbnb-streamlit",
        "live": "https://rome-airbnb-app-bsr6lkugduccvbrwmjfksk.streamlit.app/",
        "tags": ["EDA", "Maps", "ML", "Streamlit"],
    },
    {
        "title": "Explainable ML for Agricultural Production (FAOSTAT + SHAP)",
        "one_liner": "Random Forest + SHAP to explain cross-country production drivers (crop vs country effects).",
        "summary": (
            "Created an explainable ML dashboard to compare agricultural production patterns across Italy, France, Germany, and Spain. "
            "Used Random Forest as an interpretive model and SHAP to quantify feature influence transparently."
        ),
        "impact": [
            "Compared how crop choice vs country context influences production outcomes.",
            "Produced stakeholder-ready explanations using SHAP contributions.",
            "Reported model quality with MAE, Relative MAE, and R² for transparency.",
        ],
        "stack": ["Python (Advanced)", "Random Forest", "SHAP", "Explainable AI", "Streamlit"],
        "github": "https://github.com/Harshal3233/fao-shap-dashboard",
        "live": "https://fao-shap-dashboard-fyfzpqshuzcpfvz79m6xio.streamlit.app/",
        "tags": ["XAI", "SHAP", "ML", "Streamlit"],
    },
]

SKILLS = {
    "Programming & Data": [
        "Python (Advanced & Libraries)", "Advanced Java", "SQL",
        "EDA", "K-Means", "Regression", "Random Forest", "SVM", "Neural Networks",
        "Data Management", "Model Building & Deployment", "Predictive Analysis",
    ],
    "Tools & Platforms": ["Streamlit", "VS Code", "Jupyter Notebook", "GitHub", "Jira", "MS Excel", "Google Workspace"],
    "Web & Design": ["HTML", "CSS", "JavaScript", "Figma", "Interactive Dashboards"],
}

EDUCATION = [
    {
        "title": "International Master in Data Science (Ongoing)",
        "meta": "Rome Business School | Rome, Italy",
        "bullets": ["Hands-on projects and Oracle labs.", "Industry excursions with IBM and Owkin."],
    },
    {
        "title": "B.Tech in Computer Engineering (First Class Distinction)",
        "meta": "Swarrnim Institute of Technology & Startup | Gujarat, India | 2020 – 2024",
        "bullets": ["Debate Champion (2020–2021).", "Student Council Member (2020–2024).", "Hackathons; Blood Donation Camp (2023)."],
    },
]

LANGUAGES = "English (Native/Bilingual), Hindi (Native), Italian (Basic – improving)"

# -------------------------------------------------
# Helpers
# -------------------------------------------------
def pills(items):
    return "".join([f"<span class='pill'>{x}</span>" for x in items])

def anchor(anchor_id: str):
    st.markdown(f"<div id='{anchor_id}' class='anchor'></div>", unsafe_allow_html=True)

def section(title: str, subtitle: str | None = None):
    st.markdown(f"<div class='section-title'>{title}</div>", unsafe_allow_html=True)
    st.markdown("<div class='section-line'></div>", unsafe_allow_html=True)
    if subtitle:
        st.markdown(f"<div class='small-muted' style='margin-top:-0.4rem; margin-bottom:0.8rem;'>{subtitle}</div>", unsafe_allow_html=True)

def card_open():
    st.markdown("<div class='card'>", unsafe_allow_html=True)

def card_close():
    st.markdown("</div>", unsafe_allow_html=True)

# -------------------------------------------------
# Sidebar (impressive + useful)
# -------------------------------------------------
with st.sidebar:
    st.markdown("<div class='side-card'>", unsafe_allow_html=True)
    st.markdown("<div class='side-title'>Harshal M Patel</div>", unsafe_allow_html=True)
    st.markdown(f"<span class='badge'>AI Engineer</span><span class='small-muted'>{PROFILE['location']}</span>", unsafe_allow_html=True)
    st.markdown(f"<div class='small-muted' style='margin-top:0.55rem;'>📧 {PROFILE['email']}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='small-muted'> {PROFILE['phone']}</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='side-card'>", unsafe_allow_html=True)
    st.markdown("<div class='side-title'>Quick Actions</div>", unsafe_allow_html=True)
    st.link_button("LinkedIn", PROFILE["linkedin"], use_container_width=True)
    st.link_button("Rome Airbnb Live App", PROJECTS[0]["live"], use_container_width=True)
    st.link_button("FAO SHAP Live App", PROJECTS[1]["live"], use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='side-card'>", unsafe_allow_html=True)
    st.markdown("<div class='side-title'>Jump to</div>", unsafe_allow_html=True)
    st.markdown(
        """
<a class="navbtn" href="#about">About</a>
<a class="navbtn" href="#experience">Experience</a>
<a class="navbtn" href="#projects">Projects</a>
<a class="navbtn" href="#skills">Skills</a>
<a class="navbtn" href="#education">Education</a>
<a class="navbtn" href="#languages">Languages</a>
<a class="navbtn" href="#contact">Contact</a>
""",
        unsafe_allow_html=True,
    )
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='side-card'>", unsafe_allow_html=True)
    st.markdown("<div class='side-title'>Project Filters</div>", unsafe_allow_html=True)
    all_tags = sorted({t for p in PROJECTS for t in p["tags"]})
    selected_tags = st.multiselect("Filter by tags", all_tags, default=[])
    show_previews = st.toggle("Embed live previews", value=False)
    st.markdown("</div>", unsafe_allow_html=True)

# -------------------------------------------------
# Hero (top)
# -------------------------------------------------
st.markdown("<div class='hero'>", unsafe_allow_html=True)
left, right = st.columns([0.68, 0.32], vertical_alignment="top")

with left:
    st.markdown(f"<div class='hero-title'>{PROFILE['name']}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='hero-tag'>{PROFILE['tagline']}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='hero-meta'>{PROFILE['location']}</div>", unsafe_allow_html=True)
    st.markdown("<div style='height:0.6rem;'></div>", unsafe_allow_html=True)
    st.write(ABOUT)

with right:
    # Mini KPI style widgets (impressive but professional)
    st.metric("Deployed Projects", "2")
    st.metric("Focus", "AI + Analytics")
    st.metric("Location", "Rome")

    b1, b2 = st.columns(2)
    with b1:
        st.link_button("LinkedIn", PROFILE["linkedin"], use_container_width=True)
    with b2:
        st.link_button("Contact", "#contact", use_container_width=True)

st.markdown("</div>", unsafe_allow_html=True)

# -------------------------------------------------
# About
# -------------------------------------------------
anchor("about")
section("About", "How I work: explore, model, explain, ship.")
card_open()
st.write(
    "I enjoy projects where data becomes a decision. My approach is structured:"
    "\n- **EDA first** to understand patterns and edge cases"
    "\n- **Modeling** with clear baselines and explainability when needed"
    "\n- **Storytelling** with dashboards and clean narratives"
    "\n- **Delivery** through usable apps (Streamlit) and reproducible repos"
)
st.markdown(pills(["EDA", "Predictive Analysis", "Model Building", "Deployment", "Data Storytelling"]), unsafe_allow_html=True)
card_close()

# -------------------------------------------------
# Experience
# -------------------------------------------------
anchor("experience")
section("Experience", "Evidence of delivery, collaboration, and ownership.")
for e in EXPERIENCE:
    card_open()
    st.markdown(f"<div class='card-title'>{e['role']} • {e['company']}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='card-sub'>{e['meta']}</div>", unsafe_allow_html=True)
    st.write("\n".join([f"- {b}" for b in e["bullets"]]))
    st.markdown(pills(e["tags"]), unsafe_allow_html=True)
    card_close()

# -------------------------------------------------
# Projects (impressive case-study style)
# -------------------------------------------------
anchor("projects")
section("Projects", "Two shipped projects: live apps + clean repos. Click-worthy.")

def tag_match(project):
    if not selected_tags:
        return True
    return any(t in project["tags"] for t in selected_tags)

for p in [x for x in PROJECTS if tag_match(x)]:
    card_open()

    top = st.columns([0.72, 0.28], vertical_alignment="top")
    with top[0]:
        st.markdown(f"<div class='card-title'>{p['title']}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='card-sub'>{p['one_liner']}</div>", unsafe_allow_html=True)
        st.markdown(pills(p["stack"]), unsafe_allow_html=True)

    with top[1]:
        st.link_button("Live App", p["live"], use_container_width=True)
        st.link_button("GitHub Repo", p["github"], use_container_width=True)

    # Summary + impact bullets (what recruiters want fast)
    st.markdown("**Summary**")
    st.write(p["summary"])

    st.markdown("**Highlights**")
    st.write("\n".join([f"- {x}" for x in p["impact"]]))

    # Optional embedded preview (very impressive)
    if show_previews:
        with st.expander("Preview live app inside this CV"):
            components.iframe(p["live"], height=560, scrolling=True)

    card_close()

# -------------------------------------------------
# Skills
# -------------------------------------------------
anchor("skills")
section("Skills", "Core stack and strengths.")
skills_cols = st.columns(3)
for i, (k, items) in enumerate(SKILLS.items()):
    with skills_cols[i]:
        card_open()
        st.markdown(f"<div class='card-title'>{k}</div>", unsafe_allow_html=True)
        st.markdown(pills(items), unsafe_allow_html=True)
        card_close()

# -------------------------------------------------
# Education
# -------------------------------------------------
anchor("education")
section("Education", "Academic foundation and industry exposure.")
for ed in EDUCATION:
    card_open()
    st.markdown(f"<div class='card-title'>{ed['title']}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='card-sub'>{ed['meta']}</div>", unsafe_allow_html=True)
    st.write("\n".join([f"- {b}" for b in ed["bullets"]]))
    card_close()

# -------------------------------------------------
# Languages
# -------------------------------------------------
anchor("languages")
section("Languages")
card_open()
st.write(LANGUAGES)
card_close()

# -------------------------------------------------
# Contact
# -------------------------------------------------
anchor("contact")
section("Contact", "Fastest way to reach me.")
card_open()
c1, c2 = st.columns([0.55, 0.45], vertical_alignment="top")
with c1:
    st.write(f"- **Email:** {PROFILE['email']}")
    st.write(f"- **Phone:** {PROFILE['phone']}")
    st.write(f"- **LinkedIn:** {PROFILE['linkedin']}")
with c2:
    st.link_button("Open LinkedIn", PROFILE["linkedin"], use_container_width=True)
    st.link_button("Rome Airbnb Live App", PROJECTS[0]["live"], use_container_width=True)
    st.link_button("FAO SHAP Live App", PROJECTS[1]["live"], use_container_width=True)
card_close()

st.markdown("<div class='small-muted' style='margin-top:1.2rem;'>Built with Streamlit • Deployed on Streamlit Cloud</div>", unsafe_allow_html=True)
