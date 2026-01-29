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
    "text": "#111827",        # slate-900
    "muted": "#6b7280",       # gray-500
    "border": "rgba(17, 24, 39, 0.12)",
    "soft": "rgba(17, 24, 39, 0.04)",
    "accent": "#2563eb",      # blue-600
    "accent2": "#7c3aed",     # violet-600
    "chip": "rgba(37, 99, 235, 0.10)",
    "note": "rgba(37, 99, 235, 0.08)",
    "codebg": "rgba(17, 24, 39, 0.035)",
}

# -------------------------------------------------
# CSS (professional, no "cut" bars)
# -------------------------------------------------
st.markdown(
    f"""
<style>
.block-container {{
    padding-top: 1.3rem;
    padding-bottom: 2.4rem;
    max-width: 1200px;
}}
section[data-testid="stSidebar"] > div {{
    padding-top: 1.05rem;
}}
h1, h2, h3 {{ letter-spacing: 0.2px; }}
.small-muted {{
    color: {BRAND["muted"]};
    font-size: 0.95rem;
}}
.kicker {{
    color: rgba(17, 24, 39, 0.72);
    font-weight: 700;
    font-size: 1.02rem;
    margin-top: -0.25rem;
}}
.hero {{
    border: 1px solid {BRAND["border"]};
    border-radius: 18px;
    padding: 1.15rem 1.2rem;
    background:
        radial-gradient(1200px 220px at 18% -20%, {BRAND["chip"]}, transparent 60%),
        radial-gradient(1200px 220px at 92% 0%, rgba(124, 58, 237, 0.10), transparent 55%),
        #ffffff;
}}
.hero-title {{
    font-size: 2.25rem;
    font-weight: 900;
    color: {BRAND["text"]};
    margin-bottom: 0.12rem;
}}
.hero-tag {{
    font-size: 1.06rem;
    font-weight: 750;
    color: rgba(17, 24, 39, 0.78);
}}
.hero-meta {{
    color: {BRAND["muted"]};
    margin-top: 0.25rem;
}}
.section-title {{
    font-size: 1.35rem;
    font-weight: 900;
    margin: 1.6rem 0 0.55rem 0;
    color: {BRAND["text"]};
}}
.section-line {{
    height: 2px;
    width: 92px;
    border-radius: 999px;
    background: linear-gradient(90deg, {BRAND["accent"]}, {BRAND["accent2"]});
    margin-bottom: 0.95rem;
}}
.section-sub {{
    color: {BRAND["muted"]};
    margin-top: -0.35rem;
    margin-bottom: 0.8rem;
}}
.card {{
    border: 1px solid {BRAND["border"]};
    border-radius: 18px;
    padding: 1.05rem 1.1rem;
    background: #ffffff;
    margin-bottom: 0.95rem;
}}
.card:hover {{ border-color: rgba(17, 24, 39, 0.20); }}
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
.pill-accent {{
    background: {BRAND["note"]};
    border-color: rgba(37, 99, 235, 0.20);
}}
.side-card {{
    border: 1px solid {BRAND["border"]};
    border-radius: 18px;
    padding: 0.95rem 0.95rem;
    background: #ffffff;
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
    background: #ffffff;
    color: {BRAND["text"]};
    font-weight: 750;
    text-decoration: none !important;
    margin: 0.35rem 0;
}}
.navbtn:hover {{
    border-color: rgba(17, 24, 39, 0.22);
    background: {BRAND["soft"]};
}}
.anchor {{
    height: 1px;
    margin-top: -70px;
    padding-top: 70px;
}}
/* Blog polish */
.note-meta {{
    display: flex;
    gap: 0.6rem;
    align-items: center;
    flex-wrap: wrap;
    margin: 0.2rem 0 0.6rem 0;
}}
.meta-dot {{
    width: 5px; height: 5px;
    background: rgba(17,24,39,0.35);
    border-radius: 999px;
}}
.callout {{
    border: 1px solid rgba(37, 99, 235, 0.20);
    background: {BRAND["note"]};
    border-radius: 14px;
    padding: 0.75rem 0.85rem;
    margin-top: 0.6rem;
}}
.codebox {{
    border: 1px solid rgba(17, 24, 39, 0.12);
    background: {BRAND["codebg"]};
    border-radius: 14px;
    padding: 0.75rem 0.85rem;
    margin-top: 0.65rem;
}}
.codebox pre {{
    margin: 0;
    font-size: 0.85rem;
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
            "Analyzed publicly available Rome Airbnb listings to understand pricing patterns. "
            "Built an interactive dashboard to visualize hotspots and trained an SVM classifier to predict price categories."
        ),
        "impact": [
            "Identified room type + neighborhood as the strongest drivers of price.",
            "Highlighted premium zones (Centro Storico, Trastevere) using map-based insights.",
            "Delivered a stakeholder-friendly dashboard with clear visuals and variable explanations.",
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
            "Built an explainable ML dashboard to compare agricultural production patterns across Italy, France, Germany, and Spain. "
            "Used Random Forest as an interpretive model and SHAP to quantify feature influence transparently."
        ),
        "impact": [
            "Compared crop-driven vs country-driven production patterns across multiple nations.",
            "Used SHAP to turn model decisions into stakeholder-friendly explanations.",
            "Reported MAE, Relative MAE, and R² to keep evaluation transparent and interpretable.",
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

LEARNING_NOW = [
    "Embedding OpenAI into data science workflows (retrieval, prompting patterns, evaluation).",
    "Italian language: targeting **A2** proficiency.",
    "Model building + deployment patterns (reproducibility, packaging, app deployment).",
    "Exploring LLM models and practical use cases (analysis, summarization, data assistants).",
]

# Polished blog posts (with date, read time, tags, and small callouts)
BLOG_NOTES = [
    {
        "title": "How SHAP helped explain model drivers",
        "subtitle": "Turning model behavior into stakeholder-friendly insights",
        "date": "Jan 2026",
        "read_time": "3 min read",
        "tags": ["XAI", "SHAP", "Random Forest", "Interpretability"],
        "body": [
            "SHAP helped me move beyond accuracy metrics by explaining *why* a model behaves the way it does.",
            "It made feature influence visible and comparable, especially when contrasting crop choice vs country context.",
            "This helped translate model outputs into explanations that stakeholders can trust and act on.",
        ],
        "callout_title": "Key takeaway",
        "callout": "Interpretability isn’t an extra. It’s what makes models usable in real decisions.",
        "code_title": "A simple SHAP workflow (conceptual)",
        "code": """# Conceptual outline
model = RandomForestRegressor(...)
model.fit(X_train, y_train)

explainer = shap.Explainer(model, X_train)
shap_values = explainer(X_test)

# Visualize global feature influence
shap.plots.bar(shap_values)""",
    },
    {
        "title": "Why I used EDA + SVM for Airbnb price categories",
        "subtitle": "A practical modeling choice driven by the data",
        "date": "Jan 2026",
        "read_time": "3 min read",
        "tags": ["EDA", "SVM", "Classification", "Dashboards"],
        "body": [
            "EDA came first to understand price distribution shape, outliers, and neighborhood effects.",
            "I reframed the task into price categories, making it more robust and easier to communicate.",
            "SVM served as a strong baseline for classification, and the dashboard presented findings clearly.",
        ],
        "callout_title": "Key takeaway",
        "callout": "Good modeling is often reframing the problem so the output is stable and explainable.",
        "code_title": "Baseline SVM pipeline (conceptual)",
        "code": """# Conceptual outline
X = features  # e.g., room_type, neighborhood, capacity
y = price_category  # binned labels

pipe = Pipeline([
  ("prep", preprocessor),
  ("clf", SVC(kernel="rbf"))
])

pipe.fit(X_train, y_train)
pred = pipe.predict(X_test)""",
    },
]

# -------------------------------------------------
# Helpers
# -------------------------------------------------
def pills(items, accent=False):
    cls = "pill pill-accent" if accent else "pill"
    return "".join([f"<span class='{cls}'>{x}</span>" for x in items])

def anchor(anchor_id: str):
    st.markdown(f"<div id='{anchor_id}' class='anchor'></div>", unsafe_allow_html=True)

def section(title: str, subtitle: str | None = None):
    st.markdown(f"<div class='section-title'>{title}</div>", unsafe_allow_html=True)
    st.markdown("<div class='section-line'></div>", unsafe_allow_html=True)
    if subtitle:
        st.markdown(f"<div class='section-sub'>{subtitle}</div>", unsafe_allow_html=True)

def card_open():
    st.markdown("<div class='card'>", unsafe_allow_html=True)

def card_close():
    st.markdown("</div>", unsafe_allow_html=True)

# -------------------------------------------------
# Sidebar
# -------------------------------------------------
with st.sidebar:
    st.markdown("<div class='side-card'>", unsafe_allow_html=True)
    st.markdown("<div class='side-title'>Profile</div>", unsafe_allow_html=True)
    st.markdown(f"**{PROFILE['name']}**", unsafe_allow_html=True)
    st.markdown(f"<div class='small-muted'>{PROFILE['tagline']}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='small-muted' style='margin-top:0.35rem;'>{PROFILE['location']}</div>", unsafe_allow_html=True)
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
<a class="navbtn" href="#learning">What I’m Learning Now</a>
<a class="navbtn" href="#experience">Experience</a>
<a class="navbtn" href="#projects">Projects</a>
<a class="navbtn" href="#notes">Blog / Notes</a>
<a class="navbtn" href="#skills">Skills</a>
<a class="navbtn" href="#education">Education</a>
<a class="navbtn" href="#languages">Languages</a>
<a class="navbtn" href="#contact">Contact</a>
""",
        unsafe_allow_html=True,
    )
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='side-card'>", unsafe_allow_html=True)
    st.markdown("<div class='side-title'>Filters</div>", unsafe_allow_html=True)

    all_project_tags = sorted({t for p in PROJECTS for t in p["tags"]})
    selected_project_tags = st.multiselect("Project tags", all_project_tags, default=[])

    all_note_tags = sorted({t for n in BLOG_NOTES for t in n["tags"]})
    selected_note_tags = st.multiselect("Note tags", all_note_tags, default=[])

    show_previews = st.toggle("Embed live previews", value=False)
    st.markdown("</div>", unsafe_allow_html=True)

