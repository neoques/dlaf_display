import holoviews as hv
import hvplot.dask  # noqa: adds hvplot method to dask objects
import pandas as pd
import datashader.transfer_functions as tf
import datashader as ds
import matplotlib.pyplot as plt
import holoviews.operation.datashader as hd
import numpy as np
from datashader.mpl_ext import dsshow, alpha_colormap

hd.shade.cmap=["lightblue", "darkblue"]

hv.extension("bokeh", "matplotlib")
hv.output(backend="matplotlib")

if __name__ == '__main__':
    df = pd.read_csv('C:\\users\\Russell\\output.csv')
    df.columns = ["id", "parent_id", "x", "y", "z"]

    dsshow(df,
           ds.Point('x', 'y'),
           norm='eq_hist',
           cmap="inferno_r");
    plt.show()