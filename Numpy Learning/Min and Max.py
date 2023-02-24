from numpy import *
arr1 = arange(10).reshape(2,5)
print(arr1)

arr2 = arange(10,20).reshape(2,5)
print(arr2)

# min
print(arr1.min())
print(arr2.min())

# max
print(arr1.max())
print(arr2.max())

#todo finding a max and min row coll form the matrix
# for finding min row and coll

minr = arr1.min(axis = 0)
print(minr)

minr2 = arr2.min(axis=1)
print(minr2)


# todo for finding max row and coll

minr = arr1.max(axis = 0)
print(minr)

minr2 = arr2.max(axis=1)
print(minr2)