# -------------------------------------------------
# Main Hero (NO top-left LinkedIn/Contact buttons here)
# -------------------------------------------------
st.markdown("<div class='hero'>", unsafe_allow_html=True)
left, right = st.columns([0.70, 0.30], vertical_alignment="top")

with left:
    st.markdown(f"<div class='hero-title'>{PROFILE['name']}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='hero-tag'>{PROFILE['tagline']}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='hero-meta'>{PROFILE['location']}</div>", unsafe_allow_html=True)
    st.markdown("<div style='height:0.6rem;'></div>", unsafe_allow_html=True)
    st.write(ABOUT)

with right:
    st.metric("Deployed Projects", "2")
    st.metric("Core Focus", "AI + Analytics")
    st.metric("Availability", "Relocation")

st.markdown("</div>", unsafe_allow_html=True)

# -------------------------------------------------
# About
# -------------------------------------------------
anchor("about")
section("About", "How I work: explore, model, explain, ship.")
card_open()
st.write(
    "My workflow is built for clarity and delivery:"
    "\n- **EDA first** to understand patterns, outliers, and edge cases"
    "\n- **Modeling** with baselines and explainability when needed"
    "\n- **Storytelling** through dashboards and clear narratives"
    "\n- **Deployment** using reproducible repos and Streamlit apps"
)
st.markdown(pills(["EDA", "Predictive Analysis", "Model Building", "Deployment", "Data Storytelling"], accent=True), unsafe_allow_html=True)
card_close()

