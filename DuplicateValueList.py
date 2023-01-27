#create a list with duplicate values and make it unique

# LIST - mutable, ordered, allow duplicates, can have hetrogeneous data



#using set()

myList = ['amar', 54, 'raj', 34, 21, 'amar', 21]

myset = set(myList)

print(myset)

#using numpy

import numpy as N

myList = ['amar', 54, 'raj', 34, 21, 'amar', 21]

result = N.array(myList)
unique = N.unique(result)

print("\n",unique)
