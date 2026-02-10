import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# -------------------------------------------------
# Page Config
# -------------------------------------------------
st.set_page_config(
    page_title="Harshal M Patel | AI Engineer",
    layout="wide",
)

# -------------------------------------------------
# Brand / UI tokens
# -------------------------------------------------
BRAND = {
    "text": "#0f172a",        # slate-900
    "muted": "#64748b",       # slate-500
    "border": "rgba(15, 23, 42, 0.12)",
    "soft": "rgba(15, 23, 42, 0.04)",
    "accent": "#2563eb",      # blue-600
    "accent2": "#7c3aed",     # violet-600
    "chip": "rgba(37, 99, 235, 0.10)",
    "note": "rgba(124, 58, 237, 0.08)",
    "codebg": "rgba(15, 23, 42, 0.035)",
}

# -------------------------------------------------
# CSS (Professional dashboard UI + overflow fixes)
# -------------------------------------------------
st.markdown(
    f"""
<style>
/* Prevent horizontal scrollbars (the "2 sliders" issue) */
html, body {{ overflow-x: hidden; }}
* {{ box-sizing: border-box; }}
a, p, div, span {{ overflow-wrap: anywhere; word-break: break-word; }}

.block-container {{
    padding-top: 1.0rem;
    padding-bottom: 2.2rem;
    max-width: 1280px;
}}
header[data-testid="stHeader"] {{
    background: transparent;
}}
.small-muted {{ color: {BRAND["muted"]}; font-size: 0.95rem; }}

/* Hero */
.hero {{
    border: 1px solid {BRAND["border"]};
    border-radius: 20px;
    padding: 1.25rem 1.25rem;
    background:
        radial-gradient(1100px 260px at 12% -20%, {BRAND["chip"]}, transparent 58%),
        radial-gradient(1100px 240px at 95% 0%, rgba(124, 58, 237, 0.10), transparent 55%),
        #ffffff;
    box-shadow: 0 12px 30px rgba(15, 23, 42, 0.05);
}}
.hero-title {{
    font-size: 2.35rem;
    font-weight: 950;
    color: {BRAND["text"]};
    margin-bottom: 0.10rem;
}}
.hero-tag {{
    font-size: 1.05rem;
    font-weight: 850;
    color: rgba(15, 23, 42, 0.78);
}}
.hero-meta {{
    color: {BRAND["muted"]};
    margin-top: 0.25rem;
}}
.hero-cta {{
    margin-top: 0.75rem;
    display: inline-flex;
    gap: 0.5rem;
    flex-wrap: wrap;
}}

/* Section */
.section-title {{
    font-size: 1.35rem;
    font-weight: 950;
    margin: 1.55rem 0 0.45rem 0;
    color: {BRAND["text"]};
}}
.section-line {{
    height: 3px;
    width: 104px;
    border-radius: 999px;
    background: linear-gradient(90deg, {BRAND["accent"]}, {BRAND["accent2"]});
    margin-bottom: 0.90rem;
}}
.section-sub {{
    color: {BRAND["muted"]};
    margin-top: -0.30rem;
    margin-bottom: 0.85rem;
}}

/* Cards */
.card {{
    border: 1px solid {BRAND["border"]};
    border-radius: 18px;
    padding: 1.05rem 1.15rem;
    background: #ffffff;
    margin-bottom: 0.95rem;
    box-shadow: 0 10px 24px rgba(15, 23, 42, 0.04);
}}
.card:hover {{
    border-color: rgba(15, 23, 42, 0.18);
    box-shadow: 0 14px 32px rgba(15, 23, 42, 0.06);
}}
.card-title {{
    font-size: 1.10rem;
    font-weight: 950;
    margin-bottom: 0.10rem;
    color: {BRAND["text"]};
}}
.card-sub {{
    color: {BRAND["muted"]};
    font-size: 0.96rem;
    margin-bottom: 0.55rem;
}}

/* Pills */
.pill {{
    display: inline-block;
    padding: 0.24rem 0.62rem;
    margin: 0.16rem 0.28rem 0.10rem 0;
    border-radius: 999px;
    border: 1px solid {BRAND["border"]};
    background: {BRAND["soft"]};
    font-size: 0.84rem;
    color: rgba(15, 23, 42, 0.86);
}}
.pill-accent {{
    background: {BRAND["note"]};
    border-color: rgba(124, 58, 237, 0.22);
}}

/* KPI tiles */
.kpi {{
    border: 1px solid {BRAND["border"]};
    border-radius: 16px;
    padding: 0.85rem 0.95rem;
    background: #ffffff;
    box-shadow: 0 10px 22px rgba(15, 23, 42, 0.04);
}}
.kpi-label {{
    color: {BRAND["muted"]};
    font-size: 0.86rem;
    margin-bottom: 0.15rem;
}}
.kpi-value {{
    font-size: 1.15rem;
    font-weight: 950;
    color: {BRAND["text"]};
}}

/* Tab polish */
div[data-testid="stTabs"] button {{
    font-weight: 850 !important;
    border-radius: 12px !important;
    padding: 0.55rem 0.9rem !important;
}}
div[data-testid="stTabs"] button[aria-selected="true"] {{
    background: {BRAND["soft"]} !important;
    border: 1px solid rgba(15, 23, 42, 0.16) !important;
}}

/* Timeline */
.timeline {{
    position: relative;
    padding-left: 1.1rem;
}}
.timeline::before {{
    content: "";
    position: absolute;
    left: 0.36rem;
    top: 0.2rem;
    bottom: 0.2rem;
    width: 2px;
    background: rgba(15, 23, 42, 0.10);
    border-radius: 999px;
}}
.t-item {{
    position: relative;
    padding-left: 1.25rem;
    margin-bottom: 0.95rem;
}}
.t-dot {{
    position: absolute;
    left: 0.18rem;
    top: 0.42rem;
    width: 12px;
    height: 12px;
    border-radius: 999px;
    background: linear-gradient(90deg, {BRAND["accent"]}, {BRAND["accent2"]});
    box-shadow: 0 0 0 5px rgba(37, 99, 235, 0.10);
}}
.t-card {{
    border: 1px solid {BRAND["border"]};
    border-radius: 18px;
    padding: 0.95rem 1.05rem;
    background: #ffffff;
    box-shadow: 0 10px 22px rgba(15, 23, 42, 0.04);
}}
.t-title {{
    font-weight: 950;
    color: {BRAND["text"]};
    font-size: 1.05rem;
}}
.t-meta {{
    color: {BRAND["muted"]};
    margin-top: 0.15rem;
    margin-bottom: 0.55rem;
    font-size: 0.93rem;
}}

.visit {{
    margin-top: 0.55rem;
    padding-top: 0.25rem;
}}
.visit a {{
    color: {BRAND["accent"]};
    font-weight: 900;
    text-decoration: none;
}}
.visit a:hover {{
    text-decoration: underline;
}}

/* Notes code blocks wrap */
.codebox pre {{
  white-space: pre-wrap;
  word-break: break-word;
  margin: 0;
  font-size: 0.85rem;
}}
.callout {{
    border: 1px solid rgba(124, 58, 237, 0.22);
    background: {BRAND["note"]};
    border-radius: 14px;
    padding: 0.75rem 0.85rem;
    margin-top: 0.6rem;
}}
.codebox {{
    border: 1px solid rgba(15, 23, 42, 0.12);
    background: {BRAND["codebg"]};
    border-radius: 14px;
    padding: 0.75rem 0.85rem;
    margin-top: 0.65rem;
}}
.note-meta {{
    display: flex;
    gap: 0.6rem;
    align-items: center;
    flex-wrap: wrap;
    margin: 0.2rem 0 0.6rem 0;
}}
.meta-dot {{
    width: 5px; height: 5px;
    background: rgba(15,23,42,0.35);
    border-radius: 999px;
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
    "AI Engineer focused on turning data into decisions through analysis, modeling, explainability, and deployment. "
    "I build work like a product: define the problem, build reliable pipelines, and ship an interface people can use."
)

# References (ONLY Prof. Valentino as requested)
REFERENCES = [
    {
        "name": "Mr. Valentino Megale, PhD",
        "role": "CEO, Softcare Studios",
        "email": "valentinomegale@hotmail.it",
        "linkedin": "https://www.linkedin.com/in/valentinomegale",
    }
]

EXPERIENCE = [
    {
        "role": "IT & Marketing Support",
        "company": "Vinayak Infotech",
        "meta": "Ahmedabad, India • May 2024 – 2025",
        "problem": "Operational teams needed reliable systems and smoother technical workflows across support and marketing execution.",
        "approach": [
            "Installed and configured computer systems and hardware for stable day-to-day operations.",
            "Mentored team members in Java and Python (advanced and libraries) and supported testing tasks.",
            "Introduced practical fixes that reduced bottlenecks in marketing workflows.",
        ],
        "outcome": "Improved internal efficiency, reduced technical downtime, and enabled faster execution with clearer technical support.",
        "signals": ["Delivery", "Mentorship", "Operations", "Workflow Efficiency"],
        "tags": ["Python", "Java", "IT Support", "Process Improvement"],
    },
    {
        "role": "Software Engineer",
        "company": "Cignex Datamatics",
        "meta": "Gujarat, India • Aug 2022 – Jul 2023",
        "problem": "Enterprise releases required stronger quality gates to minimize defects and improve stability for multinational clients.",
        "approach": [
            "Developed structured testing workflows using Jira and collaborated closely with QA teams.",
            "Supported Java-based systems and improved testing consistency across environments.",
            "Focused on early defect discovery to reduce downstream rework.",
        ],
        "outcome": "Improved release reliability and reduced post-deployment issues through stronger testing discipline and collaboration.",
        "signals": ["Quality", "Reliability", "QA Collaboration", "Client-Facing Systems"],
        "tags": ["Java", "Jira", "QA", "Collaboration"],
    },
    {
        "role": "Software Engineering Intern",
        "company": "Axis Ray Technology",
        "meta": "Gujarat, India • Jun 2022 – Dec 2022",
        "problem": "Projects needed consistent development support and clean data integration across teams and timelines.",
        "approach": [
            "Strengthened skills in Java, Advanced Java, and SQL-based integration patterns.",
            "Worked on real-world tasks with cross-national teams and project stakeholders.",
            "Supported peer productivity through mentoring and collaborative delivery.",
        ],
        "outcome": "Accelerated delivery readiness by improving implementation consistency and team coordination.",
        "signals": ["Engineering Foundations", "SQL Integration", "Team Support"],
        "tags": ["Advanced Java", "SQL", "Collaboration", "Mentorship"],
    },
    {
        "role": "Sales Executive",
        "company": "AURA ETHNICS",
        "meta": "Jan 2022 – Jun 2022",
        "problem": "Sales performance needed clearer visibility into customer behavior and what drives conversion.",
        "approach": [
            "Used Google Analytics insights to understand traffic, conversion patterns, and customer journeys.",
            "Adjusted listings and promotions using data signals rather than guesswork.",
            "Strengthened customer experience through product storytelling and service quality.",
        ],
        "outcome": "Improved conversion outcomes through data-informed decision-making and stronger customer engagement.",
        "signals": ["Analytics", "Storytelling", "Conversion Focus"],
        "tags": ["Analytics", "Customer Engagement", "Sales"],
    },
]

PROJECTS = [
    {
        "title": "Explainable ML for Agricultural Production (FAOSTAT + SHAP)",
        "one_liner": "Random Forest + SHAP to explain cross-country production drivers (crop vs country effects).",
        "summary": (
            "Built an explainable ML dashboard to compare agricultural production patterns across Italy, France, Germany, and Spain. "
            "Used Random Forest as an interpretive model and SHAP to quantify feature influence transparently."
        ),
        "highlights": [
            "Compared crop-driven vs country-driven production patterns across multiple nations.",
            "Used SHAP to translate model behavior into stakeholder-friendly explanations.",
            "Reported MAE, Relative MAE, and R² to keep evaluation transparent and interpretable.",
        ],
        "stack": ["Python (Advanced)", "Random Forest", "SHAP", "Explainable AI", "Streamlit"],
        "link_label": "Visit app",
        "link_url": "https://fao-shap-dashboard-fyfzpqshuzcpfvz79m6xio.streamlit.app/#d166e061",
        "tags": ["XAI", "SHAP", "ML", "Streamlit"],
    },
    {
        "title": "Rome Airbnb Analysis and Price Prediction",
        "one_liner": "EDA + mapping + SVM classifier to categorize listing prices in Rome.",
        "summary": (
            "Analyzed Rome Airbnb listings to understand pricing patterns and hotspots. "
            "Built a dashboard and trained an SVM classifier to predict price categories."
        ),
        "highlights": [
            "Room type + neighborhood emerged as primary price drivers.",
            "Premium zones highlighted using map-based insights.",
            "Dashboard designed for stakeholder-friendly storytelling.",
        ],
        "stack": ["Python (Advanced)", "EDA", "SVM", "Streamlit", "Data Storytelling"],
        "link_label": "Visit app",
        "link_url": "https://rome-airbnb-app-bsr6lkugduccvbrwmjfksk.streamlit.app/",
        "tags": ["EDA", "Maps", "ML", "Streamlit"],
    },
    {
        "title": "Smoking Analysis (AI + LLM + NLP)",
        "one_liner": "Data science + LLM/NLP exploration for smoking prevalence insights and decision support.",
        "summary": (
            "Project exploring smoking prevalence analysis with a data-science workflow and LLM/NLP components. "
            "Focus includes analysis design, narrative insight delivery, and building blocks for AI-assisted reporting."
        ),
        "highlights": [
            "A-to-Z workflow mindset: data → analysis → insight narrative → future deployment paths.",
            "Exploring LLM/NLP patterns to turn signals into usable summaries and explanations.",
            "Built as a foundation for a BI-style, decision-support dashboard.",
        ],
        "stack": ["Python (Advanced)", "NLP", "LLMs", "Analytics", "BI mindset"],
        "link_label": "View repository",
        "link_url": "https://github.com/Harshal3233/Smoking-analysis-Ai-llm-Nlp/tree/main",
        "tags": ["NLP", "LLM", "Analytics"],
    },
]

SKILLS = {
    "Recruiter Snapshot": [
        "AI Engineer", "Python (Advanced & Libraries)", "SQL", "Dashboards (Streamlit)",
        "EDA + Modeling", "Explainability (SHAP)", "Deployment mindset",
    ],
    "Programming & Data": [
        "Python (Advanced & Libraries)", "Advanced Java", "SQL",
        "EDA", "K-Means", "Regression", "Random Forest", "SVM", "Neural Networks",
        "Data Management", "Model Building & Deployment", "Predictive Analysis",
    ],
    "Tools & Platforms": ["Streamlit", "VS Code", "Jupyter Notebook", "Jira", "MS Excel", "Google Workspace"],
    "Web & Design": ["HTML", "CSS", "JavaScript", "Figma", "Interactive Dashboards"],
}

EDUCATION = [
    {
        "title": "International Master in Data Science (Ongoing)",
        "meta": "Rome Business School | Rome, Italy",
        "bullets": [
            "Applied learning through Oracle labs: data workflows, database foundations, and practical analytics.",
            "IBM labs exposure: enterprise-style problem framing, tooling practices, and real-world DS workflows.",
            "Acquired end-to-end LLM deployment concepts: AI agent integration to satisfy user queries with concise, context-driven outputs (LLM + orchestration + evaluation mindset).",
        ],
    },
    {
        "title": "B.Tech in Computer Engineering (First Class Distinction)",
        "meta": "Swarrnim Institute of Technology & Startup | Gujarat, India | 2020 – 2024",
        "bullets": [
            "Debate Champion (2020–2021).",
            "Student Council Member (2020–2024).",
            "Hackathons; supported Blood Donation Camp organization (2023).",
        ],
    },
]

INDUSTRY_EXCURSIONS = [
    {
        "title": "IBM Industry Excursion | Enterprise AI Labs",
        "meta": "Rome Business School (Industry Exposure)",
        "bullets": [
            "Interactive talk with IBM lab team on the Granite model and enterprise AI workflows.",
            "Discussion: integrating an LLM layer with Granite to produce more specific, context-aligned outputs (reduce generic responses).",
            "Worked with cybersecurity experiments and lab exercises (security-first thinking and risk surfaces).",
            "Explored quantum computing concepts and demonstrations relevant to next-gen computation and optimization.",
        ],
        "tags": ["IBM Granite", "LLM Integration", "Cybersecurity Labs", "Quantum Computing"],
    },
    {
        "title": "Owkin Industry Excursion | AI in Healthcare",
        "meta": "Rome Business School (Industry Exposure)",
        "bullets": [
            "Explored applied AI use cases and problem framing in healthcare-focused environments.",
            "Observed how organizations operationalize ML workflows and translate insights into decisions.",
        ],
        "tags": ["Healthcare AI", "Applied ML", "Problem Framing"],
    },
]

LANGUAGES = "English (Native/Bilingual), Hindi (Native), Italian (Basic – improving)"

EXPLORING = [
    "Embedding OpenAI into data science workflows (retrieval, prompting patterns, evaluation).",
    "Embeddings + semantic search for context-aware analytics and knowledge retrieval.",
    "Model building and deployment patterns (reproducibility, packaging, monitoring mindset).",
    "Strengthening applied skills through Oracle and IBM labs: data workflows, analytics, and DS tooling practices.",
    "Italian language: targeting A2 proficiency for international technical environments.",
    "Exploring LLM models and practical use cases (analysis, summarization, data assistants).",
]

BLOG_NOTES = [
    {
        "title": "How SHAP explains model drivers in real decision-making",
        "subtitle": "Interpretability as a product requirement, not a nice-to-have",
        "date": "Jan 2026",
        "read_time": "3 min read",
        "tags": ["XAI", "SHAP", "Interpretability", "Random Forest"],
        "lead": "When models influence decisions, accuracy alone is insufficient. Explainability creates trust, comparison, and accountability.",
        "bullets": [
            "Use SHAP to quantify feature contribution, not just rank importance.",
            "Compare segments using consistent explanations to avoid misleading conclusions.",
            "Translate model behavior into stakeholder language: what drives outcomes and why.",
        ],
        "callout_title": "Hard-earned lesson",
        "callout": "Models become useful when their reasoning can be challenged, explained, and improved.",
        "code_title": "Conceptual SHAP workflow",
        "code": """# Conceptual outline
model = RandomForestRegressor(...)
model.fit(X_train, y_train)

explainer = shap.Explainer(model, X_train)
shap_values = explainer(X_test)

shap.plots.bar(shap_values)
shap.plots.waterfall(shap_values[0])""",
    },
    {
        "title": "Why EDA + SVM works well for price categories",
        "subtitle": "Reframing the problem to make results stable and communicable",
        "date": "Jan 2026",
        "read_time": "3 min read",
        "tags": ["EDA", "SVM", "Classification", "Dashboards"],
        "lead": "Pricing improves when the question is reframed. EDA reveals the story; SVM provides a strong baseline for categories.",
        "bullets": [
            "Start with EDA: skew, outliers, neighborhood effects, and leakage checks.",
            "Bin prices into categories to stabilize targets and simplify the narrative.",
            "Use SVM as a dependable baseline before adding complexity.",
        ],
        "callout_title": "Hard-earned lesson",
        "callout": "A model that stakeholders understand beats a model nobody trusts.",
        "code_title": "Conceptual SVM pipeline",
        "code": """# Conceptual outline
X = features
y = price_category

pipe = Pipeline([
  ("prep", preprocessor),
  ("clf", SVC(kernel="rbf"))
])

pipe.fit(X_train, y_train)""",
    },
    {
        "title": "Deployment friction: parser & Python version mismatch",
        "subtitle": "Stabilizing builds by pinning versions and simplifying dependencies",
        "date": "Jan 2026",
        "read_time": "3 min read",
        "tags": ["Deployment", "Python", "Dependencies", "Streamlit Cloud"],
        "lead": "Deployments fail more often from environment mismatches than from code. Parser issues and Python drift are common failure points.",
        "bullets": [
            "Pin Python and core libraries to prevent resolution surprises.",
            "Remove unused heavy libraries to reduce build failures.",
            "Simplify parsing: validate input formats, use safer parsing patterns, and fall back gracefully.",
            "Treat the deployment environment as part of the system: reproducibility is a feature.",
        ],
        "callout_title": "Hard-earned lesson",
        "callout": "If a project can’t deploy consistently, it isn’t finished yet.",
        "code_title": "Conceptual fix checklist",
        "code": """# Pin python version (runtime.txt)
# python-3.11

# Pin libs (requirements.txt)
# streamlit==X.Y.Z
# scikit-learn==A.B.C

# Reduce heavy deps + validate inputs""",
    },
    {
        "title": "Streamlit vs Django: demo speed vs production structure",
        "subtitle": "Why Streamlit shines for prototypes and Django scales for permanent apps",
        "date": "Jan 2026",
        "read_time": "4 min read",
        "tags": ["Django", "Streamlit", "Architecture", "Deployment"],
        "lead": "Different tools win at different stages. Streamlit accelerates demos, Django supports durable product structure and growth.",
        "bullets": [
            "Streamlit: fast UI iteration for model demos and dashboards.",
            "Django: stronger separation of concerns, routing, auth, and database integration.",
            "Production Django requires deeper planning: segmentation, services, tasks, and thorough processing pipelines.",
            "Practical approach: Streamlit for demos; Django for permanent products with users and operations.",
        ],
        "callout_title": "Hard-earned lesson",
        "callout": "A demo sells an idea. A production app supports a business.",
        "code_title": "Conceptual architecture contrast",
        "code": """# Streamlit: demo-first
# app.py -> UI + light logic

# Django: production-first
# apps/ urls.py views.py services/ models.py tasks/ tests/""",
    },
]

