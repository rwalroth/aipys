# -*- coding: utf-8 -*-
"""
@author: walroth
"""

# Standard library imports

# Other imports
from matplotlib import pyplot as plt

# This module imports
from aipys.consts import color_dict

# constants


COLOR_DICT = color_dict


def plot_xyz(df, fig=None, loc=111, **kwargs):
    if fig is None:
        fig = plt.figure()
    if type(loc) in (int, str):
        ax = fig.add_subplot(loc, projection='3d', **kwargs)
    else:
        ax = fig.add_subplot(loc[0], loc[1], loc[2], projection='3d', **kwargs)

    ax.scatter(df['x'], df['y'], df['z'], c=[COLOR_DICT[key] for key in df['Z']])
    
    return ax


def plot_regs(qm, pc, ecp):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d', proj_type = 'ortho')
    
    ax.scatter(qm['x'], qm['y'], qm['z'], c='r')
    ax.scatter(ecp['x'], ecp['y'], ecp['z'], c='b')
    ax.scatter(pc['x'], pc['y'], pc['z'], c='gray')
    
    return fig, ax


def plot_regs_2d(qm, pc, ecp):
    for a, b, c in [['x', 'y', 'z'], ['x', 'z', 'y'], ['y', 'z', 'x']]:
        low = qm[c].min()
        high = qm[c].max()
        plt.figure(figsize=(10,10))
        plt.scatter(qm[a], qm[b], c='r')
        plt.scatter(pc[(pc[c] > low) & (pc[c] < high)][a], pc[(pc[c] > low) & (pc[c] < high)][b], c='gray')
        plt.scatter(ecp[(ecp[c] > low) & (ecp[c] < high)][a], ecp[(ecp[c] > low) & (ecp[c] < high)][b], c='b')
        plt.xlabel(a)
        plt.ylabel(b)
        plt.show()
 