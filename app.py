import streamlit as st
import fitz  # PyMuPDF
import os

# -------------- PAGE CONFIG --------------
st.set_page_config(page_title="HireSense AI - Where You Fit In", layout="centered")

# -------------- DARK MODE STYLING --------------
st.markdown("""
    <style>
    .reportview-container {
        background-color: #0e1117;
        color: white;
    }
    .sidebar .sidebar-content {
        background-color: #0e1117;
    }
    .stButton>button {
        color: white;
        background-color: #9146FF;
        border-radius: 10px;
        padding: 0.5em 1em;
        font-size: 16px;
    }
    .stFileUploader {
        color: white;
    }
    .highlight {
        font-size: 28px;
        font-weight: bold;
        color: #10FFCB;
        text-align: center;
        padding: 10px 0;
    }
    .tagline {
        font-size: 18px;
        font-weight: 400;
        background: linear-gradient(to right, #8e2de2, #4a00e0);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        padding-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# -------------- HEADER --------------
st.markdown("<h1 style='text-align: center;'>📄 HireSense AI - Where You Fit In</h1>", unsafe_allow_html=True)
st.markdown("<p class='tagline'>✨An AI-powered tool that understands your resume and predicts your most suitable tech role 🚀</p>", unsafe_allow_html=True)

# -------------- FUNCTION TO EXTRACT TEXT --------------
def extract_text_from_pdf(pdf_file):
    doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text.lower()

# ------------------ JOB KEYWORDS ------------------
job_keywords = {
    "👨‍🔬 Data Scientist": [
        "machine learning", "deep learning", "pandas", "numpy", "scikit-learn", "tensorflow",
        "keras", "data analysis", "matplotlib", "seaborn", "model training"
    ],
    "📊 Data Analyst": [
        "sql", "excel", "power bi", "tableau", "data visualization", "pivot tables", "reporting",
        "dashboards", "insights", "statistics"
    ],
    "💻 Web Developer": [
        "html", "css", "javascript", "react", "vue", "frontend", "bootstrap", "tailwind",
        "node.js", "express", "web development"
    ],
    "🧠 AI/ML Engineer": [
        "neural networks", "pytorch", "tensorflow", "model deployment", "inference",
        "feature engineering", "nlp", "computer vision", "model optimization", "huggingface"
    ],
    "🛠 Backend Developer": [
        "node.js", "django", "flask", "api", "rest", "graphql", "mongodb", "postgresql",
        "database design", "server", "python", "java", "spring boot"
    ],
    "📱 Mobile App Developer": [
        "flutter", "dart", "kotlin", "android", "ios", "swift", "react native", "mobile app",
        "play store", "xcode"
    ],
    "🔐 Cybersecurity Analyst": [
        "vulnerability", "penetration testing", "firewall", "security", "network security",
        "threat detection", "malware", "owasp", "encryption", "forensics"
    ],
    "🌐 DevOps Engineer": [
        "docker", "kubernetes", "jenkins", "ansible", "terraform", "ci/cd", "cloud",
        "aws", "azure", "gcp", "monitoring", "devops"
    ],
    "☁️ Cloud Engineer": [
        "aws", "azure", "gcp", "cloud architecture", "lambda", "s3", "ec2", "cloudwatch",
        "infrastructure", "cloudformation", "terraform"
    ],
    "📈 Business Analyst": [
        "requirement gathering", "stakeholder", "analysis", "kpi", "process improvement",
        "gap analysis", "reporting", "communication", "problem solving"
    ],
    "🧩 Software Engineer": [
        "software engineer", "software development", "programming", "git", "agile", "ci/cd"
    ],
    "💻 Software Developer": ["software developer", "application development", 
        "java", "c++", "c#", "python"
    ],
    "🌐 Front-End Engineer": ["react", "angular", "vue", "html", "css", "javascript", "frontend engineer"],
    "⚙ Back-End Engineer": ["java", "python", "node.js", "api", "microservices", "database", "server-side"],
    "🔁 Full-Stack Developer": ["full-stack", "frontend", "backend", "end-to-end development", "mern", "mean"],
    "📦 QA / Test Engineer": ["qa", "test engineer", "selenium", "junit", "automation testing", "manual testing"],
    "🛠 DevOps Engineer": ["ci/cd", "jenkins", "docker", "kubernetes", "infrastructure as code", "ansible"],
    "☁ Cloud Architect": ["aws", "azure", "gcp", "solution architecture", "cloud architecture", "cloud migration"],
    "🔐 Security Engineer": ["security engineer", "vulnerability assessment", "penetration testing", "owasp", "encryption"],
    "🗃 Data Engineer": ["data engineer", "hadoop", "spark", "etl", "data pipelines", "big data"],
    "🐍 Python Developer": ["python developer", "django", "flask", "pip", "virtualenv", "pipenv"],
    "☕ Java Developer": ["java developer", "spring", "hibernate", "jvm", "maven", "gradle"],
    "📱 iOS Developer": ["swift", "objc", "ios developer", "xcode", "cocoa", "app store"],
    "📱 Android Developer": ["android developer", "kotlin", "java android", "gradle", "sdk"],
    "📊 Data Engineer": ["data engineer", "spark", "kafka", "etl", "data warehouse"],  
    "🧑‍💼 Project Manager": [
        "agile", "scrum", "kanban", "jira", "project planning", "resource allocation",
        "timeline", "stakeholder", "milestones", "risk management"
    ],
    "💼 Product Manager": [
        "product lifecycle", "roadmap", "user stories", "mvp", "market research",
        "a/b testing", "feature prioritization", "customer feedback"
    ],
    "📝 Content Writer": [
        "seo", "blog writing", "copywriting", "editing", "content marketing",
        "proofreading", "social media content", "creative writing"
    ],
    "🎨 UI/UX Designer": [
        "figma", "adobe xd", "wireframes", "user research", "design thinking",
        "prototypes", "user flows", "usability testing", "interaction design"
    ],
    "📢 Digital Marketer": [
        "seo", "sem", "google ads", "facebook ads", "email marketing", "conversion rate",
        "analytics", "campaign", "retargeting", "marketing automation"
    ],
    "📱 Social Media Manager": [
        "instagram", "facebook", "twitter", "linkedin", "canva", "reels",
        "hashtags", "analytics", "caption writing", "social strategy"
    ],
    "🎬 Video Editor": [
        "premiere pro", "after effects", "storyboarding", "transitions",
        "color grading", "motion graphics", "timeline", "editing"
    ],
    "📞 Customer Support": [
        "crm", "ticketing", "live chat", "phone support", "zendesk",
        "customer satisfaction", "resolution", "follow up", "support desk"
    ],
    "🧾 HR Executive": [
        "recruitment", "onboarding", "hrms", "payroll", "employee engagement",
        "compliance", "grievance handling", "training", "talent acquisition"
    ],
    "🧮 Accountant": [
        "tally", "gst", "invoice", "reconciliation", "ledger", "trial balance",
        "balance sheet", "financial reports", "bookkeeping", "audit"
    ],
    "🌍 International Business": [
        "global markets", "export", "import", "trade finance", "international strategy",
        "cross-border", "global compliance", "market entry"
    ],
    "📚 Academic Researcher": [
        "literature review", "research methodology", "citation", "academic writing",
        "journals", "survey", "publication", "peer review"
    ],
    "⚙ Mechanical Engineer": [
        "cad", "solidworks", "autocad", "thermodynamics", "manufacturing",
        "engineering design", "material science", "prototyping"
    ],
    "🧪 Quality Analyst": [
        "manual testing", "automation testing", "test cases", "bug reporting",
        "selenium", "jmeter", "qa process", "defect tracking"
    ],
    "🛍 E-Commerce Specialist": [
        "shopify", "woocommerce", "product listings", "order fulfillment",
        "cart recovery", "sales analytics", "inventory", "customer reviews"
    ]
}

# ------------------ CLASSIFIER FUNCTION ------------------
def classify_resume(text):
    scores = {}

    for role, keywords in job_keywords.items():
        match_count = sum(1 for keyword in keywords if keyword in text)
        scores[role] = match_count

    total_matches = sum(scores.values())
    if total_matches == 0:
        return "🤷 Unknown Role", scores

    return max(scores, key=scores.get), scores

# -------------- FILE UPLOADER --------------
uploaded_file = st.file_uploader("📄 Upload Resume (PDF format only)", type=["pdf"])

if not uploaded_file:
    st.info("👆 Upload a resume file to get started.")

# -------------- CLASSIFICATION RESULT --------------
if uploaded_file:
    st.success("✅ File Uploaded Successfully!")

    with st.spinner("🔍 Analyzing your resume..."):
        extracted_text = extract_text_from_pdf(uploaded_file)
        prediction, scores = classify_resume(extracted_text)

    # 🎯 Show prediction
    st.markdown("### 🧠 AI Prediction Result:")
    st.markdown(f"<div class='highlight'>{prediction}</div>", unsafe_allow_html=True)

    # 📊 Show bar chart of top 4 roles
    sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)[:4]
    chart_data = {role: score for role, score in sorted_scores}

    st.markdown("### 📊 Top 4 Matching Roles")
    st.bar_chart(chart_data)

st.markdown("---")  # separator line

st.markdown("""
<div style='text-align: center; padding: 20px 0; font-size: 16px; color: #CCCCCC;'>
🔍 <b>HireSense AI</b> is your intelligent assistant for resume role prediction.<br>
Designed to help HR professionals screen talent faster and smarter.<br><br>

Whether you're hiring — or hoping to get hired —<br>
<b>HireSense</b> shows you exactly <i>where you fit in</i> 💼✨
</div>
""", unsafe_allow_html=True)