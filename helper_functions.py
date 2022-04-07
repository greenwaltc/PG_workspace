import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

np.set_printoptions(suppress=True)

data_directory = './data/Feb2022/' # The root directory for where all the data files are stored
overall_filename = 'february_data.csv' # Filename where the concatenated individual files will be stored

# Helper functions. They do what the function name suggests
def read_in_file(filename, keep_columns=None, time_format='%Y-%m-%dT%H:%M:%S.%f'):
    '''Reads in a .csv file into a Pandas DataFrame. 
    
    This function assumes there is a column in the .csv whose name is 'time'. The 'time' column is automatically set as a
    Pandas DatetimeIndex.

    Args:
        filename : str
            The name of the file to be read from, in .csv format.
        keep_columns : list str
            The names of the columns to keep from the file. If None, all columns will be kept.
        time_format: str
            The datetime format for which to parse the 'time' column from the .csv file. 

    Returns:
        A Pandas DataFrame.
    '''
    df = pd.read_csv(filename, usecols=keep_columns)

    if 'time' in df.columns.tolist():
        df.time = pd.to_datetime(df.time, format=time_format)
        df = df.set_index('time')

    return df

def groupby_second(df, agg='mean'):
    '''Groups a Pandas DataFrame by second according to the aggregation method agg.

    Args:
        df: Pandas DataFrame
            A Pandas DataFrame whose index is a DatetimeIndex. The index needs to be of this type to perform the groupby.
        agg: str
            The aggregation method for the groupby operation. Default is 'mean'.

    Returns:
        The resulting Pandas DataFrame.
    '''
    df = df.groupby(by=[df.index.year, df.index.month, df.index.day, df.index.hour, df.index.minute, df.index.second]).agg(agg)
    df.index = pd.to_datetime(df.index.get_level_values(0).astype(str) + '-' +
                df.index.get_level_values(1).astype(str) + '-' +
                df.index.get_level_values(2).astype(str) + 'T' +
                df.index.get_level_values(3).astype(str) + ':' +
                df.index.get_level_values(4).astype(str) + ':' +
                df.index.get_level_values(5).astype(str),
                format='%Y-%m-%dT%H:%M:%S')
    return df

def plot_time_window(df, t1, t2, col, title=None, figsize=(18,5), fontsize=14,
                    save_fig=False, fname=None):
    '''Plots one column of a DataFrame in a certain time window.
    
    Args:
        df: Pandas DataFrame
            The DataFrame with the data to be plotted.
        t1: Datetime
            The opening of the time interval (inclusive).
        t2: Datetime
            The end of the time interval (exclusive).
        col: str
            The column of df to plot.'''
            
    df = df[(df.index >= t1) & (df.index < t2)]

    fig, axs = plt.subplots(1, sharex=True, sharey=False, gridspec_kw={'hspace': 0}, figsize=figsize)

    sns.lineplot(x=df.index, y=df[col], ax=axs, fontsize=fontsize)
    
    plt.rcParams.update({'font.size': fontsize})
    if title is not None:
        plt.title(title, fontsize=fontsize)

    if save_fig:
        plt.tight_layout()
        plt.savefig(fname, dpi=300)
        
    plt.show()