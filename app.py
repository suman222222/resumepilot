from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/preview", methods=["POST"])
def preview():

    data = {
    "name": request.form.get("name"),
    "email": request.form.get("email"),
    "phone": request.form.get("phone"),
    "linkedin": request.form.get("linkedin"),
    "github": request.form.get("github"),
    "education": request.form.get("education"),
    "skills": request.form.get("skills"),
    "projects": request.form.get("projects"),
    "experience": request.form.get("experience"),
    "summary": request.form.get("summary"),
    "certifications": request.form.get("certifications")
}
    

    return render_template("preview.html", data=data)


if __name__ == "__main__":
    app.run(debug=True)