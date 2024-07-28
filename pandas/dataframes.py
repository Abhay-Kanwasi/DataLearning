import pandas as pd

data = {
    "Names" : ["Abhay", "Akash", "Babul"],
    "DOB" : ["27/12/2001", "21/12/2000", '28/12/2002']
}

df = pd.DataFrame(data)
print("Dataframe\n", df)

# locate row
print("\nlocate 0th row element\n", df.loc[0])

# can return 0 and 1 row
print("\n0th and 1st row\n", df.loc[[0, 1]])