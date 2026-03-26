"""Stress points
Author: A.W.J Remstedt

This script contains the code for finding the stresses and mohr
circles for the different points in the specimen.
"""

import numpy as np

strains = {
    1: np.array([0.0780638, -0.000109094, 0.167676]) / 1000,
    2: np.array([-0.0320553, -0.0506244, 0.0858915]) / 1000,
    3: np.array([0.0477689, 0.0937671, 0.195837]) / 1000,
}

E = 210e9  # Pa
v = 0.3

factor: float = E / (1 + v) / (1 - 2 * v)
matrix = np.array(
    [
        [1 - v, v, 0],
        [v, 1 - v, 0],
        [0, 0, (1 - 2 * v) / 2],
    ]
)


def print_matrix_form(matrix: np.ndarray) -> None:
    """Print the matrix in a nice format."""
    print(f"""
{matrix[0]:.2f} & {matrix[1]:.2f} \\\\
{matrix[1]:.2f} & {matrix[2]:.2f} 
          """)


for i, strain in strains.items():
    print(strain)
    stress = factor * matrix @ strain / 1e6
    print_matrix_form(stress)
