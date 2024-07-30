# Write a Pandas program to convert a Panda module Series to Python list and it's type.

import pandas as pd

ds = pd.Series([2,4,6,8])
print(type(ds))
ds = ds.tolist()
print(type(ds))
