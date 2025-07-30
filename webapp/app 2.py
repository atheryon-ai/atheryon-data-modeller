from flask import Flask, render_template, request
from agent.tools.query_tool import search_trades_by_field

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    results = None
    if request.method == "POST":
        field = request.form.get("field")
        value = request.form.get("value")
        results = search_trades_by_field(field, value)
    return render_template("index.html", results=results)

if __name__ == "__main__":
    app.run(debug=True)