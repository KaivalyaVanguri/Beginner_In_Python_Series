l1 = ['k','a','i','v','a','l','y','a','']
l2 = [0,1,2,3,4,5,6,7]
l3 = ['V','a','n','g','u','r','i']
print('\nList Functions\n')
print(l1)
l1.append(l3)
print('Appended',l1)
print('length',len(l1))
c = l1.copy()
print('Copied list',c)
l1.clear()
print('list cleared',l1)
l1 = ['k','a','i','v','a','l','y','a','','']
d = l1.count('a')
print('count of a',d)
l1.extend(l3)
print('extended list',l1)
f = l1.index('g')
print('Index of g',f)
print('list before insertion',l2)
l2.insert(len(l2),10)
print('inserted new list',l2)
h = l2.pop(4)
print('Popped list {0} and popped item {1}'.format(l2,h))
i= l1.remove('')
print('removed space from list',l1,i)
l2.reverse()
print('Reversed list',l2)
l2.sort()
print('Sorted list',l2)
print('List indexing',l1[1])
fruits = ['apples', 'oranges', 'bananas']
tangerines = (2, 9) 
fruits.append(tangerines)
print('Appended list with tuple',fruits)
fruits += [1]
print('Addition of integer to a list',fruits)
print('',type(l2[2]))
