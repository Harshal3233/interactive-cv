import streamlit as st
from pathlib import Path

# -------------------------------------------------
# Page Config
# -------------------------------------------------
st.set_page_config(
    page_title="Harshal M Patel | AI Engineer",
    layout="wide"
)

# -------------------------------------------------
# Styling (Professional UI)
# -------------------------------------------------
st.markdown("""
<style>
.block-container { padding-top: 2rem; padding-bottom: 2rem; max-width: 1150px; }
.name { font-size: 2.25rem; font-weight: 850; letter-spacing: 0.2px; }
.tagline { font-size: 1.05rem; font-weight: 650; color: rgba(49, 51, 63, 0.82); margin-top: 0.25rem; }
.muted { color: rgba(49, 51, 63, 0.68); }
.section { font-size: 1.35rem; font-weight: 800; margin-top: 2rem; margin-bottom: 0.6rem; }
.card {
    border: 1px solid rgba(49, 51, 63, 0.14);
    border-radius: 14px;
    padding: 1.15rem 1.15rem;
    margin-bottom: 1rem;
    background: #ffffff;
}
.pill {
    display: inline-block;
    padding: 0.28rem 0.65rem;
    margin: 0.2rem 0.3rem 0.15rem 0;
    border-radius: 999px;
    border: 1px solid rgba(49, 51, 63, 0.18);
    font-size: 0.86rem;
    color: rgba(49, 51, 63, 0.80);
    background: rgba(49, 51, 63, 0.02);
}
hr { border: none; height: 1px; background: rgba(49, 51, 63, 0.12); margin: 1.25rem 0; }
.small { font-size: 0.93rem; }
a { text-decoration: none; }
</style>
""", unsafe_allow_html=True)

# -------------------------------------------------
# Data (Edit-friendly)
# -------------------------------------------------
PROFILE = {
    "name": "Harshal M Patel",
    "tagline": "AI Engineer | Data Science | Software Engineering | Analytics",
    "location": "Rome, Italy (available to relocate)",
    "email": "harshalmpatel2001@gmail.com",
    "phone": "+91 9974890592",
    "linkedin_url": "https://www.linkedin.com/in/harshal-patel-246306352/",
}

ABOUT = (
    "Driven by curiosity for technology and a passion for transforming data into meaningful insights, "
    "I bring analytical thinking, technical proficiency, and clear communication. My background across "
    "multiple institutions strengthened my adaptability and broadened my problem-solving approach. "
    "With a solid foundation in data management, model building and deployment, predictive analysis, "
    "and storytelling through data, along with sales and mentorship experience, I aim to deliver impactful, "
    "data-driven solutions with elegance."
)

EXPERIENCE = [
    {
        "title": "IT & Marketing Support | Vinayak Infotech",
        "meta": "Ahmedabad, India | May 2024 – 2025",
        "bullets": [
            "Assisted in installation and setup of computer systems and hardware.",
            "Mentored the software team in Java, Python (advanced and libraries), and testing tasks.",
            "Streamlined marketing team processes and provided technical assistance to improve efficiency."
        ],
        "tags": ["Python", "Java", "Mentorship", "IT Support", "Process Improvement"]
    },
    {
        "title": "Software Engineer | Cignex Datamatics",
        "meta": "Gujarat, India | Aug 2022 – Jul 2023",
        "bullets": [
            "Developed testing scripts using Jira and collaborated closely with QA teams.",
            "Resolved bugs and improved system performance by addressing multinational client needs.",
            "Worked on Java-based projects and testing environments to enhance client system efficiency."
        ],
        "tags": ["Java", "Jira", "QA", "Client Collaboration"]
    },
    {
        "title": "Software Engineering Intern | Axis Ray Technology",
        "meta": "Gujarat, India | Jun 2022 – Dec 2022",
        "bullets": [
            "Built proficiency in Java, Advanced Java, and SQL-based data integration.",
            "Worked on real-world projects with cross-national business professionals.",
            "Collaborated with and mentored peers, contributing to successful internship delivery."
        ],
        "tags": ["Advanced Java", "SQL", "Collaboration", "Mentorship"]
    },
    {
        "title": "Sales Executive | AURA ETHNICS",
        "meta": "Jan 2022 – Jun 2022",
        "bullets": [
            "Managed and grew online sales channels through Google Analytics analysis and customer-journey monitoring.",
            "Improved traffic, conversions, and revenue by adjusting listings and promotions.",
            "Used brand storytelling and high-quality in-store service to increase walk-in conversions and repeat customers."
        ],
        "tags": ["Analytics", "Sales", "Customer Engagement", "Storytelling"]
    },
]

