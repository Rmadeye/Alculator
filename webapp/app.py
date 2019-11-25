from flask import Flask, request, render_template

from webapp.src import calculate
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/calculate_dilution', methods=["POST"])
def calculate_dilution():
    calcs = calculate.Calculations()
    rootdir = AbsPath()
    volume = request.form['volume']
    solution = request.form['solution']
    final = request.form['final']
    densities = app.open_resource(rootdir.main_cwd() + '\\webapp\\src\\density.csv', 'r')

    try:

        return str(calcs.calc_dil(float(volume), float(final), float(solution)))

    except TypeError:

        return render_template("type_error.html")

class AbsPath:

    def main_cwd(self):
        return os.path.dirname(app.root_path)



if __name__ == "__main__":
    app.run('127.0.0.1', 5000, debug=True)


