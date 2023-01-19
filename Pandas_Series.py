"""
Installing pandas is basically "pip install pandas" in the powershell
pandas full form is  PANnel Data System
Pandas is made on Numpy
Data structures refer to a specialised way to store data so as to apply a specific type of functionality on them
Once you have created a series, you can't change the amount of values that exist, however you can change the values in them
In other words, Series are Value muatble, but Size immutable
d type can be int64, float64, object (self explanatory)
"""

# Creating Series
import pandas as pd
x1 = pd.Series([1,2,3,4])
print(x1)
# You can assign indexes too
x2 = pd.Series([2,3,4,5], index = [2,3,4,5])
# Indexes will always have the same amount of values, any more or less will give error
# Duplicate indexes will also work
print(x2)
# You can create an empty series with pd.Series()

# You can also create series using NumPy arrays
import numpy as np
import pandas as pd
x3 = np.array(['a','b','c'])
x4 = pd.Series(x3, index=["Jan", "Feb", "March"])
print(x4)

# You can create Series using a Dictionary too, where the keys become the indexes
import pandas as pd
x5 = {"a": "January", "b" : "February", "c" : "March"}
x6 = pd.Series(x5)
print(x6)

# You can Access elements in a Series too
import pandas as pd
x7 = {"a": "January", "b" : "February", "c" : "March"}
x8 = pd.Series(x7)
print(x8["a"]) # Output is Jaunary
x9 = pd.Series([1,2,3,4,5,6,7,8,9])
print(x9[2])
# Slicing works similar to lists in series
# Lower limit is included, upper limit is excluded for integers
# Both limits are included for objects
print(x8['a':'b'])
print(x9[-5:-2])
print(x9[::-1])



# Attributes of Series
# **Note : You don't need parentheses for Attributes to work, since they are literally attributes, not functions / methods

import pandas as pd
import numpy as np
dict={'India':'New Delhi','USA':'WDC','UK':'London','France':'Paris'}
x10 = pd.Series(dict)
x11 = pd.Series([1,2,3,4,5,6,7,8,9])
x12 = pd.Series([10,20,30,40,50,60,70,80,90])

# Index gives us the index of the Series
print(x10.index)

# Index Name gives a heading to the index column
x10.index.name = "Country"
print(x10)

# Index Value gives us the Values of the Series as an ndarray (type of List)
print(x10.values)

# dtype gives us the datatype of Series
print(x11.dtype)

# Shape gives us the number of rows and columns as a tuple 
# ** Note: For series, it will give us the value in the form of (x,) because series is one dimensional
print(x10.shape)

# nbytes gives us the number of bytes taken up in memory by the Series in the form of bytes
print(x11.nbytes)

# ndim gives us the dimensions of the table (1 dimensional for series, 2 dimensional for DataFrame etc)
print(x10.ndim)

# size gives us the number of elements in the Series in the form of an integer
print(x11.size)

# hasnans check for NaN values and returns True/False
print(x11.hasnans)

# empty returns Boolean True if the series is empty
emp = pd.Series()
print(emp.empty)
print(x10.empty)

# name assigns name to the WHOLE SERIES, shown at the end of the series, beside the dtype
x10.name = "Capitals"
print(x10)


# You can modify the values in a series using the following syntax
# For values
x10["India"] = "Mumbai"
print(x10)
# For indexes
x10.index=['Maharashtra','USA','UK','France']
print(x10)




# Methods of Series
# **Note : You need parenthesis for methods to work, since they are functions on series

# head() gives us the first values of a Series (5 by default)
print(x11.head())

# tail() gives us the last values of a Series (5 by default)
print(x11.tail())

# count() gives us the count of the total number of values in a Series in the form of an int
print(x10.count())
print(x11.count())

# Operations on Series

# Vector operations on Series
print(x11 + 2)
print(x11 - 2)
print(x11 * 2)
print(x11 / 2)
print(x11 ** 2)
print(x11 < 5)
print(x11 > 5)

# Arithmetic operations on Series
# **Note : It is not mandatory to have the same number of elements in two series to perform all the given operations except comparisons
print(x11 + x12)
print(x11 - x12)
print(x11 * x12)
print(x11 / x12)
print(x11 ** x12)
print(x11 > x12)
print(x11 < x12)

