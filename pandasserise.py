# A Pandas series is like a column in a table . it is 1D array which holds data of any type
# here we will create a simple pandas serise.
import pandas as pd
shared =[1,5,3,10,7]
sharednew=pd.Series(shared)
print(sharednew)
# labeling - label can be use to access a specified value.
print(sharednew[0]) # 1 value

# with create label you can create
sharednew1=pd.Series(shared,index=['a','b','c','d','e'])
print("create label", sharednew1['d'])

# you can also use akey or value object like a dictionary, when creating a series.
# Here we will create a simple pandas series from a dictionalrty

shared2=pd.Series({'a':1,'b':2,'c':3,'d':4,'e':5})
sharednew2=pd.Series(shared2,index=['e'])
print("Create a serise from a dictionary",sharednew2,)

# NO-TE : aita Colum are moto kaj kore data colum akare sajai.