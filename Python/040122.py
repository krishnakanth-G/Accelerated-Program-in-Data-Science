# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 08:01:58 2022
https://www.linkedin.com/in/raghuraj-singh-475b8715
@author: (raghuraj@hotmail.com)
"""


int = 4 bytes = 2**31 - 1 = 2147483647
float = 8 bytes = 2**63 - 1 = 9223372036854775807
complex = 16 bytes = 8 + 8 = 

byte = -128 to -1   +0 - +127

a = 10
type(a)

f = 1.23

import sys
sys.getsizeof(a)

sys.getsizeof(f)


a = 2**63 - 1
print(a)
type(a)
sys.getsizeof(a)

import math
dir(math)
print(dir(math))

a = math.factorial(10)
print(a)
sys.getsizeof(a)

a = math.factorial(100)
print(a)
type(a)
sys.getsizeof(a)


a = math.factorial(1000)
print(a)
type(a)
sys.getsizeof(a)


a = math.factorial(10000)
print(a)
type(a)
sys.getsizeof(a)


int float complex bool str
short long huge double lon double, unsigned


True False None 

import builtins
print(dir(builtins))

dunder

addition = 10
print(sum)

sum([1,2,3,4,5])

True = 100

True + True
False + False
True + False

False = 0, null
True = 1, any +ve value , any -ve value, any non null

bool(0)
bool(100)
bool(-100)
bool('')
bool('*')

0b/0B   0o/0O   0x/0X
bin     oct     hex      dec (default)

a = 1101
type(a)
print(a)

a = 0b1101
print(a)

a = 0B1101
print(a)
type(a)


a = 0o567
print(a)
type(a)

a = 0O567
print(a)
type(a)

a = 0xfed
print(a)
type(a)

a = 0XFeDcB89876
print(a)
type(a)

A Python identifier can be a combination of lowercase/ uppercase letters, digits, or an underscore. 
An identifier name cannot begin with a digit.

Keywords cannot be used as identifiers.
Special symbols cannot be used in the identifier name.

casting: If you mix an integer and a float in any other operation, you’ll get a float.

'a' + 10
'a' + 10.123

MAXIMUM = 100
print(MAXIMUM)
type(MAXIMUM)

MAXIMUM = 1000

if __name__ == "__main__":


# print()
a = 10
b = 20
c = a + b

print('The sum of',a,'and',b,'is',c)
print("The sum of",a,"and",b,"is",c)
print("The sum of " + str(a) + " and " + str(b) + " is " + str(c))
print("The sum of %s and %s is %s " % (a, b, c))
print("The sum of {0} and {1} is {2}".format(a, b, c))
print("The sum of {} and {} is {}".format(a, b, c))
print(f'The sum of {a} and {b} is {c}')     # f srings/syntax
print(f"The sum of {a} and {b} is {c}")     # f srings/syntax
print(f"The sum of {a} and {b} is {c}")   # 3.6 or more...

{{{}}}
begin end

: = Beginning, start
    
















