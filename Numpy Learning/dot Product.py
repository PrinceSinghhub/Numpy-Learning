from numpy import *


arr1 = arange(6).reshape(2,3)
print(arr1)
arr2 = arange(6,12).reshape(3,2)
print(arr2)
print(arr1.dot(arr2))