# Getting Started

## How to set up and run the matrix profile

### Prerequisites
A configured python environment with the following libraries installed:
> pandas
> numpy
> zipfile
> tqdm
> matplotlib
> seaborn
> stumpy (this is the library for doing the matrix profile)
> datetime
> sklearn

### Step 1 - Getting the data ready

The most recent data we have is for the period of February 14 to February 28. The data is stored in individual files
representing one entire day (midnight to midnight). Because GitHub limits the size of any one file that is in a remote
repository, all the data files are stored in GitHub as compressed .zip files in the data/Feb2022/zip/ folder. When
a .zip archive in this folder is unzipped, the output is a .csv file stored in the data/Feb2022/ folder.

#### Step 1A - Clone this repo

Clone this repository into your desired workspace folder using this url: https://github.com/greenwaltc/PG_workspace.git

#### Step 1B - Switch to the correct branch

The 'submission' branch is the branch containing our final work for the Capstone. In a terminal, first make sure
your present working directory is the root directory of the cloned workspace, then enter the following command:
```
git checkout submission
```

#### Step 1C - Run the code to unzip and join all the data

The file "data_prep.ipynb" contains all the necessary code to unzip the individual data files. Additionally, this file
contains code to concatenate all the individual data files and output one complete data file "february_data.csv". Open
the file and run every cell, in order, to get all the data ready for running the matrix profile.