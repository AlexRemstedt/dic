import pandas as pd

YOUNGS_MODULUS = 210e9  # Pa


def add_stress(strain_df: pd.DataFrame) -> None:
    """Add a column to the strain DataFrame with the stress data."""
    strain_df["stress"] = strain_df["strain"] * YOUNGS_MODULUS
