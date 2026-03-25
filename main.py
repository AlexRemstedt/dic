"""dic - Digital Image Correlation
Author: A.W.J Remstedt
Date: 25/03/2026
Course: MT2464 - Mechanics of Maritime Constructions

This script is the main script used for performing calculations and
creating graphs in support of the report on the assignments for the
DIC lab for the course of MT2464 at the TU Delft.

Notes:
    The data are csv files with tabs as separators, and has a head
    of 3 lines.
"""

from plotters import plot_stress
from src.strain import read_strain_data
from src.stress import add_stress
import pandas as pd


def main() -> None:
    df = pd.concat(
        [
            read_strain_data(strain_line_number=1),
            read_strain_data(strain_line_number=2),
        ],
        ignore_index=True,
    )
    add_stress(df)
    plot_stress(df)


if __name__ == "__main__":
    main()
