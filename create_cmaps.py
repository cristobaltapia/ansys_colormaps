"""
Generate colormap files compatible with Ansys APDL.

The colormaps correspond to the ones defined in matplotlib.
"""
import csv
import os

import matplotlib.cm as cm
import numpy as np


def to_ansys_color(x):
    return [int(ix * 100) for ix in x]


def ensure_dir(f):
    """look up for the directory 'f' and creates it if it doesn't exist."""
    if not os.path.exists(f):
        os.makedirs(f)


def main():

    cmaps = ["viridis", "inferno", "magma", "plasma", "cividis"]
    nums = np.linspace(0, 255, 9, dtype=int)

    ensure_dir("cmaps")

    for ci in cmaps:
        cmap_i = cm.get_cmap(ci)(nums)
        ansys_viridis = [to_ansys_color(ci) for ci in cmap_i]

        with open(f"cmaps/cmap_{ci}.cmap", "w") as f:
            # Write header
            f.write("  *** COLOR MAP CREATED FOR THE WIN32C DRIVER ***\n")
            f.write("      0   100   100   100\n")
            # Write each color (9 colors)
            for ix, ci in enumerate(ansys_viridis, start=1):
                f.write(f"{ix: >7}{ci[0]: >6}{ci[1]: >6}{ci[2]: >6}\n")

            # Write the rest of the colors
            f.write("""     10   100   100     0
     11   100    57     0
     12   100     0     0
     13    80    80    80
     14    60    60    60
     15     0     0     0\n""")


if __name__ == "__main__":
    main()
