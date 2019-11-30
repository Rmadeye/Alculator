from flask import Flask, request, render_template

from webapp.src import calculate
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")


def check_input(volume, final, solution):

    if int(volume) > 0:
        pass
    if int(solution) > 0:
        pass
    if int(solution) < 100:
        pass
    if int(final) > 0:
        pass
    if int(final) < 100:
        pass
    else:
        return render_template("error.html")




@app.route('/calculate_dilution', methods=["POST"])
def calculate_dilution():
    calcs = calculate.Calculations()
    volume = request.form['volume']
    solution = request.form['solution']
    final = request.form['final']

    try:
        check_input(volume, final, solution)
        if float(solution) > float(final):
            output = calcs.calc_dil(float(volume), float(final), float(solution))
            answer = output[0]
            pure = output[1]
            return render_template("answer.html", answer = answer, pure = pure)
        else:
            return render_template("error.html")


    except:

        return render_template("error.html")

class AbsPath:

    def main_cwd(self):
        return os.path.dirname(app.root_path)


