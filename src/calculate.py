import pandas as pd
import os

class Calculations:
    def __init__(self):
        pass

    def calc_dil(self, volume: float, final: float, solution: float):
        print(os.getcwd())
        df = pd.read_csv(str(os.getcwd()+'\\density.csv'), sep = ';')
        init_density = df.loc[df['Percentage']==str(solution)]
        init_density_output = init_density['density']
        final_density = df.loc[df['Percentage']==str(final)]
        answer = ((volume*solution*init_density_output)-(volume*final*final_density))/(final*final_density)
        pure = volume*(solution/100)*init_density_output
        print(answer,pure)
        return str(answer,pure)

        