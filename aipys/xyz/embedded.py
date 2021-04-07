# -*- coding: utf-8 -*-
"""
@author: walroth
"""

# Standard library imports

# Other imports
import pandas as pd
import numpy as np
from scipy.spatial import KDTree

# This module imports
from .xyz_f import coord_number


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


def get_constraints(qm, ecp, kind='box', bounds=[5,5,10]):
    constrained = {}
    constrained['cart'] = []
    constrained['cart_range'] = [[qm.shape[0], qm.shape[0] + ecp.shape[0] - 1]]
    if kind == 'cylinder':
        for i in range(qm.shape[0]):
            if (np.sqrt(qm.iloc[i]['x']**2 + qm.iloc[i]['y']**2) >= bounds[0]) | (abs(qm.iloc[i]['z']) >= bounds[1]):
                constrained['cart'].append(i)
                
    elif kind == 'box':
        for i in range(qm.shape[0]):
            if (abs(qm.iloc[i]['x']) >= bounds[0]) | (abs(qm.iloc[i]['y']) >= bounds[1]) | (abs(qm.iloc[i]['z']) >= bounds[2]):
                constrained['cart'].append(i)
    
    return constrained


def clean_qm(qm, ecp, threshhold):
    qm_out = qm.copy()
    ecp_out = ecp.copy()
    qm_tree = KDTree(qm[['x', 'y', 'z']])
    for i, idx in enumerate(qm.index):
        Z = qm.loc[idx]['Z']
        cn = coord_number(i, qm, qm_tree)
        if cn < threshhold[Z]:
            ecp_out.loc[idx] = qm.loc[idx]
            qm_out.drop(idx, inplace=True)
    return qm_out, ecp_out