# -------------------------------------------------
# What I'm Learning Now
# -------------------------------------------------
anchor("learning")
section("What I’m Learning Now", "Current focus areas and upskilling.")
card_open()
st.write("\n".join([f"- {x}" for x in LEARNING_NOW]))
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
# Projects
# -------------------------------------------------
anchor("projects")
section("Projects", "Deployed apps + clean repos. Built to be clicked.")

def project_match(p):
    if not selected_project_tags:
        return True
    return any(t in p["tags"] for t in selected_project_tags)

for p in [x for x in PROJECTS if project_match(x)]:
    card_open()

    top = st.columns([0.72, 0.28], vertical_alignment="top")
    with top[0]:
        st.markdown(f"<div class='card-title'>{p['title']}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='card-sub'>{p['one_liner']}</div>", unsafe_allow_html=True)
        st.markdown(pills(p["stack"]), unsafe_allow_html=True)

    with top[1]:
        st.link_button("Live App", p["live"], use_container_width=True)
        st.link_button("GitHub Repo", p["github"], use_container_width=True)

    st.markdown("**Summary**")
    st.write(p["summary"])

    st.markdown("**Highlights**")
    st.write("\n".join([f"- {x}" for x in p["impact"]]))

    if show_previews:
        with st.expander("Preview live app inside this CV"):
            components.iframe(p["live"], height=560, scrolling=True)

    card_close()

