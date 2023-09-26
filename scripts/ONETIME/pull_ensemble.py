#!/usr/bin/env python3
#

"""
GENERATE BLOCK-ASSIGNMENT FILES FROM AN R ENSEMBLE

- https://arxiv.org/abs/2206.10763 | https://arxiv.org/pdf/2206.10763.pdf
- https://dataverse.harvard.edu/file.xhtml?fileId=6392711&version=14.0
- https://stackoverflow.com/questions/40996175/loading-a-rds-file-in-pandas

"""

import os
import pyreadr

from pg import *

xx: str = "NC"

data_dir: str = "/Users/alecramsay/local"
rds_file: str = f"{xx}_cd_2020_plans.rds"

#

result = pyreadr.read_r(os.path.join(data_dir, rds_file))  # also works for RData

# done!
# result is a dictionary where keys are the name of objects and the values python
# objects. In the case of Rds there is only one object with None as key
df = result[None]  # extract the pandas data frame

#

cols: list = list(df)
print(cols)

nrows: int = df.shape[0]
print(nrows)

data = df.reset_index().values.tolist()

pass

pass

### END ###
