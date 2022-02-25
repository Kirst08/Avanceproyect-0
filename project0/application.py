from flask import Flask, request, render_template

app = Flask(__name__)
app.debug = True

@app.route("/", methods= ["POST","GET"])
def home():
    return render_template("introduccion.html")

@app.route("/estudios", methods= ["POST","GET"])
def Estudios():
    return render_template("estudios.html")