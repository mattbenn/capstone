#!/usr/bin/env python
# coding: utf-8

# In[ ]:
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def cprint(text: str, color: str = 'yellow'):
  """Uses a few basic colors to print messages/warnings to the console."""
  lookup_dict = {'black': 30, 'red': 31, 'green': 32, 'yellow': 33, 'blue': 34, 'magenta': 35, 'cyan': 36, 'white': 37,
                 'bred': 91, 'bgreen':92, 'byellow': 93, 'bblue': 94, 'bmagenta': 95, 'bcyan': 96, 'bwhite': 97}
  if color not in lookup_dict.keys():
    message = "Color not in code. Possible values: " + str(list(lookup_dict.keys()))
    cprint(text = message, color = '31')
    return
  print("\033[{}m{}\033[00m".format(lookup_dict[color], text))
  return

def plotColumnCounts(df, column_list, number_graphs_per_row = None, outlier_mask = False, stitle = None, dropna = True, auto_show = True):
    if number_graphs_per_row is None:
        number_graphs_per_row = len(column_list)
    df = df[column_list] # Reduce df to only column list
    nCols = number_graphs_per_row
    nRows = int(np.ceil(len(column_list)/number_graphs_per_row))
    plt.figure(figsize = (4 * nCols, 5.5 * nRows), dpi = 80, facecolor = 'w', edgecolor = 'k')
    if stitle is not None:
        plt.suptitle(stitle)
    ax_count = 1
    for column in column_list:
        plt.subplot(nRows, nCols, ax_count)
        ax_count += 1
        if not pd.api.types.is_numeric_dtype(df[column]):
            toPlot = df[column].value_counts(dropna = dropna)
            if(toPlot.shape[0] > 20):
                toPlot = toPlot.iloc[:19]
            toPlot.plot.bar()
        else:
            toPlot = df[column]
            if outlier_mask:
                temp_outlier_high = toPlot.mean() + 3*toPlot.std()
                temp_outlier_low = toPlot.mean() - 3*toPlot.std()
                toPlot = toPlot[(toPlot > temp_outlier_low) & (toPlot < temp_outlier_high)]
            plt.hist(toPlot)
            #plt.plot(df[column], kind = 'hist')
        plt.ylabel('counts')
        plt.xticks(rotation = 90)
        plt.title(f'{column}')
    plt.tight_layout()
    if auto_show:
        plt.show()

def trim_feature(series, threshold = .01):
    counts_ = series.value_counts(normalize = True)
    keep_values = counts_.index[counts_ >= threshold]
    series = series.apply(lambda x: x if x in keep_values else np.nan)
    return series

def convert_range_to_avg(range_str):
    lower, upper = map(int, range_str.split(' - '))
    return (lower + upper)/2

from IPython.core.display import HTML
def load_custom_css():
    css = """
    <style>
    .bold-underline {
        font-weight: bold;
        text-decoration: underline;
        color: Green;
    }
    </style>
    """
    return HTML(css)