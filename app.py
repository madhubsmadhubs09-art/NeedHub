from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/education")
def education():
    return render_template("education.html")

@app.route("/sgpa")
def sgpa():
    return render_template("sgpa.html")

@app.route("/cgpa")
def cgpa():
    return render_template("cgpa.html")


@app.route("/cgpa/2022")
def cgpa_2022():
    return render_template("cgpa_2022.html")

@app.route("/percentage")
def percentage():
    return render_template("percentage.html")

@app.route("/attendance")
def attendance():
    return render_template("attendance.html")

@app.route("/study-planner")
def study_planner():
    return render_template("study_planner.html")

@app.route("/scholarships")
def scholarships():
    return render_template("scholarships.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)