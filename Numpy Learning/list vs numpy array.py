from numpy import *
import sys

# 1 difference that is memory used
List = range(100)
size = sys.getsizeof(87) * len(List)
print(size)

numpyarry = arange(100)
size1 = numpyarry.itemsize * len(numpyarry)
print(size1)

# 2 faster
import  time
x = range(100000000)
y = range(100000000,200000000)

# add both every eleemnt of the x and y to each other
start_time = time.time()
ans = [i+j for i,j in zip(x,y)]
print(time.time()-start_time)

st = time.time()
arr_x = arange(100000000)
arr_y = arange(100000000,200000000)
ans1 = arr_x+arr_y
print(time.time()-st)