# -------------------------------------------------
# Helpers
# -------------------------------------------------
def pills(items, accent=False):
    cls = "pill pill-accent" if accent else "pill"
    return "".join([f"<span class='{cls}'>{x}</span>" for x in items])

def section(title: str, subtitle: str | None = None):
    st.markdown(f"<div class='section-title'>{title}</div>", unsafe_allow_html=True)
    st.markdown("<div class='section-line'></div>", unsafe_allow_html=True)
    if subtitle:
        st.markdown(f"<div class='section-sub'>{subtitle}</div>", unsafe_allow_html=True)

def timeline_open():
    st.markdown("<div class='timeline'>", unsafe_allow_html=True)

def timeline_close():
    st.markdown("</div>", unsafe_allow_html=True)

def timeline_item(e, technical: bool):
    st.markdown("<div class='t-item'>", unsafe_allow_html=True)
    st.markdown("<div class='t-dot'></div>", unsafe_allow_html=True)
    st.markdown("<div class='t-card'>", unsafe_allow_html=True)

    st.markdown(f"<div class='t-title'>{e['role']} • {e['company']}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='t-meta'>{e['meta']}</div>", unsafe_allow_html=True)
    st.markdown(pills(e["signals"], accent=True), unsafe_allow_html=True)

    if technical:
        cols = st.columns([0.34, 0.33, 0.33], vertical_alignment="top")
        with cols[0]:
            st.markdown("**Problem**")
            st.write(e["problem"])
        with cols[1]:
            st.markdown("**Approach**")
            st.write("\n".join([f"- {x}" for x in e["approach"]]))
        with cols[2]:
            st.markdown("**Outcome**")
            st.write(e["outcome"])
    else:
        st.markdown("**Impact narrative**")
        st.write(f"{e['problem']}  \n\n**Outcome:** {e['outcome']}")

    st.markdown(pills(e["tags"]), unsafe_allow_html=True)
    st.markdown("</div></div>", unsafe_allow_html=True)

