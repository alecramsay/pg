#!/usr/bin/env python3
#

"""
GENERATE BLOCK-ASSIGNMENT FILES FROM AN R ENSEMBLE

- https://arxiv.org/abs/2206.10763 | https://arxiv.org/pdf/2206.10763.pdf
- https://dataverse.harvard.edu/file.xhtml?fileId=6392711&version=14.0
- https://stackoverflow.com/questions/40996175/loading-a-rds-file-in-pandas

- https://rpy2.github.io/doc/latest/html/introduction.html

"""

import os
import rpy2.robjects as robjects
from rpy2.robjects import pandas2ri

# from rpy2.robjects.conversion import localconverter

# import pyreadr

from pg import *

xx: str = "NC"

data_dir: str = "/Users/alecramsay/local"
rds_file: str = f"{xx}_cd_2020_plans.rds"
rds_path: str = os.path.join(data_dir, rds_file)

# pyreadr

"""
result = pyreadr.read_r(rds_path)  # also works for RData

# done!
# result is a dictionary where keys are the name of objects and the values python
# objects. In the case of Rds there is only one object with None as key
df = result[None]  # extract the pandas data frame
"""

# rpy2

pandas2ri.activate()
readRDS = robjects.r["readRDS"]
df = readRDS(rds_path)
# df = pandas2ri.ri2py(df)
# do something with the dataframe

#

cols: list = list(df)
print(cols)

nrows: int = df.shape[0]
print(nrows)

data = df.reset_index().values.tolist()

pass

pass

### END ###
