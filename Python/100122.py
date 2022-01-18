# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 08:09:42 2022
https://www.linkedin.com/in/raghuraj-singh-475b8715
@author: (raghuraj@hotmail.com)
"""

'''
set:
    
set = set()
A set is a heterogeneous collecion of unique values, separated by commans, enclosed in {}
An empty set is declared using the function set()
It is mutable data structure. It allows insertion, updation and deletion of elements.
(updation => deletion + inserion)
Order of the elements is not preserved. Elements can be sorted.
Duplicates are not allowed.
Indexing and slicing are not allowed.
'''

s = {}
type(s)

s = set()
type(s)

s= {10,20,30,40,50}
print(s)
type(s)

lst = [10,20,30,40,50]
s = set(lst)
print(s)
type(s)

s = set(range(10))
print(s)
type(s)

s.add(60)
print(s)

s[0]

even = {2,4,6,8}
odd = {1,3,5,7}

s = set()
s.update(even,odd)
print(s)

s.update(100)   # error

s.pop()
print(s)

s.pop(3)

s.remove(3)
print(s)

s.discard(5)
print(s)


s.clear()
print(s)


s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}

# Union, Intersection, Difference, Symmetric difference

s = s1.union(s2)
print(s)

s= s1 | s2
print(s)

s = s1.intersection(s2)
print(s)

s = s1 & s2 
print(s)

s = s1.intersection(s2)
print(s)

s = s1 - s2
print(s)


s = s1.symmetric_difference(s2)
print(s)


vowels ={'a','e','i','o','u'}
print(vowels)
flag = "b" in vowels
print(flag)

s[1:4]


lst = [1,2,3,4,5,4,3,3,1,2,3,4,5,6,4,4,3,3]
lst_un = list(set(lst))
print(lst_un)
type(lst_un)


# To print vowels present in a word:

string = 'Hello How are you?'

s = set(string)
print(s)
v = {'a','e','i','o','u'}
vinw = s.intersection(v)
print("Vowels present in the word: ", vinw)   


# Comprehensions

comprehension is an elegant way to define and create data structures(ds) ( list, set and dict)
They provide a concise syntax for completing this task, limiting our lines of code.
comprehension is generally more compact and faster than normal functions and loops for creating ds
However, we should avoid writing very long comprehensions in one line to ensure that code is user-friendly.
every comprehension can be rewritten in for loop, but every for loop can’t be rewritten in the form of list comprehension.
comprehensions can make our code more succinct, it is important to ensure that our final code is as 
readable as possible, so very long single lines of code should be avoided to ensure that our code is user friendly.



# Create a set of squares of numbers from 1 to 10
s = {x*x for x in range(10)}
print(s)

# Create a set of numbers 2**x, where x is a even number less than 10
s = {2**x for x in range(2,10,2)}
print(s)


lst = [1, 2, 2, 3, 3, 4, 4, 4]
s = {var for var in lst}
print(s)


Create a set of ordered pairs (x,y) where x takes values 3 and 4 and y takes values 1 and 2 

s = {(var1, var2) for var2 in range(1, 3) for var1 in range(3, 5)}
print(s)

# Create a set of squares of numbers from a given range such that the square is a multiple of 4 and 6
s = {var**2 for var in range(10) if var**2 % 4 == 0 and var**2 % 6 == 0}
print(s)


from timeit import default_timer as timer

# comprehension
start = timer()
addition = [num/10 for num in range(1,100000)]
end = timer()
print(end - start)

print(addition)


# iteration
start = timer()
addition = []
for i in range(1, 100000):
    addition.append(i/10)
end = timer()
print(end-start)    



print(addition)







