# Iniciando proyecto
# from flask import Flask

from flask import Flask, render_template
from flask import request, redirect,url_for,Blueprint

app = Flask(__name__)
@app.route("/")
def home():
    return render_template("666inti.html")

if __name__ == "__main__":
    app.run(debug=True)