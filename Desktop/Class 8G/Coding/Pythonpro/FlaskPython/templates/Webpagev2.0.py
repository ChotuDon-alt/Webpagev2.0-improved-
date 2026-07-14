from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def welcome():
    return render_template("welcome.html")
@app.route("/home")
def home():
    return render_template("home.html")
@app.route("/about")
def about():
    return render_template("about.html")
@app.route("/contact")
def contact():
    return render_template("contact.html")
@app.route("/persdet")
def persdet():
    return render_template("persdet.html")
@app.route("/follow")
def feedback():
    return render_template("follow.html")

import os
if (__name__) == "__main__":
    port = int(os.environ.get("PORT", 6200))
    app.run(host = "0.0.0.0", port=port)
