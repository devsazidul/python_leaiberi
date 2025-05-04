# DataFrame : it is a 2D data structure like a 2D array with table incl. rows and columns
import pandas as pd

data = {"cal":[420,380,390],"dur":[50,40,45],"day":[1,2,3]}
sazidul=pd.DataFrame(data)
print(sazidul)
print("==========================")
print(sazidul.loc[0])
print("==========================")
print(sazidul.loc[[0,1]])


fileload=pd.read_csv('customers-10000.csv',)
print(fileload.to_string)
print("==========================")

# NO-TE: DataFrame Row akahre kaj kore sirialy