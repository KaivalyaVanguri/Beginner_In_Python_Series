import numpy as n
a = n.array([[1,2,3],[2,3,4]])
print('a',a)#print(a[]) SyntaxError: invalid syntax
print('dimensions of a',a.ndim)
print('size of a',a.size)
print(a.itemsize)
print('Data type of a',a.dtype)
s = a.shape
print('shape of a',s)
print(a[1][2])
print(a[0])
x = a.copy()
x[1] = 7
print('copy effect on a with x', a )
print('x',x)
y = a.view()
y[1] = 5
print('view effect on a with y', a )
a[1] = 7
print('y',y)
a[1] = 5
print('copy effect on x', a , x )
print('view effect on y', a , y)
#b = np.array([[d, b, c],[2,3,4],[3,4,5]]) NameError:
b = n.array([['a','b','c'],['b','c','d'],['c','d','e']])
print('dimensions of b',b.ndim)
print('shape of b',b.shape) 
print('b',b[0:2]) #== print(b)
print(b[2,0:2])
print(b[0:2,1:])
c = n.array([['a','b','c','d','e'],[1,2,3,4,5]])
print('c',c)
print('shape of c',c.shape)
print('dimensions of c',c.ndim)