def project_card(p, technical: bool):
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown(f"<div class='card-title'>{p['title']}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='card-sub'>{p['one_liner']}</div>", unsafe_allow_html=True)

    if technical:
        st.markdown(pills(p["stack"]), unsafe_allow_html=True)
        st.markdown("**Summary**")
        st.write(p["summary"])
        st.markdown("**Highlights**")
        st.write("\n".join([f"- {x}" for x in p["highlights"]]))
    else:
        st.write(p["summary"])
        st.markdown(pills([*p["tags"]], accent=True), unsafe_allow_html=True)

    st.markdown(
        f"<div class='visit small-muted'><a href='{p['link_url']}' target='_blank'>{p['link_label']} ↗</a></div>",
        unsafe_allow_html=True,
    )
    st.markdown("</div>", unsafe_allow_html=True)

def note_card(note):
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown(f"<div class='card-title'>{note['title']}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='card-sub'>{note['subtitle']}</div>", unsafe_allow_html=True)
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
    st.write(note["lead"])
    with st.expander("Read full note"):
        st.write("\n".join([f"- {x}" for x in note["bullets"]]))
        st.markdown(
            f"""
<div class="callout">
  <strong>{note["callout_title"]}:</strong> {note["callout"]}
</div>
""",
            unsafe_allow_html=True,
        )
        st.markdown("**" + note["code_title"] + "**")
        st.markdown(f"<div class='codebox'><pre>{note['code']}</pre></div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

def delivery_radar():
    labels = [
        "SQL", "Data (CSV/API)", "Cleaning", "EDA", "Feature Eng",
        "Modeling", "Evaluation", "Explainability", "Dashboard UI", "Deployment"
    ]
    scores = np.array([8, 8, 7, 8, 7, 8, 7, 8, 9, 8], dtype=float)

    angles = np.linspace(0, 2*np.pi, len(labels), endpoint=False)
    scores_loop = np.concatenate([scores, [scores[0]]])
    angles_loop = np.concatenate([angles, [angles[0]]])

    fig = plt.figure(figsize=(5.0, 3.8), dpi=140)
    ax = plt.subplot(111, polar=True)

    ax.plot(angles_loop, scores_loop, linewidth=2)
    ax.fill(angles_loop, scores_loop, alpha=0.12)

    ax.set_xticks(angles)
    ax.set_xticklabels(labels, fontsize=7)
    ax.set_yticks([2, 4, 6, 8, 10])
    ax.set_yticklabels(["2", "4", "6", "8", "10"], fontsize=7)
    ax.set_ylim(0, 10)
    ax.grid(alpha=0.25)
    ax.set_title("A→Z Data Science Delivery", fontsize=10, pad=12, fontweight="bold")
    fig.tight_layout()
    return fig

# -------------------------------------------------
# HERO (top)
# -------------------------------------------------
st.markdown("<div class='hero'>", unsafe_allow_html=True)
left, right = st.columns([0.72, 0.28], vertical_alignment="top")

with left:
    st.markdown(f"<div class='hero-title'>{PROFILE['name']}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='hero-tag'>{PROFILE['tagline']}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='hero-meta'>{PROFILE['location']}</div>", unsafe_allow_html=True)
    st.markdown("<div style='height:0.55rem;'></div>", unsafe_allow_html=True)
    st.write(ABOUT)
    st.markdown(
        """
<div class="hero-cta">
  <span class="pill pill-accent">AI Engineer</span>
  <span class="pill">Dashboards</span>
  <span class="pill">ML + Explainability</span>
  <span class="pill">Deployment</span>
</div>
""",
        unsafe_allow_html=True,
    )

with right:
    st.markdown(
        "<div class='kpi'><div class='kpi-label'>Deployed Apps / Projects</div><div class='kpi-value'>3</div></div>",
        unsafe_allow_html=True,
    )
    st.markdown("<div style='height:0.7rem;'></div>", unsafe_allow_html=True)
    st.markdown("<div class='kpi'><div class='kpi-label'>Core Stack</div><div class='kpi-value'>Python + ML</div></div>", unsafe_allow_html=True)
    st.markdown("<div style='height:0.7rem;'></div>", unsafe_allow_html=True)
    st.markdown(
        f"""
<div class='kpi'>
  <div class='kpi-label'>Contact</div>
  <div class='kpi-value'>
    <a href="{PROFILE['linkedin']}" target="_blank"
       style="text-decoration:none; color:{BRAND['accent']}; font-weight:950;">
      LinkedIn ↗
    </a>
  </div>
</div>
""",
        unsafe_allow_html=True,
    )

st.markdown("</div>", unsafe_allow_html=True)

# -------------------------------------------------
# Explore My Work (Header + graph + tabs)
# -------------------------------------------------
section("Explore My Work", "Two views: recruiter-friendly and technical deep-dive.")

hleft, hright = st.columns([0.62, 0.38], vertical_alignment="top")
with hleft:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<div class='card-title'>End-to-end delivery mindset</div>", unsafe_allow_html=True)
    st.write(
        "A full data science project isn’t just modeling. It’s a pipeline: data acquisition → analysis → modeling → "
        "explainability → dashboard UX → deployment. This dashboard shows that delivery flow clearly."
    )
    st.markdown(pills(["SQL", "EDA", "Modeling", "Explainability", "Dashboard UX", "Deployment"], accent=True), unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

with hright:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.pyplot(delivery_radar(), clear_figure=True)
    st.markdown("</div>", unsafe_allow_html=True)

tab_recruiter, tab_technical = st.tabs(["Recruiter View", "Technical View"])

# =========================
# Recruiter View
# =========================
with tab_recruiter:
    # Auto-adjust layout: keep it clean
    c1, c2, c3, c4 = st.columns([1.05, 1.05, 1.05, 0.95])

    with c1:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("<div class='card-title'>Snapshot</div>", unsafe_allow_html=True)
        st.write("AI Engineer with deployed dashboards and ML projects (Explainability + classification + NLP exploration).")
        st.markdown(pills(["AI Engineer", "Python", "SQL", "Streamlit", "SHAP", "SVM", "NLP"], accent=True), unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with c2:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("<div class='card-title'>Projects</div>", unsafe_allow_html=True)
        st.write("3 projects: 2 deployed Streamlit apps + 1 AI/LLM/NLP analytics repository.")
        st.markdown(pills(["3 Projects", "2 Deployed Apps", "1 Repo"], accent=True), unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with c3:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("<div class='card-title'>Contact</div>", unsafe_allow_html=True)
        st.write(f"Email: {PROFILE['email']}")
        st.write(f"Phone: {PROFILE['phone']}")
        st.markdown(
            f"<div class='visit small-muted'><a href='{PROFILE['linkedin']}' target='_blank'>LinkedIn ↗</a></div>",
            unsafe_allow_html=True,
        )
        st.markdown("</div>", unsafe_allow_html=True)

    with c4:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("<div class='card-title'>Reference</div>", unsafe_allow_html=True)
        r = REFERENCES[0]
        st.markdown(f"**{r['name']}**")
        st.markdown(f"<div class='small-muted'>{r['role']}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='small-muted'>✉️ {r['email']}</div>", unsafe_allow_html=True)
        st.markdown(
            f"<div class='visit small-muted'>🔗 <a href='{r['linkedin']}' target='_blank'>LinkedIn ↗</a></div>",
            unsafe_allow_html=True,
        )
        st.markdown("</div>", unsafe_allow_html=True)

    section("Experience", "Impact-first narrative.")
    timeline_open()
    for e in EXPERIENCE:
        timeline_item(e, technical=False)
    timeline_close()

    section("Projects", "Simple summaries with links.")
    for p in PROJECTS:
        project_card(p, technical=False)

    section("Languages", None)
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.write(LANGUAGES)
    st.markdown("</div>", unsafe_allow_html=True)

# =========================
# Technical View
# =========================
with tab_technical:
    section("Exploration Tracks", "LLMs, orchestration, deployment patterns.")
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.write("\n".join([f"- {x}" for x in EXPLORING]))
    st.markdown(pills(["Oracle Labs", "IBM Labs", "Embeddings", "LLMs", "Deployment Patterns"], accent=True), unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    section("Experience Timeline", "Problem → Approach → Outcome.")
    timeline_open()
    for e in EXPERIENCE:
        timeline_item(e, technical=True)
    timeline_close()

    section("Projects", "Full detail: stack, highlights, and links.")
    for p in PROJECTS:
        project_card(p, technical=True)

    section("Skills", "Toolbox view.")
    cols = st.columns(3)
    keys = ["Programming & Data", "Tools & Platforms", "Web & Design"]
    for i, k in enumerate(keys):
        with cols[i]:
            st.markdown("<div class='card'>", unsafe_allow_html=True)
            st.markdown(f"<div class='card-title'>{k}</div>", unsafe_allow_html=True)
            st.markdown(pills(SKILLS[k]), unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)

    section("Notes", "Explainability + deployment + architecture.")
    for note in BLOG_NOTES:
        note_card(note)

    section("Contact", None)
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.write(f"- **Email:** {PROFILE['email']}")
    st.write(f"- **Phone:** {PROFILE['phone']}")
    st.write(f"- **LinkedIn:** {PROFILE['linkedin']}")
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown(
    "<div class='small-muted' style='margin-top:1.2rem;'>Built with Streamlit • Deployed on Streamlit Cloud</div>",
    unsafe_allow_html=True,
)
