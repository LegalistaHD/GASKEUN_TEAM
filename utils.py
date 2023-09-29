import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def visualize_tax(df: pd.DataFrame) -> plt.Figure:

    """Visualisasi Data Harga dari Hotel-hotel di Bali"""
    x: pd.DataFrame = df.groupby('Tax')['Tax'].count()
    y: int = len(df)
    ratio = ((x/y).round(2))
    df.ratio = pd.DataFrame(ratio)

    fig, ax = plt.subplots(1, 1, figsize=(6.5, 2.5))

    ax.barh(df.ratio.index, df.ratio['Tax'], color='yellow', label='Tax')

    return fig
  