import pandas as pd
import os

color_dict = {
    'C':  [0.0, 0.0, 0.0],
    'O':  [1.0, 0.0, 0.0],
    'N':  [0.0, 0.0, 1.0],
    'Si': [0.3, 0.3, 0.3],
    'Fe': [0.8, 0.2, 0.2],
    'Mg': [0.3, 0.6, 0.3],
    'Ti': [0.9, 0.9, 0.9]
}

atomic_radii = pd.read_csv(
    os.path.join(
        os.path.abspath(os.path.dirname(__file__)), 'atomic_radii.csv'
    ),
    index_col='symbol'
)
