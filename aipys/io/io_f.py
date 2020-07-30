# -*- coding: utf-8 -*-
"""
@author: walroth
"""

# Standard library imports

# Other imports
import pandas as pd

# This module imports


def read_xyz(file_path):
    out_dict = {}
    with open(file_path, 'r') as f:
        i = 0
        for line in f:
            if len(line.split()) == 4:
                out_dict[i] = line.split()
                for j in range(1,4):
                    out_dict[i][j] = float(out_dict[i][j])
                i += 1
        return pd.DataFrame.from_dict(out_dict, orient='index', columns=['Z', 'x', 'y', 'z'])


def write_xyz(xyz, file, header=True):
    if header:
        file.write(str(xyz.shape[0]) + '\n')
        file.write('\n')
    for i in xyz.index:
        file.write(' '.join([str(x) for x in xyz.loc[i]]) + '\n')


def write_pc(xyz, file, charge_dict, header=True):
    if header:
        file.write(str(xyz.shape[0]) + '\n')
        file.write('\n')
    for i in xyz.index:
        line = [str(x) for x in xyz.loc[i]]
        line[0] = str(charge_dict[line[0]])
        file.write(' '.join(line) + '\n')


def write_ecp(xyz, file, charge_dict, header=True):
    if header:
        file.write(str(xyz.shape[0]) + '\n')
        file.write('\n')
    for i in xyz.index:
        line = [str(x) for x in xyz.loc[i]]
        line.insert(1, str(charge_dict[line[0]]))
        line[0] += '>'
        line.append('NewECP "SDD" end')
        file.write(' '.join(line) + '\n')


def write_constraints(constraints, file):
    file.write('%geom Constraints\n')
    for key, constraint in constraints.items():
        if key == 'cart':
            for i in constraint:
                file.write(f'    {{C {i} C}}\n')
        elif key == 'cart_range':
            for i, j in constraint:
                file.write(f'    {{C {i}:{j} C}}\n')
    file.write('    end\nend')