import pandas as pd
from plotnine import ggplot, aes, geom_line, ggsave


def plot_strain(df: pd.DataFrame):
    """Create a plot of the strain data using ggplot."""
    p = ggplot(df, aes(x="x", y="strain", color="line")) + geom_line()
    ggsave(p, "strain.png")
