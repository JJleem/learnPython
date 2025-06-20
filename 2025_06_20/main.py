# from file import save_to_file
# from extractors.wwr import extract_wwr_jobs

# keyword = input("What do you want to search?")

# indeed = extract_indeed_jobs(keyword)
# wwr = extract_wwr_kobs(keyword)

# jobs = indeed + wwr
# save_to_file(keyword,jobs)

from flask import Flask, render_template

app = Flask("JobScrapper")

@app.route("/")
def home():
    return render_template("home.html", name="nico")

# @app.route("/hello")
# def hello():
#     return "Hello, World!"

app.run("0.0.0.0")