PROJECTS = [
    {
        "name": "Rome Airbnb Analysis and Price Prediction",
        "role_line": "EDA + interactive maps + SVM classification",
        "objective": "Analyze Airbnb listings in Rome, understand key price drivers, and classify listings into price categories.",
        "methods": [
            "Exploratory Data Analysis (histograms, boxplots, bar charts, scatter plots) for pricing, room types, neighborhoods, reviews.",
            "Interactive map visualization of listing distribution and price hotspots.",
            "Machine Learning: SVM classifier using room type, neighborhood, capacity, and other features."
        ],
        "key_findings": [
            "Room type and neighborhood are the strongest drivers of price.",
            "Central areas like Centro Storico and Trastevere show higher prices.",
            "Review count has weak correlation with price.",
            "Dashboard highlights market hotspots and trends with clear explanations."
        ],
        "stack": ["Python (Advanced & Libraries)", "EDA", "SVM", "Streamlit", "Data Storytelling"],
        "github": "https://github.com/Harshal3233/rome-airbnb-streamlit",
        "live": "https://rome-airbnb-app-bsr6lkugduccvbrwmjfksk.streamlit.app/"
    },
    {
        "name": "Explainable ML for Cross-Country Agricultural Production (FAOSTAT + SHAP)",
        "role_line": "Random Forest regression + SHAP explainability (policy-style interpretation)",
        "objective": "Use explainable machine learning to compare how crop choice vs country context drive production differences across Italy, France, Germany, and Spain.",
        "methods": [
            "Random Forest regression (Country + Item features) as an interpretive model (not forecasting).",
            "SHAP explainability to quantify feature contributions and compare drivers across countries.",
            "Transparent reporting using MAE, Relative MAE, and R² for scale-aware evaluation."
        ],
        "key_findings": [
            "Italy and Spain appear predominantly crop-driven systems.",
            "France combines crop-driven effects with scale-driven country influence.",
            "Germany shows a more balanced crop and country effect structure.",
            "Approach emphasizes interpretability, transparency, and comparability for stakeholders."
        ],
        "stack": ["Python (Advanced & Libraries)", "Random Forest", "SHAP", "Streamlit", "Explainable AI"],
        "github": "https://github.com/Harshal3233/fao-shap-dashboard",
        "live": "https://fao-shap-dashboard-fyfzpqshuzcpfvz79m6xio.streamlit.app/"
    },
]

SKILLS = {
    "Programming & Data": [
        "Python (Advanced & Libraries)", "Advanced Java", "SQL",
        "EDA", "K-Means", "Regression", "Random Forest", "SVM", "Neural Networks",
        "Data Management", "Model Building & Deployment", "Predictive Analysis"
    ],
    "Tools & Platforms": [
        "Streamlit", "VS Code", "Jupyter Notebook", "GitHub", "Jira",
        "MS Excel", "Google Workspace"
    ],
    "Web & Design": [
        "HTML", "CSS", "JavaScript", "Figma", "Interactive Dashboards"
    ],
}

EDUCATION = [
    {
        "title": "International Master in Data Science (Ongoing)",
        "meta": "Rome Business School | Rome, Italy",
        "bullets": [
            "Strengthening theoretical and practical data science foundations through hands-on projects and Oracle labs.",
            "Participated in industry excursions with organizations such as IBM and Owkin."
        ],
    },
    {
        "title": "B.Tech in Computer Engineering (First Class Distinction)",
        "meta": "Swarrnim Institute of Technology & Startup | Gujarat, India | 2020 – 2024",
        "bullets": [
            "Debate Champion (2020–2021).",
            "University Student Council Member (2020–2024): supported departmental events and initiatives.",
            "Participated in multiple hackathons; contributed to organizing a Blood Donation Camp (2023)."
        ],
    }
]

LANGUAGES = "English (Native/Bilingual), Hindi (Native), Italian (Basic – improving)"

# -------------------------------------------------
# Helpers
# -------------------------------------------------
def pills(items):
    return "".join([f"<span class='pill'>{x}</span>" for x in items])

