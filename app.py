## app.py
from flask import Flask, render_template, request, redirect, url_for
from controller import run_command
from config import COMMANDS

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", commands=COMMANDS.keys())

@app.route("/run/<command>")
def run(command):
    if command in COMMANDS:
        output = run_command(COMMANDS[command])
    else:
        output = "Invalid command."
    return f"<pre>{output}</pre><br><a href='/'>Back</a>"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)