# -------------------------------------------------
# Blog / Notes (Polished)
# -------------------------------------------------
anchor("notes")
section("Blog / Notes", "Short technical notes on decisions and learnings.")

# Notes index (interactive)
index_cols = st.columns([0.55, 0.45], vertical_alignment="center")
with index_cols[0]:
    st.markdown("<div class='small-muted'>Browse notes by tag and open the one you want.</div>", unsafe_allow_html=True)
with index_cols[1]:
    note_titles = [n["title"] for n in BLOG_NOTES]
    jump_note = st.selectbox("Jump to a note", ["(Select)"] + note_titles)

def note_match(n):
    if not selected_note_tags:
        return True
    return any(t in n["tags"] for t in selected_note_tags)

for note in [n for n in BLOG_NOTES if note_match(n)]:
    card_open()

    st.markdown(f"<div class='card-title'>{note['title']}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='card-sub'>{note['subtitle']}</div>", unsafe_allow_html=True)

    # Meta row: date • read time • tags
    st.markdown(
        f"""
<div class="note-meta">
  <span class="small-muted">{note["date"]}</span>
  <span class="meta-dot"></span>
  <span class="small-muted">{note["read_time"]}</span>
</div>
""",
        unsafe_allow_html=True,
    )
    st.markdown(pills(note["tags"], accent=True), unsafe_allow_html=True)

    # Compact preview
    st.write(note["body"][0])

    with st.expander("Read full note"):
        st.write("\n".join([f"- {x}" for x in note["body"]]))

        st.markdown(
            f"""
<div class="callout">
  <strong>{note["callout_title"]}:</strong> {note["callout"]}
</div>
""",
            unsafe_allow_html=True,
        )

        st.markdown("**" + note["code_title"] + "**")
        st.markdown(
            f"""
<div class="codebox"><pre>{note["code"]}</pre></div>
""",
            unsafe_allow_html=True,
        )

    card_close()

# -------------------------------------------------
# Skills
# -------------------------------------------------
anchor("skills")
section("Skills", "Core stack and strengths.")
cols = st.columns(3)
for i, (k, items) in enumerate(SKILLS.items()):
    with cols[i]:
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
section("Contact")
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

st.markdown(
    "<div class='small-muted' style='margin-top:1.2rem;'>Built with Streamlit • Deployed on Streamlit Cloud</div>",
    unsafe_allow_html=True
)
