# Create series

import pandas as pd
list_series = [1, 7, 2]
series = pd.Series(list_series)

print("Series :", series)

print("First value of series", series[0])


# Create Labels

labels_series = [1, 7, 2]
labels = pd.Series(labels_series, index=["a", "b", "c"])

print("Labels :", labels)

print("First value of series with user-defined labels : ", labels[0])


