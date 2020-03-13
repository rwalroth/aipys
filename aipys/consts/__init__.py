import pandas as pd

color_dict = {
    'C': [0,0,0],
    'O': [1,0,0],
    'N': [0,0,1],
    'Si': [0.3,0.3,0.3],
}

atomic_radii = pd.read_csv('atomic_radii.csv', index_col='symbol')/100