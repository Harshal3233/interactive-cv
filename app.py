import streamlit as st

# -------------------------------------------------
# Page Config
# -------------------------------------------------
st.set_page_config(
    page_title="Harshal M Patel | AI Engineer",
    layout="wide",
)

# -------------------------------------------------
# Subtle Professional Styling (no thick lines, no weird fonts)
# -------------------------------------------------
st.markdown(
    """
<style>
/* Keep Streamlit default font, just refine spacing */
.block-container { padding-top: 1.6rem; padding-bottom: 2.2rem; max-width: 1200px; }

h1, h2, h3 { letter-spacing: 0.2px; }
.small-muted { color: rgba(49, 51, 63, 0.70); font-size: 0.95rem; }
.kicker { color: rgba(49, 51, 63, 0.70); font-weight: 600; font-size: 0.95rem; margin-top: -0.25rem; }

.divider { height: 1px; background: rgba(49, 51, 63, 0.12); margin: 1rem 0 1.1rem 0; border-radius: 999px; }
.section-title { font-size: 1.35rem; font-weight: 800; margin: 1.4rem 0 0.6rem 0; }
.section-sub { color: rgba(49, 51, 63, 0.72); margin-top: -0.2rem; }

.card {
  border: 1px solid rgba(49, 51, 63, 0.14);
  border-radius: 16px;
  padding: 1rem 1.1rem;
  background: white;
  margin-bottom: 0.9rem;
}

.pill {
  display: inline-block;
  padding: 0.22rem 0.55rem;
  margin: 0.15rem 0.25rem 0.1rem 0;
  border: 1px solid rgba(49, 51, 63, 0.18);
  border-radius: 999px;
  font-size: 0.85rem;
  color: rgba(49, 51, 63, 0.85);
  background: rgba(49, 51, 63, 0.03);
}

/* Sidebar spacing */
section[data-testid="stSidebar"] > div { padding-top: 1.1rem; }
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
    "along with sales and mentorship experience, I deliver impactful, data-driven solutions with elegance."
)

EXPERIENCE = [
    {
        "role": "IT & Marketing Support",
        "company": "Vinayak Infotech",
        "location": "Ahmedabad, India",
        "dates": "May 2024 – 2025",
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
        "location": "Gujarat, India",
        "dates": "Aug 2022 – Jul 2023",
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
        "location": "Gujarat, India",
        "dates": "Jun 2022 – Dec 2022",
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
        "location": "",
        "dates": "Jan 2022 – Jun 2022",
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
        "short": "EDA + interactive map of hotspots + SVM classifier to predict price categories for Rome Airbnb listings.",
        "objective": "Analyze Airbnb listings in Rome, understand drivers of pricing, and classify listings into price categories.",
        "methods": [
            "EDA: histograms, boxplots, bar charts, scatter plots for price, room types, neighborhoods, and reviews.",
            "Interactive map visualization of listing distribution and price hotspots.",
            "ML: SVM classifier using room type, neighborhood, capacity, and other features.",
        ],
        "findings": [
            "Room type and neighborhood are strongest factors affecting price.",
            "Central areas (Centro Storico, Trastevere) show significantly higher prices.",
            "Review count has weak correlation with price.",
            "Dashboard clearly visualizes market hotspots and trends.",
        ],
        "tags": ["EDA", "SVM", "Streamlit", "Data Storytelling"],
        "github": "https://github.com/Harshal3233/rome-airbnb-streamlit",
        "live": "https://rome-airbnb-app-bsr6lkugduccvbrwmjfksk.streamlit.app/",
    },
    {
        "title": "Explainable ML for Agricultural Production (FAOSTAT + SHAP)",
        "short": "Random Forest regression + SHAP to explain cross-country drivers (crop vs country) for production differences.",
        "objective": "Compare crop-driven vs country-driven production patterns across Italy, France, Germany, and Spain using explainable ML.",
        "methods": [
            "Random Forest regression (interpretive model, not forecasting).",
            "SHAP explainability to quantify feature contributions and compare drivers across countries.",
            "Transparent evaluation using MAE, Relative MAE, and R² for scale-aware assessment.",
        ],
        "findings": [
            "Italy and Spain appear predominantly crop-driven systems.",
            "France shows combined crop effects with scale-driven country influence.",
            "Germany demonstrates a more balanced influence structure.",
            "SHAP supports transparent, stakeholder-friendly interpretation.",
        ],
        "tags": ["Random Forest", "SHAP", "Explainable AI", "Streamlit"],
        "github": "https://github.com/Harshal3233/fao-shap-dashboard",
        "live": "https://fao-shap-dashboard-fyfzpqshuzcpfvz79m6xio.streamlit.app/",
    },
]

SKILLS = {
    "Programming & Data": [
        "Python (Advanced & Libraries)", "Advanced Java", "SQL",
        "EDA", "K-Means", "Regression", "Random Forest", "SVM", "Neural Networks",
        "Data Management", "Model Building & Deployment", "Predictive Analysis",
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
            "Hackathons; supported Blood Donation Camp organization (2023).",
        ],
    },
]

LANGUAGES = "English (Native/Bilingual), Hindi (Native), Italian (Basic – improving)"

# -------------------------------------------------
# Helpers
# -------------------------------------------------
def pills(items):
    return "".join([f"<span class='pill'>{x}</span>" for x in items])

def anchor(anchor_id: str):
    st.markdown(f"<div id='{anchor_id}'></div>", unsafe_allow_html=True)

def section(title: str, subtitle: str | None = None):
    st.markdown(f"<div class='section-title'>{title}</div>", unsafe_allow_html=True)
    if subtitle:
        st.markdown(f"<div class='section-sub'>{subtitle}</div>", unsafe_allow_html=True)
    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

def card_open():
    st.markdown("<div class='card'>", unsafe_allow_html=True)

def card_close():
    st.markdown("</div>", unsafe_allow_html=True)

# -------------------------------------------------
# Sidebar (useful + “interactive” but not blocking scroll)
# -------------------------------------------------
with st.sidebar:
    st.markdown("### Quick Navigation")
    st.markdown(
        """
- [Overview](#overview)
- [Experience](#experience)
- [Projects](#projects)
- [Skills](#skills)
- [Education](#education)
- [Languages](#languages)
- [Contact](#contact)
""",
        unsafe_allow_html=True,
    )

    st.markdown("### Quick Links")
    st.link_button("LinkedIn", PROFILE["linkedin"], use_container_width=True)
    st.link_button("Rome Airbnb App", PROJECTS[0]["live"], use_container_width=True)
    st.link_button("FAO SHAP App", PROJECTS[1]["live"], use_container_width=True)

    st.markdown("### Project Filter")
    all_tags = sorted({t for p in PROJECTS for t in p["tags"]})
    selected_tags = st.multiselect("Show projects with tags:", all_tags, default=[])

    st.markdown("### Snapshot")
    st.markdown(pills(["Python", "SQL", "EDA", "SVM", "Random Forest", "SHAP", "Streamlit"]), unsafe_allow_html=True)

# -------------------------------------------------
# MAIN PAGE (Single continuous scroll)
# -------------------------------------------------
anchor("overview")
st.title(PROFILE["name"])
st.markdown(f"<div class='kicker'>{PROFILE['tagline']}</div>", unsafe_allow_html=True)
st.markdown(f"<div class='small-muted'>{PROFILE['location']}</div>", unsafe_allow_html=True)

c1, c2, c3 = st.columns([0.34, 0.33, 0.33])
with c1:
    st.markdown(f"**Email:** {PROFILE['email']}")
with c2:
    st.markdown(f"**Phone:** {PROFILE['phone']}")
with c3:
    st.markdown(f"**LinkedIn:** {PROFILE['linkedin']}")

st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

section("About", "A quick summary of what I do and how I work.")
st.write(ABOUT)

# Experience
anchor("experience")
section("Experience", "Roles that shaped my execution, communication, and delivery.")
for e in EXPERIENCE:
    card_open()
    top = f"{e['role']} | {e['company']}"
    meta = f"{e['location']} • {e['dates']}".strip(" •")
    st.markdown(f"**{top}**")
    st.markdown(f"<div class='small-muted'>{meta}</div>", unsafe_allow_html=True)
    st.write("\n".join([f"- {b}" for b in e["bullets"]]))
    st.markdown(pills(e["tags"]), unsafe_allow_html=True)
    card_close()

# Projects
anchor("projects")
section("Projects", "Two deployed projects with GitHub repos and live apps.")

def tag_match(p):
    if not selected_tags:
        return True
    p_tags = set(p["tags"])
    return any(t in p_tags for t in selected_tags)

for p in [x for x in PROJECTS if tag_match(x)]:
    card_open()
    st.subheader(p["title"])
    st.markdown(f"<div class='small-muted'>{p['short']}</div>", unsafe_allow_html=True)
    st.markdown(pills(p["tags"]), unsafe_allow_html=True)

    b1, b2, b3 = st.columns([0.22, 0.25, 0.53])
    with b1:
        st.link_button("GitHub", p["github"], use_container_width=True)
    with b2:
        st.link_button("Live App", p["live"], use_container_width=True)

    with st.expander("See full project details"):
        st.markdown("**Objective**")
        st.write(p["objective"])
        st.markdown("**Methods**")
        st.write("\n".join([f"- {m}" for m in p["methods"]]))
        st.markdown("**Key Findings**")
        st.write("\n".join([f"- {f}" for f in p["findings"]]))
    card_close()

# Skills
anchor("skills")
section("Skills", "Core technical and professional capabilities.")
for k, items in SKILLS.items():
    st.markdown(f"**{k}**")
    st.markdown(pills(items), unsafe_allow_html=True)
    st.markdown("")

# Education
anchor("education")
section("Education", "Academic path and industry exposure.")
for ed in EDUCATION:
    card_open()
    st.markdown(f"**{ed['title']}**")
    st.markdown(f"<div class='small-muted'>{ed['meta']}</div>", unsafe_allow_html=True)
    st.write("\n".join([f"- {b}" for b in ed["bullets"]]))
    card_close()

# Languages
anchor("languages")
section("Languages")
st.write(LANGUAGES)

# Contact
anchor("contact")
section("Contact", "Fastest ways to reach me.")
card_open()
st.write(f"- **Email:** {PROFILE['email']}")
st.write(f"- **Phone:** {PROFILE['phone']}")
st.write(f"- **LinkedIn:** {PROFILE['linkedin']}")
card_close()
