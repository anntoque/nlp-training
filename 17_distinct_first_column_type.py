import pandas as pd

table = pd.read_table("./hightemp.txt",header=None)
print(table[0].unique())