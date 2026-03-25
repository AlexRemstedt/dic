"""Strain
Author: A.W.J Remstedt
Date: 25/03/2026
Course: MT2464 - Mechanics of Maritime Constructions

This module contains the code for reading the strain data and
plotting it.

Notes:
    The data are csv files with tabs as separators, and has a head
    of 3 lines.
"""

import pandas as pd
from pathlib import Path
from src.plotters import plot_strain

DATA_DIR = Path("./data/")


def read_strain_data(*, strain_line_number: int) -> pd.DataFrame:
    """Read the strain data from the csv file.

    Parameters:
        strain_line_number (int): The identifier of the strainline to read.

    Returns:
        DataFrame with columns: x, strain, line.
    """
    df = pd.read_csv(
        DATA_DIR / f"Line{strain_line_number}_tangential_strain_y",
        sep="\t",
        skiprows=3,
        header=None,
        names=["x", "strain", "uncertainty"],
    )
    df["line"] = f"Line{strain_line_number}"
    return df


def main() -> None:
    df = pd.concat(
        [
            read_strain_data(strain_line_number=1),
            read_strain_data(strain_line_number=2),
        ],
        ignore_index=True,
    )
    plot_strain(df)


if __name__ == "__main__":
    main()
