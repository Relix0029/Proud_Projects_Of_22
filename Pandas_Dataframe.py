"""
Dataframes are 2 dimensional Data structures. They are both size and value mutable
This means that you can change both the values and the indexes in DataFrames
"""

# # Creating a DataFrame : 

# # Using List of Dictionaries
# import pandas as pd
# listdict = [{"A" : 10 , "B" : 5}, {"A" : 5 , "B" : 10 ,"C" : 20 }]
# df = pd.DataFrame(listdict)
# print(df)

# # Using NumPy ndarrays
# import pandas as pd
# import numpy as np
# array1 = np.array([10,20,30])
# array2 = np.array([100,200,300])
# array3 = np.array([-10,-20,-30,-40])
# df = pd.DataFrame(array1)
# print(df)
# # You can add all of the arrays too in the form of a list(either variable passed through, or explicitly) 
# # and you can specify the index too
# # By default, it's usually given to be indexed using integers starting from 0
# df = pd.DataFrame([array1 , array2 , array3], index = ["Student A" , "Stuednt B" , "Student C "])
# print(df)

# # Creation of DataFrame form Series
# import pandas as pd
# seriesA = pd.Series([1,2,3,4,5], index = ["a", "b", "c","d","e"])
# seriesB = pd.Series([1000,2000,-1000,-5000,1000], index = ["a", "b", "c","d","e"])
# seriesC = pd.Series([10,20,-10,-50,100], index = ["z", "y", "a", "c", "e"])
# # We simply pass through the required series in the form of a list
# # where, the elements of the list would be the series itself
# df = pd.DataFrame([seriesA, seriesB, seriesC])
# print(df)

# As with all things, you can always nest different types of data series, for example, here we've nested a dictionary with keys as names, and values as a Pandas Series, where the index in the series shows us the respective subject for which we have the marks taken. It's important to note that in a dictionary, the keys are always taken as the headings, so the value headers are taken as the indexes by default.
import pandas as pd
ResultSheet={'Arnab': pd.Series([90, 91, 97],  index=['Maths','Science','Hindi']),'Ramit': pd.Series([92, 81, 96],  index=['Maths','Science','Hindi']),'Samridhi': pd.Series([89, 91, 88],  index=['Maths','Science','Hindi']),'Riya': pd.Series([81, 71, 67],  index=['Maths','Science','Hindi']),'Mallika': pd.Series([94, 95, 99],  index=['Maths','Science','Hindi'])}
Result_df = pd.DataFrame(ResultSheet)
print(Result_df)

# We can use the .drop() method to delete specific rows and columns from a DataFrame
print(Result_df)
print("To delete the Science row")
