import pandas as pd
import os

color_dict = {
    'C': [0,0,0],
    'O': [1,0,0],
    'N': [0,0,1],
    'Si': [0.3,0.3,0.3],
}

atomic_radii = pd.read_csv(
    os.path.join(
        os.path.abspath(os.path.dirname(__file__)), 'atomic_radii.csv'
    ),
    index_col='symbol'
)
