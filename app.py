from flask import Flask, render_template
import webbrowser

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/pie")
def pie():
    return render_template("pie.html")

@app.route("/bar")
def bar():
    return render_template("bar.html")

@app.route("/map")
def map():
    return render_template("map.html")

if __name__ == "__main__":
    app.run(debug=True)
