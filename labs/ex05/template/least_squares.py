# -*- coding: utf-8 -*-
"""Exercise 3.

Least Square
"""

import numpy as np


def least_squares(y, tx):
    """calculate the least squares."""
    w = np.linalg.solve(tx.T.dot(tx), tx.T.dot(y))
    return w
