from flask import Flask, request, render_template, redirect, url_for, session, send_file
from PyPDF2 import PdfReader
import random
import io
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

app = Flask(__name__)
app.secret_key = "secret123"

leaderboard = []

skills_list = ["python","java","sql","machine learning","html","css","javascript"]

questions_db = {
    "python": ["What is Python?", "What is decorator?", "Explain generators"],
    "sql": ["What is SQL?", "What is JOIN?", "Explain normalization"],
    "java": ["What is JVM?", "What is inheritance?", "What is abstraction"],
}

general_questions = [
    "What is API?", "What is Git?", "What is debugging?",
    "What is database?", "What is cloud computing?"
]

coding_questions = [
    "Write a Python program to check if a number is prime.",
    "Write a program to reverse a string."
]

answer_keywords = {
    "python": ["decorator","function","generator"],
    "sql": ["join","query","table"],
    "java": ["jvm","runtime","thread"]
}

# ---------------- FUNCTIONS ---------------- #

def extract_text_from_pdf(file):
    reader = PdfReader(file)
    text = ""
    for p in reader.pages:
        if p.extract_text():
            text += p.extract_text()
    return text

def extract_skills(text):
    return [s for s in skills_list if s in text.lower()]

def match_skills(jd, resume):
    return list(set(jd)&set(resume)), list(set(jd)-set(resume))

def score(jd, matched):
    return round((len(matched)/len(jd))*100,2) if jd else 0


# ---------------- ROUTES ---------------- #

@app.route("/", methods=["GET","POST"])
def home():
    if request.method=="POST":
        session.clear()

        jd = request.form["jd"]
        file = request.files['resume_file']

        if file.filename=="":
            return render_template("index.html", error="Please upload a file ❌")

        if not file.filename.lower().endswith(".pdf"):
            return render_template("index.html", error="Only PDF format is allowed ❌")

        resume_text = extract_text_from_pdf(file)

        jd_skills = extract_skills(jd)
        resume_skills = extract_skills(resume_text)

        matched, missing = match_skills(jd_skills, resume_skills)
        resume_score = score(jd_skills, matched)

        # QUESTIONS
        questions=[]
        for skill in matched:
            if skill in questions_db:
                questions.extend(questions_db[skill])

        if len(questions)<10:
            questions.extend(general_questions)

        random.shuffle(questions)
        questions = questions[:10]
        questions.extend(coding_questions)

        # SUMMARY
        strengths = ", ".join(matched) if matched else "No strong skills"
        gaps = ", ".join(missing) if missing else "No major gaps"

        summary = f"Candidate shows strengths in {strengths}. Improvement needed in {gaps}."

        # PLAN
        plan = {}
        if missing:
            for skill in missing:
                plan[skill] = {
                    "resource": f"Learn {skill} via online resources",
                    "time": "1-2 weeks"
                }
        else:
            plan["Advanced Practice"] = {
                "resource": "Build projects",
                "time": "Ongoing"
            }

        session.update({
            "questions": questions,
            "answers": [],
            "current_q": 0,
            "score": resume_score,
            "matched": matched,
            "missing": missing,
            "plan": plan,
            "summary": summary
        })

        return redirect(url_for("chatbot"))

    return render_template("index.html")


@app.route("/chatbot", methods=["GET","POST"])
def chatbot():
    q = session.get("questions",[])
    i = session.get("current_q",0)

    if request.method=="POST":
        session["answers"].append(request.form["answer"])
        session["current_q"]=i+1
        i+=1

    if i<len(q):
        return render_template("chatbot.html", question=q[i], q_no=i+1)

    return redirect(url_for("final"))


@app.route("/final")
def final():
    answers=session.get("answers",[])
    questions=session.get("questions",[])

    correct=0
    results=[]

    for i in range(len(answers)):
        ans=answers[i].lower()
        q=questions[i].lower()
        is_correct=False

        if "write" in q:
            if len(ans.strip()) > 10:
                correct += 1
                is_correct = True
        else:
            for skill,words in answer_keywords.items():
                if skill in q:
                    if any(w in ans for w in words):
                        correct+=1
                        is_correct=True
                    break

        results.append((questions[i],answers[i],is_correct))

    answer_score=(correct/len(answers))*100 if answers else 0
    resume_score=session.get("score",0)

    overall=round((resume_score*0.7)+(answer_score*0.3),2)

    if overall>75:
        decision="Strong Candidate – Ready for Hiring"
    elif overall>50:
        decision="Needs Improvement"
    else:
        decision="Not Suitable"

    leaderboard.append({"name":"Candidate","score":overall})
    leaderboard.sort(key=lambda x:x["score"], reverse=True)

    return render_template(
        "final.html",
        score=resume_score,
        answer_score=answer_score,
        overall=overall,
        decision=decision,
        results=results,
        leaderboard=leaderboard,
        missing=session.get("missing"),
        plan=session.get("plan"),
        summary=session.get("summary")
    )


# 🔥 FIXED DOWNLOAD ROUTE
@app.route("/download")
def download():
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer)
    styles = getSampleStyleSheet()

    content=[]
    content.append(Paragraph("Assessment Report",styles['Title']))
    content.append(Paragraph(f"Resume Score: {session.get('score')}%",styles['Normal']))
    content.append(Paragraph(f"Summary: {session.get('summary')}",styles['Normal']))

    doc.build(content)
    buffer.seek(0)

    return send_file(buffer, as_attachment=True, download_name="report.pdf")


if __name__=="__main__":
    app.run(debug=True)
