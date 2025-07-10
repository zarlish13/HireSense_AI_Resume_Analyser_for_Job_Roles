# 💼 HireSense AI – Resume Analyser for Job Role Detection

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://hiresense-ai.streamlit.app/)
[![GitHub stars](https://img.shields.io/github/stars/zarlish13/HireSense_AI_Resume_Analyser_for_Job_Roles.svg?style=social)](https://github.com/zarlish13/HireSense_AI_Resume_Analyser_for_Job_Roles)

> 🔍 *"Where you fit in... just one upload away."*  
> **HireSense AI** helps job seekers discover the most relevant job role based on their resume content — with an instant, AI-assisted classification and beautiful analytics.

---

## 🚀 Live Demo
👉 [https://hiresense-ai.streamlit.app/](https://hiresense-ai.streamlit.app/)

---

## 🧠 About the Project

**HireSense AI** is a keyword-based, AI-powered resume classifier built using Python & Streamlit. Just upload your PDF resume, and it instantly predicts the job roles you're best suited for — from **Data Scientist** to **Content Writer**, **DevOps**, **HR**, **Cybersecurity**, and more.

Designed with:
- 🎨 A clean, dark UI theme
- 📊 Top 4 job role match bar chart
- ✨ Poetic predictions and engaging feedback
- 💼 Practical use cases for both **HR** and **candidates**

---

## 🎯 Who Is It For?

- **Job Seekers** – Understand where your resume fits best
- **HR Professionals** – Speed up resume screening
- **Students & Developers** – Learn NLP, Streamlit, and UI design

---

## 📄 Sample Roles Detected

- 👨‍🔬 Data Scientist
- 📊 Data Analyst
- 💻 Web Developer
- 🧠 AI/ML Engineer
- 🛠 Backend Developer
- 📱 Mobile App Developer
- 🔐 Cybersecurity Analyst
- 🌐 DevOps Engineer
- ☁️ Cloud Engineer
- 📈 Business Analyst
- 🧾 HR Executive
- 💼 Product Manager
- 📝 Content Writer
- 🎨 UI/UX Designer
- 🧮 Accountant
- 🧩 Software Engineer
- ⚙️ Mechanical Engineer
- 📢 Digital Marketer
- 📞 Customer Support
- ...and more!

> ✅ 25+ roles supported and easy to extend

---

## 🛠 Tech Stack

| Tool      | Use                                  |
|-----------|---------------------------------------|
| 🐍 Python | Core language                         |
| 🧾 PyMuPDF | PDF text extraction                   |
| ⚙️ Streamlit | Web app UI & interactivity           |
| 🎨 CSS & Emojis | Aesthetic UI & improved UX         |

---

## 📦 How to Run Locally

git clone https://github.com/zarlish13/HireSense_AI_Resume_Analyser_for_Job_Roles.git
cd HireSense_AI_Resume_Analyser_for_Job_Roles
pip install -r requirements.txt
streamlit run app.py
📝 Requires Python 3.7+ and pip

📁 Folder Structure
bash
Copy
Edit
HireSenseAI/
├── app.py                 # Main Streamlit app
├── requirements.txt       # Python dependencies
├── README.md              # This file!
├── sample_resumes/        # Optional: dummy PDFs
├── .gitignore             # To exclude venv, __pycache__, etc.
🎯 How It Works
Upload a resume (PDF)

Resume is parsed and converted to lowercase text

Keywords are matched against a dictionary of job roles

The role with the highest match is predicted

Bar chart displays top 4 matches

Summary & poetic message wraps it up

✨ Screenshot
(Insert a screenshot of your running app here)

💡 Future Improvements
✅ TF-IDF based scoring

✅ Multiple resume upload

🧠 Add ML/NLP model for smarter matching

💬 Feedback form or contact field

🧑‍💻 GitHub Action to deploy updates

🤝 Contributions Welcome!
Want to improve role detection? Add new job categories? Enhance UI?
Feel free to fork and contribute!
Open an issue or submit a PR 🚀

📬 Connect with Me
🧑‍💻 GitHub: @zarlish13

💌 Email: zarlishfathima@gmail.com

🌐 Project: hiresense-ai.streamlit.app
