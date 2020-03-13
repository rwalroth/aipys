# -*- coding: utf-8 -*-
"""
@author: walroth
"""

# Standard library imports

# Other imports
import pandas as pd
import numpy as np

# This module imports


def get_box(xyz, x, y, z):
    box = (
        (xyz['x'] > -x/2) & (xyz['x'] < x/2) &
        (xyz['y'] > -y/2) & (xyz['y'] < y/2) &
        (xyz['z'] > -z/2) & (xyz['z'] < z/2)
    )
    return box


def get_regs(xyz, box=[10, 10, 20], border=[2,2,2]):
    inner = get_box(xyz, *box)
    outer = get_box(xyz, *[2*x + box[i] for i, x in enumerate(border)])
    
    qm = xyz[inner]
    pc = xyz[~outer]
    ecp = xyz[~inner & outer]
    
    return qm, pc, ecp


def get_cylinder(xyz, radius, height):
    dist = np.sqrt(xyz['x']**2 + xyz['y']**2)
    box = (
        (dist < radius) &
        (xyz['z'] > -height/2) & (xyz['z'] < height/2)
    )
    return box


def get_regs_cylinder(xyz, radius=5, height=20, border=2):
    inner = get_cylinder(xyz, radius, height)
    outer = get_cylinder(xyz, radius + border, height + 2*border)
    
    qm = xyz[inner]
    pc = xyz[~outer]
    ecp = xyz[~inner & outer]
    
    return qm, pc, ecp


def get_info(xyz, charge_dict):
    out = {}
    formula = dict(xyz.groupby('Z').count()['x'])
    out['total charge'] = sum([val*charge_dict[key] for key, val in formula.items()])
    out['chemical formula'] = formula
    return out