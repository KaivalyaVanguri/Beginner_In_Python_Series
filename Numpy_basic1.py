import numpy as np
a = np.array([[1,2],[2,3],[3,4]])
print(a)
print(a.shape)
print(a.ndim)
print(a.reshape(2,3))#rows x columns
print('reshape in ndim',a.reshape(2,3).ndim)
c = a.copy()
print('base',c.base)
b = np.array([1,2,3,4,5],ndmin = 5)
print(b)
print(b[0])# column 0 sum
d = b.view()
print('base',d.base)
print(b.shape) #number of elements present at every dimension
a = np.array([1,2,3,4,5,6,7,8,9,10])
print(a.reshape(5,2))
a = np.array([[1,2,3],[0,1,2],[9,0,1]])
print(a.sum(axis = 0))#row 0 sum
print(a.sum(axis = 1))# row 1 sum
x = a.sort()#its a method
print(x,a)
y = a.sort#its an attribute
print(y,a)
print(np.where(a==0))
print(np.where(a%3==0))
c = np.array([[1,3,0],[3,1,2]])
print('Before reshape = ',c)
f = c.reshape(3,2)
print('after reshape c',c,'after reshape f',f)
e = np.array([[1,3,0],[3,1,2]])
print('e = ',e)
#print(e-c) print(e+c) this wont work due to the orders of matrices 
print('e*f','and '+'f*e','this is not a matrix multiplication only square matrices work for this kind of multiplication')
