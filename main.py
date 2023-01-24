from flask import Flask, render_template
from advice_class import GetAdvice

app = Flask(__name__)


@app.route("/")
def home_page():
    tool = GetAdvice()
    my_advice = tool.get_advice()
    return render_template("index.html", advice=my_advice)


if __name__ == "__main__":
    app.run(debug=True)
