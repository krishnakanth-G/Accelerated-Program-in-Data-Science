# -*- coding: utf-8 -*-
"""
Created on Fri Jan  7 07:51:42 2022
https://www.linkedin.com/in/raghuraj-singh-475b8715
@author: (raghuraj@hotmail.com)
"""

'''
tuple:   
Its a READ ONLY collection of Heterogeneous elements.
It does not allow any changes to be made to its elements. 
For this reason, it is inilialized during its creation.
An empty tuple can be created with the help of tuple() or with the help of empty ().
Insertion order is preserved.
Duplications are allowed. 
A tuple is like a read only list.
Elements within a tuple are accessed with the subcripts.
'''

t = ()
type(t)

t = tuple()
type(t)

t = 10,20,30
type(t)

# a,b = b,a

print(t)

t = (10)
type(t)

t = (10,)
type(t)
print(t)

a = 10
b = 20
c = 30
d = 40
t = a,b,c,d
print(t)
type(t)

w,x,y,z = t

w,x,z = t     # error
w,x,y,z,u = t # error

t1 = (10,20,30)
t2 = (100,200,300)
t3 = t1+t2
print(t3)

t3 = t1*2
print(t3)

t3.count(10)
t3.count(1000)

t3.index(10)
t3.index(20)
t3.index(200)

min(t3)
max(t3)
len(t3)


t = (10, 20, 30, 40, 50, 60, 70)

t[:]
t[::]
t[::-1]

t[5] = 100


# nesting
t = (1,2,[33,44,55],6,7,8)
type(t)
len(t)
t[2]
t[2][1]
t[-4][-2]

t[2][1] = 444
print(t)


t = [1,2,(33,44,55),6,7,8]
type(t)
t[2][1]
t[-4][-2]

t[-4][-2] = 4

type(t[-4])

# list   tuple

# Dictionary

'''
dict()  {}

Dictionary is a dynamic and mutable data structure.
It is a structure that stores the data as key-value pairs.
An empty dictionary is declared using a pair of empty {}, or with the help of dict()
Keys and values can belong to heterogeneous data types
Keys are used as index and allows the individual values to be accessed.
Keys cannot be duplicated, values can be duplicated.
Insertion order is not preserved
Indexing and slicing are not supported.

general structure: d = {key1:value1,key2:value2,.......,key-n:value-n}
'''
d = {}
print(d)
type(d)

d = dict()
type(d)

d = {1: "first", 2:"second", 3:"third", 4:"fourth",5:"fifth",6:"sixth", 3:'three'}    
print(d)

d[1]
d[0]

d[0] = 'Zero"'
print(d)
d[-1] = 'Negative'
print(d)

d[-1] = 'Negative value'

print(d)

d[2] = 'three'
print(d)

d[1.2] = 'float'
print(d)

d['abc'] = 'float'
print(d)


len(d)

print(d.keys())
print(d.values())
print(d.items())

keys = d.keys()
type(keys)

d.get(2)
d.get(100)
d[100]

d_al = d
id(d)
id(d_al)

d_copy = d.copy()
id(d)
id(d_copy)

d.update({7: 'seventh'})
print(d)

d2 = {8:'eightth', 9:'ninth', 10:'tenth'}
d.update(d2)
print(d)

d.get('three')


for i in (d.keys()):
    print(i, end = ' ')
    print('value' == d.get(i))


print(1 in d)
print('abc' in d)


d1 = {1:'one',  2:'two', 3:'three', 4:'four'}
d2 = {5:'five', 6:'six', 7:'seven', 8:'eight'}

dmerge = {**d1, **d2}
print(dmerge)


print(d)
d.pop()    # error
d.pop(6)
print(d)
d.pop(6)   # error, as the key does not exists..

d.popitem()

print(d2)
d2.clear()
print(d2)
type(d2)

del d2
type(d2)    # error

'''
         create  create
list     []      list()
tuple    ()      tuple()
dict     {}      dict()
set      -       set()
'''

s = {1,2,3,4,5}
type(s)
s = {}
type(s)

s = {1,2,3,4,5}
print(s)

'''
Set
A set is a heterogeneous collecion of unique values, separated by commans, enclosed in {}
An empty set is declared using the function set()
It is mutable data structure. It allows insertion, deletion of elements.
Order of the elements is not preserved. Elements can be sorted.
Duplicates are not allowed.
Indexing and slicing are not allowed.
'''

s = {1,1,1,1,1,2,2,2,2,2,2,3,3,3,3,3,3,4,4,4,4,4}
print(s)


s = set(range(10))
print(s)

l = [1,2,3,4,4,4,5,5,5,5,66,6,6,7]
s = set(l)
print(s)

s.add(100)
print(s)

s.add(100)
print(s)

even = {2,4,6,8}
odd = {1,3,5,7}
s = set()

s.update(even,odd)
print(s)





