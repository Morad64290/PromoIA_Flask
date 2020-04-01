from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("home.html", message = "Je fais un test 3210")

if __name__ == "__main__":
    app.run()