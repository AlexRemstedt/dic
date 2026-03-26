import pandas as pd
import numpy as np
from plotnine import ggplot, aes, geom_line, ggsave, geom_hline


def plot_strain(df: pd.DataFrame):
    """Create a plot of the strain data using ggplot."""
    p = ggplot(df, aes(x="x", y="Strain/%", color="line")) + geom_line()
    ggsave(p, "strain.png")


def plot_stress(df: pd.DataFrame):
    """Create a plot of the stress data using ggplot."""
    avg = np.mean(df["Stress/GPa"])
    max = np.max(df["Stress/GPa"])
    p = ggplot(df, aes(x="x", y="Stress/GPa")) + geom_line()
    ggsave(p, "stress.png")
