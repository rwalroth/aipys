# -*- coding: utf-8 -*-
"""
@author: walroth
"""

# Standard library imports

# Other imports
import numpy as np
import pandas as pd
from scipy.spatial import KDTree

# This module imports
from ..consts import atomic_radii

# COV_RADII = atomic_radii['covalent_single']


def rotate_point_x(xyz, theta, radians=False):
    """
    Rotates a 3D vector by the angle theta about the x axis
    Args:
        xyz: x, y, z tupple or array
        theta: float, angle in degrees unless radians is True
        radians: bool, if true then theta is treated as radians
    Returns:
        a, b, c: rotated coordinates
    """
    if not radians:
        theta = np.radians(theta)
    cost = np.cos(theta)
    sint = np.sin(theta)
    Rx = np.array([[1.0, 0.0, 0.0],
                   [0.0, cost, sint],
                   [0.0, -sint, cost]])
    return np.matmul(xyz, Rx)


def rotate_point_y(xyz, theta, radians=False):
    """
    Rotates a 3D vector by the angle theta about the y axis
    Args:
        xyz: x, y, z tupple or array
        theta: float, angle in degrees unless radians is True
        radians: bool, if true then theta is treated as radians
    Returns:
        a, b, c: rotated coordinates
    """
    if not radians:
        theta = np.radians(theta)
    cost = np.cos(theta)
    sint = np.sin(theta)
    Ry = np.array([[cost, 0.0, -sint],
                   [0.0, 1.0, 0.0],
                   [sint, 0.0, cost]])
    return np.matmul(xyz, Ry)


def rotate_point_z(xyz, theta, radians=False):
    """
    Rotates a 3D vector by the angle theta about the z axis
    Args:
        xyz: x, y, z tupple or array
        theta: float, angle in degrees unless radians is True
        radians: bool, if true then theta is treated as radians
    Returns:
        a, b, c: rotated coordinates
    """
    if not radians:
        theta = np.radians(theta)
    cost = np.cos(theta)
    sint = np.sin(theta)
    Rz = np.array([[cost, sint, 0.0],
                   [-sint, cost, 0.0],
                   [0.0, 0.0, 1.0]])
    return np.matmul(xyz, Rz)


def coord_number(i, xyz, tree=None, radius="covalent_single"):
    RADII = atomic_radii[radius]
    if tree is None:
        tree = KDTree(xyz[['x', 'y', 'z']])
    dists, ids = tree.query(tree.data[i], k=10, p=2)
    finites = np.isfinite(dists)
    dists = dists[finites]
    ids = ids[finites]
    radii = pd.DataFrame({'radii':RADII[xyz.iloc[ids]['Z']]})
    cn = (radii.iloc[0]['radii'] + radii >= dists.reshape(-1,1)).sum() - 1
    return cn.iloc[0]


def get_info(xyz, charge_dict):
    out = {}
    formula = dict(xyz.groupby('Z').count()['x'])
    out['total charge'] = sum([val*charge_dict[key] for key, val in formula.items()])
    out['chemical formula'] = formula
    return out