import numpy as np


# todo method 1
arr1 = np.array([1,2,3,4,5])
print(arr1)
print(type(arr1))

arr2 = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr2)

# todo method 2
arr3 = np.zeros((2,3))
print(arr3)
arr4 = np.ones((3,4))
print(arr4)

# todo method 3
arr5 = np.identity(5)
print(arr5)

# todo method 4
arr6 = np.arange(10)
print(arr6)

# todo method 5
arr7 = np.linspace(1,10,20)
print(arr7)

# todo method 6
arr8 = arr7.copy()
print(arr8)
