# 🤖 AI-Powered Skill Assessment & Personalized Learning Plan Agent

## 📌 Overview

This project is an AI-powered hiring assistant that evaluates candidates beyond traditional resume screening.
It analyzes resumes, matches skills with job requirements, conducts assessments (including coding questions), and provides personalized learning recommendations.

The goal is to improve hiring accuracy and help candidates understand and enhance their skill gaps.

---

## 🚀 Key Features

### 📄 Resume Analysis

* Upload resume in PDF format
* Extracts technical skills automatically

### 🧠 Skill Matching

* Compares resume skills with job description
* Identifies matched and missing skills

### ❓ Assessment Engine

* Generates minimum 10 questions
* Includes **coding questions**
* Timer-based evaluation

### ✅ Answer Evaluation

* Keyword-based answer validation
* Calculates answer score

### 🎯 Final Decision System

* Combines resume + assessment scores
* Provides hiring recommendation

### 📊 Visualization

* Performance chart using Chart.js
* Score breakdown

### 🧠 AI Summary

* Highlights strengths and weaknesses

### ❌ Missing Skills Detection

* Identifies gaps in candidate profile

### 📚 Learning Plan

* Suggests improvement roadmap

### 🏆 Leaderboard

* Displays top candidate scores

### 📄 Report Generation

* Downloadable PDF report

### 🌙 UI Features

* Clean modern UI
* Dark mode toggle

---

## 🛠 Tech Stack

* **Backend:** Python (Flask)
* **Frontend:** HTML, CSS, JavaScript
* **Libraries:**

  * PyPDF2 (Resume parsing)
  * ReportLab (PDF generation)
  * Chart.js (Graphs)

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run Application

```bash
python app.py
```

### 4️⃣ Open in Browser

http://127.0.0.1:5000

---

## 📊 System Workflow

1. User enters Job Description
2. Uploads Resume (PDF)
3. System extracts skills
4. Matches with required skills
5. Generates assessment questions
6. Candidate answers questions
7. System evaluates responses
8. Calculates final score
9. Displays:

   * Summary
   * Missing skills
   * Learning plan
   * Charts
   * Leaderboard
   * Report download

---

## 📥 Sample Input

**Job Description:**

```
Looking for a Python Developer with SQL knowledge
```

**Resume:**

```
Skills: Python, SQL
```

---

## 📤 Sample Output

* Resume Score: 80%
* Answer Score: 70%
* Final Score: 77%
* Decision: Strong Candidate – Ready for Hiring
* Missing Skills: Machine Learning
* Learning Plan: Suggested resources

---

## 🎯 Use Cases

* 👨‍💼 Recruiters: Faster and more accurate screening
* 🎓 Students: Self-evaluation and skill improvement
* 🏫 Institutions: Candidate assessment system

---

## 🔮 Future Scope

* NLP-based semantic answer evaluation
* Code execution engine for coding questions
* Database integration
* User login system
* Cloud deployment

---

## 👤 Author

**Hitha B M**

---

## ⭐ Conclusion

This system bridges the gap between resume screening and actual skill validation by combining automated analysis with real-time assessment and feedback.
It makes hiring smarter and learning more personalized.
