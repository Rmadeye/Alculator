import pandas as pd
import os

class Calculations:


    def __init__(self):
        pass

    def calc_dil(self, volume: float, final: float, solution: float):

        file_path = os.getcwd() + '\\src\\density.csv'
        file = open(file_path, 'r')

        data = pd.read_csv(file, sep = ';', index_col=0, squeeze=True).to_dict()
        print(data)
        df = pd.read_csv(str(os.getcwd()+'\\density.csv'), sep = ';')
        init_density = df.loc[df['Percentage']==str(solution)]
        init_density_output = init_density['density']
        final_density = df.loc[df['Percentage']==str(final)]
        answer = ((volume*solution*init_density_output)-(volume*final*final_density))/(final*final_density)
        pure = volume*(solution/100)*init_density_output
        print(answer,pure)
        return str(answer,pure)

        