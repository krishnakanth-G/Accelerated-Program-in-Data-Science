# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 07:33:01 2022
https://www.linkedin.com/in/raghuraj-singh-475b8715
@author: (raghuraj@hotmail.com)
"""

import random

random.seed(10)
print(random.random())

random.seed(-1)
print(random.random())

num = random.random()
print(num)

num = round(random.random()*100)
print(num)

random.randint(1,100)
random.randint(50,60)

random.randrange(1,100)

random.randrange(1,100, 5)

random.randrange(1,100,10)

lst = ["apple", "banana", "cherry", "dragon fruit","Elephant","Fig"]
random.choice(lst)

s = 'abcdefghijklmnopqrstuvwxyz'
random.choice(s)

random.choices(lst, weights=(5,1,1,1,1,1), k=10)

random.shuffle(lst)
print(lst)

'''
password generation:
upper case alphabets = 3
lower case alphabets = 3
digits = 3
special characters = 3 
'''
ualpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lalpha = 'abcdefghijklmnopqrstuvwxyz'
digit = '1234567890'
sp = '!@#$%^&*()'
passwd = ''
passwd += ''.join(random.choice(ualpha) for i in range(3))
passwd += ''.join(random.choice(lalpha) for i in range(3))
passwd += ''.join(random.choice(digit) for i in range(3))
passwd += ''.join(random.choice(sp) for i in range(3))
passwd = list(passwd)
random.shuffle(passwd)
passwd = ''.join(passwd)
print(passwd)

import string
passwd = ''
passwd += ''.join(random.choice(string.ascii_uppercase) for i in range(3))
passwd += ''.join(random.choice(string.ascii_lowercase) for i in range(3))
passwd += ''.join(random.choice(string.digits) for i in range(3))
passwd += ''.join(random.choice(string.printable) for i in range(3))
passwd = list(passwd)
random.shuffle(passwd)
passwd = ''.join(passwd)
print(passwd)


random.sample(lst,2)

passwd = ''
passwd += ''.join(random.sample((string.ascii_uppercase),3))
passwd += ''.join(random.sample((string.ascii_lowercase),3))
passwd += ''.join(random.sample((string.digits),3))
passwd += ''.join(random.sample((string.printable),3))
passwd = list(passwd)
random.shuffle(passwd)
passwd = ''.join(passwd)
print(passwd)



# list
'''
List is a data structure in Python
It is a collection of heterogenous elements
Elements are ordered. The order of the elements is preserved.
Elements can be accessed with the help of index values.
First element from the left side has an index value of 0    
First element from the right side has an index value of -1    
It allows duplicate elements to exists
It is mutable data structure, i.e., it allows insertion, deletion and updations
It allows nesting of the elements. 
List may contain other data structures like, list, tuple, string, dict etc
List elements are enclosed in [] and elements are separated by commas
An empty list is created with the help of function list(), or empty pair of []
'''

'''
operations on list:
    addition of two lists result in a list

'''

lst = list()
lst = []

lst = list(range(1,10))
print(lst)


lst_copy = lst
id(lst)
id(lst_copy)

lst_copy = lst.copy()
id(lst)
id(lst_copy)

lst_copy = lst[::]
id(lst)
id(lst_copy)


lst = [0,1,2,3,4,5,6,7,8,9]
print(lst)

lst[:]
lst[::]
lst[3:]
lst[:5]
lst[::-1]
lst[1:5:-1]
lst[5:1:-1]

# Exercise
stack: LIFO, FILO = push()=append(), pop()= pop()

lst
lst.append(10)
lst
lst.append(11)
lst
lst.pop(-1)
lst
lst.pop(5)
lst

lst.remove(4)
lst

lst.insert(0,10)
lst
lst.insert(5,4)
lst = [1,2,2,3,3,4,5,5,4,3,3,4,4,6,5,4,4,5,4,5,5]

lst.remove(5)
lst

L = ['a', 'b', ['cd', 'ef', ['ghi', 'jkl']], ['mn','op','qr'], 's']
len(L)

L[2]
L[3]
L[2][2][0][1]
L[2]

L[-3][-3][-2][-2]
L[-3][-1][-2][-2]

lst = [1,1.2,10+100j, True]
lst


str list

lst = [1,2,3,4]
id(lst)
lst.append(10)
id(lst)

s = 'abcdg'
id(s)

s = 'xyz'
id(s)

s = 'abcdg'
id(s)

lst.reverse()
lst

lst = lst * 2
lst.clear()
lst

odd = [1,3,5,7,9]
even = [2,4,6,8,10]

alln = odd + even
alln

alln.sort()
alln

lst = [1,2,3,4,2.3,4.5,10+20j]
lst.sort()
lst


2 in lst













