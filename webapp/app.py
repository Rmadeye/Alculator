from flask import Flask, request, render_template, send_file
from src import calculate
import os, shutil

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/calculate_dilution', methods=["POST"])
def calculate_dilution():
    calcs = calculate.Calculations()
    volume = request.form['volume']
    solution = request.form['solution']
    final = request.form['final']

    try:

        return str(calcs.calc_dil(float(volume), float(final), float(solution)))

    except TypeError:

        return render_template("type_error.html")



if __name__ == "__main__":
    app.run('127.0.0.1', 5000, debug=True)


