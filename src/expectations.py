import numpy as np
from plotnine import ggplot, aes, geom_line
import pandas as pd

L = 250
x = np.linspace(0, L, 1000)
y1 = -np.cos(2 * np.pi * x / L) + 1
y2 = -2 * np.cos(2 * np.pi * x / L) + 2

df = pd.DataFrame({"$x$ [mm]": x, "y1": y1, "y2": y2})
df = df.melt(
    id_vars="$x$ [mm]",
    value_vars=["y1", "y2"],
    var_name="line",
    value_name="$\\sigma$ [MPa]",
)

m = {
    "y1": "0",
    "y2": "100",
}
df["$y=$"] = df["line"].map(m)

g = ggplot(df, aes(x="$x$ [mm]", y="$\\sigma$ [MPa]", color="$y=$")) + geom_line()
g.save("expectations.png")
