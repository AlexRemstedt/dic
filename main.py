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

import pandas as pd
from pathlib import Path
from src.plotters.strain_plotter import plot_strain

DATA_DIR = Path("./data/")


def read_strain_data(*, strain_line_number: int) -> pd.DataFrame:
    """Read the strain data from the csv file.

    Parameters:
        strain_line_number (int): The identifier of the strainline to read.

    Returns:
        DataFrame with columns: x, strain, uncertainty, line.
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


def strain() -> None:
    df = pd.concat(
        [
            read_strain_data(strain_line_number=1),
            read_strain_data(strain_line_number=2),
        ],
        ignore_index=True,
    )
    plot_strain(df)


if __name__ == "__main__":
    strain()
