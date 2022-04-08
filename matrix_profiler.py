
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import stumpy
from sklearn.preprocessing import MinMaxScaler

class MatrixProfiler():
    '''This class performs and plots the result from performing a matrix profile on a given time window of data.'''

    def __init__(self, m=3, t1=None, t2=None, normalize=True, fontsize=14, save_fig=False, fname=None, figsize=(18,10)):
        '''Constructor for the MatrixProfiler.
        
        Args:
            m: int
                Window size for the matrix profile algorithm.
            t1: Datetime
                Starting time window for analysis (inclusive).
            t2: Datetime
                Ending time window for analysis (exclusive).
            normalize: bool
                If true, normalize the data according to min-max normalization.
            fontsize: int
                Fontize for plot labels, title, etc
            savefig: bool
                If true, save the output figure to a file.
            fname: str
                The filename to store the saved figure. Ex: "test-matrix-profile.png"
            figsize: tup
                The dimensions of the output figure. (w x h)
        '''
        self.m = m
        self.t1, self.t2 = t1, t2
        self.fontsize = fontsize
        self.save_fig = save_fig
        self.fname = fname
        self.figsize = figsize
        self.normalize = normalize

    def fit(self, df):
        self.n_dim = len(df.columns)

        if self.t1 is not None \
            and self.t2 is not None \
            and self.t1 < self.t2:
            self.df = df[(df.index >= self.t1) & (df.index < self.t2)]

        if self.normalize:
            self.df.iloc[:,:] = MinMaxScaler().fit_transform(self.df.iloc[:,:])

        if self.n_dim > 1: # If you have more than one dimension
            self.do_matrix_profile_nd()
        else:
            self.do_matrix_profile_1d()

    def do_matrix_profile_1d(self):
        '''Performs an 1-dimensional matrix profile to find motifs and discords.
        
        This function will display a PyPlot figure for the matrix profile.
        
        Args:
            df: Pandas DataFrame
                A Pandas DataFrame with exactly one column. Additionally, that column of the DataFrame needs to be of type
                float. This function will not work with non-continuos datatypes present in the DataFrame.
            m: int
                The window size for the matrix profile.
                
        Returns:
            None. Only the output is displayed.
        '''
        
        self.mp = stumpy.stump(self.df.iloc[:, 0], self.m)
        self.discord_idx = np.argsort(self.mp[:, 0])[-1]

    def do_matrix_profile_nd(self, df):
        '''Performs an n-dimensional matrix profile to find motifs, where n > 1. This function will display PyPlot figures for each dimension of the matrix profile.
        
        Args:
            df: Pandas DataFrame
                A Pandas DataFrame with more than one column and whose number of columns is greater than 1. Additionally,
                each column of the DataFrame needs to be of type float. This function will not work with non-continuos
                datatypes present in the DataFrame.
            m: int
                The window size for the matrix profile.
                
        Returns:
            None. Only the output is displayed.
        '''

        self.mp, self.indices = stumpy.mstump(df, self.m)
        self.discord_idx = np.argsort(self.mp, axis=1)[:, -1]

    def display(self):
        if self.n_dim == 1:
            nrows = 2
            figsize = self.figsize
            self.fig, self.axs = plt.subplots(nrows, sharex=True, sharey=False, gridspec_kw={'hspace': 0}, figsize=figsize)
            self.display_1d()
        else:
            nrows = self.mp.shape[0] * 2
            figsize = (18,5*self.df.shape[1])
            self.fig, self.axs = plt.subplots(nrows, sharex=True, sharey=False, gridspec_kw={'hspace': 0}, figsize=figsize)
            self.display_2d()

        if self.save_fig:
            plt.tight_layout()
            plt.savefig(self.fname, dpi=300)

        plt.show()

    def display_1d(self):
        plt.suptitle('Discord (Anomaly/Novelty) Discovery - Window Size {}'.format(self.m), fontsize=self.fontsize)
        self.axs[0].plot(self.df.iloc[:, 0].values)
        self.axs[0].set_ylabel(list(self.df.columns)[0], fontsize=self.fontsize)
        self.axs[1].set_xlabel('Time', fontsize =self.fontsize)
        self.axs[1].set_ylabel('Matrix Profile', fontsize=self.fontsize)
        self.axs[1].plot(self.mp[:, 0])

        rect = Rectangle((self.discord_idx, 0), self.m, max(self.df.iloc[:, 0]), facecolor='red', alpha=.35)
        self.axs[0].add_patch(rect)
        self.axs[1].axvline(x=self.discord_idx, linestyle="dashed", color='red', alpha=0.5)

    def display_2d(self):
        for k, dim_name in enumerate(self.df.columns):
            self.axs[k].set_ylabel(dim_name, fontsize=self.fontsize)
            self.axs[k].plot(np.arange(self.df.shape[0]), self.df[dim_name])
            self.axs[k].set_xlabel('Time', fontsize =self.fontsize)

            self.axs[k + self.mp.shape[0]].set_ylabel(dim_name.replace('T', 'P'), fontsize=self.fontsize)
            self.axs[k + self.mp.shape[0]].plot(self.mp[k], c='orange')
            self.axs[k + self.mp.shape[0]].set_xlabel('Time', fontsize =self.fontsize)

            self.axs[k].axvline(x=self.discord_idx[1], linestyle="dashed", c='black')
            self.axs[k + self.mp.shape[0]].axvline(x=self.discord_idx[1], linestyle="dashed", c='black')
