# Write a Pandas program to create and display a one-dimensional array-like object containing an array of data using Pandas module.

import pandas as pd

data = {
        "firstname" : "Abhay",
        "lastname" : "Kanwasi",
        "roll_no" : "1",
        "branch" : "Computer Science and Engineering"
    }

ds = pd.Series(data)
print(ds)
