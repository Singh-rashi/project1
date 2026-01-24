from flask import Flask, render_template, request
from analyzer.complexity import estimate_complexity

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    complexity = None
    if request.method == "POST":
        code = request.form["code"]
        complexity = estimate_complexity(code)
    return render_template("index.html", complexity=complexity)

if __name__ == "__main__":
    app.run(debug=True)
