# -*- coding: utf-8 -*-
"""
Created on Wed Jan  5 08:06:57 2022
https://www.linkedin.com/in/raghuraj-singh-475b8715
@author: (raghuraj@hotmail.com)
"""

# OOPS

_name: private member
__name: Mangling. Cannot be overridden
__name__: dunder. 
name_: sharing keyword's name
_

for i in range(0,5,1):
    print("hello")

for _ in range(0,5,1):
    print("hello")


ord('a')
ord('0')
ord('A')

chr(97)

# alising
a = 100

b = a   # alising

id(a)
id(b)


# complex
c1 = 10 + 30j
type(c1)
print(c1)


c2 = -20J - 10
type(c2)
print(c2)

c3 = -100i - 100   # error

c1.conjugate()

c1.real
c1.imag

type(c1)

s = 'abcdf\'\'eghj'
type(s)
print(s)

import string
print(dir(string))

string.ascii_letters
string.digits
string.hexdigits
string.printable

# slicing

s = 'abcdefghijkl'
print(s)
s[0]
s[-1]
s[-len(s)]
s[0:4]   # range(start, stop+1,inc/dec)
s[0:4:1]
s[4:]
s[:4]
s[4:7:-1]
s[7:4:-1]

Pythonic way of programming:
    
Palindrome: MADAM

s = input('Enter a string: ')
s = 'MADAM'

if s[::] == s[::-1]:
    print(f'{s} is palindrome')

a = 100
b = 200

a,b = b,a


module: a python file, .py

__init__.py


# exercise: 
create a password:
    a..z    = 3
    A..Z    = 3
    0..9    = 3
    sp. char = 2

    
s1 = 'First'
s2 = 'Second'

s1+s2

s1 + 10
s1 + '10'
s1+str(1000)


'r' in s1
'z' in s1
 
s1 * 3

s = "Python-is-a-very-good language and very easy to learn"
print(s.split())
print(s.split('-'))


s1 = ('apple','banana', 'mango')
s = ' '.join(s1)
print(s)




for i in range(random.randrange(7,11)):
    print(random.choice(string.printable),end='')












