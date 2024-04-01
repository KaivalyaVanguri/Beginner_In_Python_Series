''''Remember sets are mutable and are disordered'''
set1 = {1,12,3,52,89,43,34,98,'k','g'}
set2 = {3,53,43,23,14,67,9,5,'k','k'}
set3 = {3,9,5,14}
set4 = {'k','g','l','a','s','v','b'}
set5 = {'a','b','c','d','e'}
print('\nSet Functions\n')
print(set1, set2) 
s = set1.add(23)
print(set1 & set2)#intersection
print(set1 | set2)#union
print(s,set1)   
a = set1.copy()
print(a)
b = set1.difference(a)
print(b)
c = set1.difference_update(set2)
''''set1.difference_update(set2) need not be the same as set2.difference_update(set1) same applies to all update functions '''
print(c,set1)
d = a.clear()
print(d,a)
e = set1.discard('g')
print(e,set1)
f = set1.issuperset(set3)
g = set3.issubset(set2)
print(f, g)
h = set4.intersection(set5)
print(h,set4,set5)
i = set4.intersection_update(set5)#like this one here
'''' this update function doesnt give out a value instead it updates the set with the operation executed'''
print(i,set4,set5)
j = set1.isdisjoint(set4)
print(j)
p = set2.pop()#takes no arguments
print(p,set2)
m = set1.remove(98)
print(m,set1)
k = set1.symmetric_difference(set2)
l = set4.symmetric_difference_update(set5)#this one too
print(k,l,set4)
u = set5.union(set4)
print(u,set4,set5)
''''observe carefully the output set5.union(set4) turns set5 to union set and set4.union(set5) turns set4 to union set'''
