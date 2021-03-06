import pandas as pd
import os, csv, webapp.app

class Calculations:


    def __init__(self):
        pass

    def calc_dil(self, volume: float, final: float, solution: float):
        path = webapp.app.AbsPath()
        print(path.main_cwd())

        data = []
        with open(path.main_cwd() + '/webapp/src/density.csv', 'r', encoding='utf-8') as file:
            readCSV = csv.reader(file, delimiter=';')

            for row in readCSV:
                data.append(row)
        df = pd.DataFrame(data[1:], columns=data[0][0:2])
        data = df.set_index('percent')['density'].to_dict()
        initial_density = data[str(int(solution))]
        final_density = data[str(int(final))]

        print(initial_density)

        answer = ((float(volume)*float(solution)*float(initial_density))-(volume*float(final)*float(final_density)))/(final*float(final_density))
        pure = volume*(float(solution)/100)*float(initial_density)
        return str(int(answer)), str(round(pure,2))