def card(title, meta=None, bullets=None, tags=None):
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader(title)
    if meta:
        st.caption(meta)
    if bullets:
        st.write("\n".join([f"- {b}" for b in bullets]))
    if tags:
        st.markdown(pills(tags), unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

def cv_download_button():
    """
    Put your CV file in your GitHub repo here:
      assets/Harshal_Patel_CV.pdf
    Then the button will appear automatically on Streamlit Cloud.
    """
    cv_path = Path("assets/Harshal_Patel_CV.pdf")
    if cv_path.exists():
        st.download_button(
            label="⬇️ Download CV",
            data=cv_path.read_bytes(),
            file_name=cv_path.name,
            mime="application/pdf",
            use_container_width=True
        )
    else:
        st.info("To enable download: add `assets/Harshal_Patel_CV.pdf` in your repo (Upload files in GitHub).")

# -------------------------------------------------
# Sidebar Navigation
# -------------------------------------------------
st.sidebar.markdown("### Navigation")
section = st.sidebar.radio(
    "Go to",
    ["Overview", "Experience", "Projects", "Skills", "Education", "Languages", "Contact"],
    index=0
)

st.sidebar.markdown("---")
st.sidebar.markdown("### Quick Links")
st.sidebar.link_button("LinkedIn", PROFILE["linkedin_url"])
st.sidebar.link_button("Rome Airbnb Live App", PROJECTS[0]["live"])
st.sidebar.link_button("FAO SHAP Live App", PROJECTS[1]["live"])
st.sidebar.link_button("Rome Airbnb GitHub", PROJECTS[0]["github"])
st.sidebar.link_button("FAO SHAP GitHub", PROJECTS[1]["github"])

# -------------------------------------------------
# Top Header (Always visible)
# -------------------------------------------------
col1, col2 = st.columns([0.72, 0.28], vertical_alignment="top")
with col1:
    st.markdown(f"<div class='name'>{PROFILE['name']}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='tagline'>{PROFILE['tagline']}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='muted'>{PROFILE['location']}</div>", unsafe_allow_html=True)
    st.write(f" {PROFILE['email']}   |    {PROFILE['phone']}   |    {PROFILE['linkedin_url']}")

with col2:
    cv_download_button()

st.markdown("<hr/>", unsafe_allow_html=True)

# -------------------------------------------------
# Sections
# -------------------------------------------------
if section == "Overview":
    st.markdown("<div class='section'>About Me</div>", unsafe_allow_html=True)
    st.write(ABOUT)

    st.markdown("<div class='section'>Featured Projects</div>", unsafe_allow_html=True)
    for p in PROJECTS:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.subheader(p["name"])
        st.caption(p["role_line"])
        st.write(p["objective"])
        st.markdown(pills(p["stack"]), unsafe_allow_html=True)

        c1, c2 = st.columns(2)
        with c1:
            st.link_button("GitHub Repo", p["github"], use_container_width=True)
        with c2:
            st.link_button("Live Streamlit App", p["live"], use_container_width=True)

        st.markdown("</div>", unsafe_allow_html=True)

elif section == "Experience":
    st.markdown("<div class='section'>Professional Experience</div>", unsafe_allow_html=True)
    for e in EXPERIENCE:
        card(e["title"], e["meta"], e["bullets"], e["tags"])

elif section == "Projects":
    st.markdown("<div class='section'>Projects</div>", unsafe_allow_html=True)

    for p in PROJECTS:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.subheader(p["name"])
        st.caption(p["role_line"])

        st.markdown("**Objective**")
        st.write(p["objective"])

        st.markdown("**Methods Used**")
        st.write("\n".join([f"- {m}" for m in p["methods"]]))

        st.markdown("**Key Findings**")
        st.write("\n".join([f"- {k}" for k in p["key_findings"]]))

        st.markdown(pills(p["stack"]), unsafe_allow_html=True)

        c1, c2 = st.columns(2)
        with c1:
            st.link_button("GitHub Repo", p["github"], use_container_width=True)
        with c2:
            st.link_button("Live Streamlit App", p["live"], use_container_width=True)

        st.markdown("</div>", unsafe_allow_html=True)

elif section == "Skills":
    st.markdown("<div class='section'>Skills</div>", unsafe_allow_html=True)
    for cat, items in SKILLS.items():
        st.markdown(f"**{cat}**")
        st.markdown(pills(items), unsafe_allow_html=True)

elif section == "Education":
    st.markdown("<div class='section'>Education</div>", unsafe_allow_html=True)
    for ed in EDUCATION:
        card(ed["title"], ed["meta"], ed["bullets"], None)

elif section == "Languages":
    st.markdown("<div class='section'>Languages</div>", unsafe_allow_html=True)
    st.write(LANGUAGES)

elif section == "Contact":
    st.markdown("<div class='section'>Contact</div>", unsafe_allow_html=True)
    st.write("If you'd like to connect, feel free to reach out:")
    st.write(f"- Email: {PROFILE['email']}")
    st.write(f"- Phone: {PROFILE['phone']}")
    st.write(f"- LinkedIn: {PROFILE['linkedin_url']}")
