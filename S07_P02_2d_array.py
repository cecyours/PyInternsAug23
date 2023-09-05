""" 
8 7 6
6 2 9
4 8 7
 """

#  x = a[2][1]

import numpy

x = numpy.array(
                [[1, 4, 6], 
                 [2, 5, 8], 
                 [3, 5, 9], 
                 [4, 5, 7], 
                 [5, 5, 8], 
                 [6, 5, 8], 
                 [7, 8, 1]])


x = numpy.arange(20).reshape(2,2,5)
y = x

print(y)
# print(y.ndim)
print(y[1][1][3])

# 

