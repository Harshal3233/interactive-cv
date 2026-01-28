import streamlit as st

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Harshal M Patel | AI Engineer",
    layout="wide"
)

# -----------------------------
# Custom Styling (Professional)
# -----------------------------
st.markdown("""
<style>
.block-container { padding-top: 2rem; padding-bottom: 2rem; }
.name { font-size: 2.2rem; font-weight: 800; }
.tagline { font-size: 1.1rem; font-weight: 600; color: #444; }
.section { font-size: 1.4rem; font-weight: 700; margin-top: 2rem; }
.card {
    border: 1px solid #e1e4e8;
    border-radius: 12px;
    padding: 1.2rem;
    margin-bottom: 1rem;
    background-color: #ffffff;
}
.pill {
    display: inline-block;
    padding: 0.3rem 0.7rem;
    margin: 0.2rem 0.3rem 0.2rem 0;
    border-radius: 999px;
    border: 1px solid #d0d7de;
    font-size: 0.85rem;
}
.muted { color: #6a737d; }
</style>
""", unsafe_allow_html=True)

# -----------------------------
# Header
# -----------------------------
st.markdown("<div class='name'>Harshal M Patel</div>", unsafe_allow_html=True)
st.markdown("<div class='tagline'>AI Engineer | Data Science | Software Engineering | Analytics</div>", unsafe_allow_html=True)
st.markdown("<div class='muted'>Rome, Italy (available to relocate)</div>", unsafe_allow_html=True)

st.write(" harshalmpatel2001@gmail.com |  +91 9974890592 |  LinkedIn")

# -----------------------------
# About Me
# -----------------------------
st.markdown("<div class='section'>About Me</div>", unsafe_allow_html=True)
st.write(
    "Driven by curiosity for technology and a passion for transforming data into meaningful insights, "
    "I bring analytical thinking, technical proficiency, and clear communication. My background across "
    "multiple institutions has strengthened my adaptability and broadened my problem-solving approach. "
    "With a strong foundation in data management, machine learning concepts, and storytelling through data, "
    "along with sales and mentorship experience, I aim to deliver impactful, data-driven solutions with elegance."
)

# -----------------------------
# Experience (FIRST)
# -----------------------------
st.markdown("<div class='section'>Professional Experience</div>", unsafe_allow_html=True)

with st.container():
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("IT & Marketing Support | Vinayak Infotech")
    st.caption("Ahmedabad, India | May 2024 – 2025")
    st.write("""
    - Assisted in installation and setup of computer systems and hardware.
    - Mentored software team members in Java, Python (advanced and libraries), and testing tasks.
    - Streamlined marketing team workflows and provided technical assistance to improve efficiency.
    """)
    st.markdown("""
    <span class='pill'>Python</span>
    <span class='pill'>Java</span>
    <span class='pill'>Mentorship</span>
    <span class='pill'>IT Support</span>
    """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

with st.container():
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("Software Engineer | Cignex Datamatics")
    st.caption("Gujarat, India | Aug 2022 – Jul 2023")
    st.write("""
    - Developed testing scripts using Jira and collaborated closely with QA teams.
    - Resolved bugs and improved system performance for multinational clients.
    - Contributed to Java-based projects and testing environments.
    """)
    st.markdown("""
    <span class='pill'>Java</span>
    <span class='pill'>Jira</span>
    <span class='pill'>QA Collaboration</span>
    """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

with st.container():
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("Software Engineering Intern | Axis Ray Technology")
    st.caption("Gujarat, India | Jun 2022 – Dec 2022")
    st.write("""
    - Gained advanced proficiency in Java, Advanced Java, and SQL.
    - Worked on real-world projects with cross-national teams.
    - Mentored peers and contributed to successful project delivery.
    """)
    st.markdown("""
    <span class='pill'>Advanced Java</span>
    <span class='pill'>SQL</span>
    <span class='pill'>Team Collaboration</span>
    """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

with st.container():
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("Sales Executive | Aura Ethnics")
    st.caption("Jan 2022 – Jun 2022")
    st.write("""
    - Managed online sales channels using Google Analytics insights.
    - Improved traffic, conversions, and repeat customers through data-driven decisions.
    - Delivered personalized in-store sales experiences using brand storytelling.
    """)
    st.markdown("""
    <span class='pill'>Analytics</span>
    <span class='pill'>Sales Strategy</span>
    <span class='pill'>Customer Engagement</span>
    """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# -----------------------------
# Skills
# -----------------------------
st.markdown("<div class='section'>Skills</div>", unsafe_allow_html=True)

st.markdown("**Programming & Data**")
st.markdown("""
<span class='pill'>Python (Advanced & Libraries)</span>
<span class='pill'>Advanced Java</span>
<span class='pill'>SQL</span>
<span class='pill'>EDA</span>
<span class='pill'>K-Means</span>
<span class='pill'>Regression</span>
<span class='pill'>Random Forest</span>
<span class='pill'>SVM</span>
<span class='pill'>Neural Networks</span>
<span class='pill'>Data Management</span>
<span class='pill'>Model Building & Deployment</span>
<span class='pill'>Predictive Analysis</span>
""", unsafe_allow_html=True)

st.markdown("**Tools & Platforms**")
st.markdown("""
<span class='pill'>Streamlit</span>
<span class='pill'>VS Code</span>
<span class='pill'>Jupyter Notebook</span>
<span class='pill'>GitHub</span>
<span class='pill'>Jira</span>
<span class='pill'>MS Excel</span>
<span class='pill'>Google Workspace</span>
""", unsafe_allow_html=True)

st.markdown("**Web & Design**")
st.markdown("""
<span class='pill'>HTML</span>
<span class='pill'>CSS</span>
<span class='pill'>JavaScript</span>
<span class='pill'>Figma</span>
<span class='pill'>Interactive Dashboards</span>
""", unsafe_allow_html=True)

# -----------------------------
# Education
# -----------------------------
st.markdown("<div class='section'>Education</div>", unsafe_allow_html=True)

with st.container():
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("International Master in Data Science")
    st.caption("Rome Business School | Rome, Italy | Ongoing")
    st.write("""
    - Strengthening theoretical and practical data science foundations.
    - Participated in industry excursions with organizations such as IBM and Owkin.
    - Gaining hands-on experience through applied projects and Oracle labs.
    """)
    st.markdown("</div>", unsafe_allow_html=True)

with st.container():
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("Bachelor of Technology in Computer Engineering")
    st.caption("Swarrnim Institute of Technology & Startup | Gujarat, India | 2020 – 2024")
    st.write("""
    - First Class Distinction.
    - Debate Champion (2020–2021).
    - Active participant in hackathons and student initiatives.
    """)
    st.markdown("</div>", unsafe_allow_html=True)

# -----------------------------
# Languages
# -----------------------------
st.markdown("<div class='section'>Languages</div>", unsafe_allow_html=True)
st.write("English (Native/Bilingual), Hindi (Native), Italian (Basic – improving)")
