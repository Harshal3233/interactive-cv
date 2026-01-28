
   import streamlit as st

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
    padding: 1.15rem;
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
</style>
""", unsafe_allow_html=True)

# -------------------------------------------------
# Profile Data
# -------------------------------------------------
PROFILE = {
    "name": "Harshal M Patel",
    "tagline": "AI Engineer | Data Science | Software Engineering | Analytics",
    "location": "Rome, Italy (available to relocate)",
    "email": "harshalmpatel2001@gmail.com",
    "phone": "+91 9974890592",
    "linkedin": "https://www.linkedin.com/in/harshal-patel-246306352/"
}

ABOUT = (
    "Driven by curiosity for technology and a passion for transforming data into meaningful insights, "
    "I bring analytical thinking, technical proficiency, and clear communication. My background across "
    "multiple institutions strengthened my adaptability and broadened my problem-solving approach. "
    "With a solid foundation in data management, model building and deployment, predictive analysis, "
    "and storytelling through data, along with sales and mentorship experience, I aim to deliver impactful, "
    "data-driven solutions with elegance."
)

# -------------------------------------------------
# Experience
# -------------------------------------------------
EXPERIENCE = [
    (
        "IT & Marketing Support | Vinayak Infotech",
        "Ahmedabad, India | May 2024 – 2025",
        [
            "Installed and configured computer systems and hardware.",
            "Mentored software team in Java and Python (advanced and libraries).",
            "Streamlined marketing workflows through technical support."
        ],
        ["Python", "Java", "Mentorship", "IT Support"]
    ),
    (
        "Software Engineer | Cignex Datamatics",
        "Gujarat, India | Aug 2022 – Jul 2023",
        [
            "Developed testing scripts using Jira and collaborated with QA teams.",
            "Resolved bugs and improved performance for multinational clients.",
            "Worked on Java-based systems in testing environments."
        ],
        ["Java", "Jira", "QA"]
    ),
    (
        "Software Engineering Intern | Axis Ray Technology",
        "Gujarat, India | Jun 2022 – Dec 2022",
        [
            "Built proficiency in Java, Advanced Java, and SQL.",
            "Worked on real-world projects with cross-national teams.",
            "Mentored peers and contributed to successful delivery."
        ],
        ["Advanced Java", "SQL"]
    ),
    (
        "Sales Executive | Aura Ethnics",
        "Jan 2022 – Jun 2022",
        [
            "Analyzed Google Analytics data to optimize online sales.",
            "Improved conversions through pricing and promotion insights.",
            "Delivered personalized in-store customer experiences."
        ],
        ["Analytics", "Sales", "Customer Engagement"]
    )
]

# -------------------------------------------------
# Projects
# -------------------------------------------------
PROJECTS = [
    {
        "title": "Rome Airbnb Analysis and Price Prediction",
        "subtitle": "EDA, interactive maps, and SVM classification",
        "objective": "Analyze Airbnb listings in Rome and identify key drivers of pricing.",
        "highlights": [
            "Strong impact of room type and neighborhood on pricing.",
            "Central areas show significantly higher prices.",
            "Review count has weak correlation with price.",
            "Interactive dashboard visualizes market hotspots clearly."
        ],
        "stack": ["Python (Advanced)", "EDA", "SVM", "Streamlit"],
        "github": "https://github.com/Harshal3233/rome-airbnb-streamlit",
        "live": "https://rome-airbnb-app-bsr6lkugduccvbrwmjfksk.streamlit.app/"
    },
    {
        "title": "Explainable ML for Agricultural Production (FAOSTAT + SHAP)",
        "subtitle": "Random Forest regression with SHAP explainability",
        "objective": "Compare crop-driven vs country-driven agricultural production patterns.",
        "highlights": [
            "Italy and Spain are primarily crop-driven systems.",
            "France shows mixed crop and scale effects.",
            "Germany demonstrates balanced influence.",
            "SHAP ensures transparency and interpretability."
        ],
        "stack": ["Python (Advanced)", "Random Forest", "SHAP", "Explainable AI"],
        "github": "https://github.com/Harshal3233/fao-shap-dashboard",
        "live": "https://fao-shap-dashboard-fyfzpqshuzcpfvz79m6xio.streamlit.app/"
    }
]

# -------------------------------------------------
# Sidebar
# -------------------------------------------------
st.sidebar.markdown("### Navigation")
section = st.sidebar.radio(
    "Go to",
    ["Overview", "Experience", "Projects", "Skills", "Education", "Contact"]
)

st.sidebar.markdown("---")
st.sidebar.link_button("LinkedIn", PROFILE["linkedin"])
st.sidebar.link_button("Rome Airbnb App", PROJECTS[0]["live"])
st.sidebar.link_button("FAO SHAP App", PROJECTS[1]["live"])

# -------------------------------------------------
# Header
# -------------------------------------------------
st.markdown(f"<div class='name'>{PROFILE['name']}</div>", unsafe_allow_html=True)
st.markdown(f"<div class='tagline'>{PROFILE['tagline']}</div>", unsafe_allow_html=True)
st.markdown(f"<div class='muted'>{PROFILE['location']}</div>", unsafe_allow_html=True)
st.write(f" {PROFILE['email']} |  {PROFILE['phone']} |  {PROFILE['linkedin']}")

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
        st.subheader(p["title"])
        st.caption(p["subtitle"])
        st.write(p["objective"])
        st.markdown("".join([f"<span class='pill'>{t}</span>" for t in p["stack"]]), unsafe_allow_html=True)

        c1, c2 = st.columns(2)
        with c1:
            st.link_button("GitHub Repo", p["github"], use_container_width=True)
        with c2:
            st.link_button("Live Streamlit App", p["live"], use_container_width=True)

        st.markdown("</div>", unsafe_allow_html=True)

elif section == "Experience":
    st.markdown("<div class='section'>Professional Experience</div>", unsafe_allow_html=True)
    for title, meta, bullets, tags in EXPERIENCE:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.subheader(title)
        st.caption(meta)
        st.write("\n".join([f"- {b}" for b in bullets]))
        st.markdown("".join([f"<span class='pill'>{t}</span>" for t in tags]), unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

elif section == "Projects":
    st.markdown("<div class='section'>Projects</div>", unsafe_allow_html=True)
    for p in PROJECTS:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.subheader(p["title"])
        st.caption(p["subtitle"])
        st.write(p["objective"])
        st.write("\n".join([f"- {h}" for h in p["highlights"]]))
        st.markdown("".join([f"<span class='pill'>{t}</span>" for t in p["stack"]]), unsafe_allow_html=True)
        st.link_button("GitHub Repo", p["github"])
        st.link_button("Live Streamlit App", p["live"])
        st.markdown("</div>", unsafe_allow_html=True)

elif section == "Skills":
    st.markdown("<div class='section'>Skills</div>", unsafe_allow_html=True)
    st.markdown("**Programming & Data**")
    st.write("Python (Advanced & Libraries), Advanced Java, SQL, EDA, K-Means, Regression, Random Forest, SVM, Neural Networks")
    st.markdown("**Tools & Platforms**")
    st.write("Streamlit, VS Code, Jupyter Notebook, GitHub, Jira, MS Excel, Google Workspace")
    st.markdown("**Web & Design**")
    st.write("HTML, CSS, JavaScript, Figma, Interactive Dashboards")

elif section == "Education":
    st.markdown("<div class='section'>Education</div>", unsafe_allow_html=True)
    st.markdown("**International Master in Data Science** — Rome Business School (Ongoing)")
    st.write("Industry excursions with IBM and Owkin; applied projects and Oracle labs.")
    st.markdown("**B.Tech in Computer Engineering** — Swarrnim Institute (2020–2024)")
    st.write("First Class Distinction | Debate Champion | Student Council Member")

elif section == "Contact":
    st.markdown("<div class='section'>Contact</div>", unsafe_allow_html=True)
    st.write(f"- Email: {PROFILE['email']}")
    st.write(f"- Phone: {PROFILE['phone']}")
    st.write(f"- LinkedIn: {PROFILE['linkedin']}")
