# cleaning data: it means fixing the bad data in the dataset
# bad data could be: empty cell, data in a wrong formate, duplicate data and wrong data  
# emplty cell: it will give you wrong result always, we will have to remove the rows  always that contain the bad data.
# here we will return a new data frame with no empty cell.
import  pandas as pd
sazidul=pd.read_csv('customers-10000.csv')
sazidulnew=sazidul.dropna()
print(sazidulnew.to_string())
print("==========================")
# 
sazidulnew1=sazidul.dropna(inplace=True)
print(sazidulnew1)

# replacing the empty value : we will use the fillna() method which will allow us to replace the empty cell with a value.
