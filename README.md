# Matplotlib colormaps for Ansys

Small python script to generate colormaps compatible with Ansys APDL based on the colormaps defined in matplotib.

The currently generated colormaps are:

* viridis
* inferno
* plasma
* magma
* cividis

To generate additional colormaps edit the list of colormaps in the script.

## Usage

To use any of these colormaps copy them to your working directory and run the following command:

```
/cmap,viridis,cmap
```

The colormap will be loaded and used for all further plots.
