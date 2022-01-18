# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 07:56:14 2022
https://www.linkedin.com/in/raghuraj-singh-475b8715
@author: (raghuraj@hotmail.com)
"""

# global nonlocal

total = 100

def increment():
    global total
    total = -10
    print(total)
    count = 10
    count = count + total
    total += 1
    print(total)
    return count

print(increment())

# nonlocal

count = 100   # global

def outer():
    count = 0  # nonlocal
    def inner():
        nonlocal count
        count += 1
        return count
    return inner()

print(outer())


# functions: first class citizens

def add(a, b):
    return (a+b)

def sub(a, b):
    return (a-b)

def mul(a, b):
    return (a*b)

def div(a, b):
    return (a/b)

def rem(a, b):
    return (a%b)

def main():
    fun_list = [add, sub, mul, div, rem]
    for i in range(len(fun_list)):
        print(fun_list[i](10,20))

main()


    
# function as an argument:
def add(a, b):
    return (a+b)

def sub(a, b):
    return (a-b)

def mul(a, b):
    return (a*b)

def div(a, b):
    return (a/b)

def rem(a, b):
    return (a%b)

def opr(arg1, arg2, fun):
    print(fun(arg1, arg2))

def main():
    fun_list = [add, sub, mul, div, rem]

    for i in range(len(fun_list)):
        opr(10, 20, fun_list[i])

main()


# returning mutiple values thru functions
def compound_interest(p, r, n):
     amount = p * (1+r/100)**n
     return amount, amount-p

t = compound_interest(1000, 10, 5)
print(t)
type(t)
t[0]
t[1]



# variable number of parameters
# def sum_all_values(a,b,c):
# def sum_all_values(a,b,c,d,e):

def sum_all_values(*args):
    print(type(args))
    total = 0
    for val in args:
        total += val

    print (total)

sum_all_values(1, 2, 3)
sum_all_values(1, 2, 3, 4, 5)




# default values 

def compound_interest(p=1000, r=10, n=5):
     amount = p * (1+r/100)**n
     return (amount)

print(compound_interest())
print(compound_interest(n=10, p = 20000, r = 15))




import itertools as it
import operator

lst = [1,2,3,4,5]
lst = [1,2,-1,-1,4,4,2,5,6,7,8,3,4,5]

list(it.accumulate(lst))
list(it.accumulate(lst, operator.add))

list(it.accumulate(lst, min))


s = 'abcd'

list(it.permutations(s, 3))

for size in range(1,len(s)):
    print(list(it.permutations(s, size)))



perms = tuple(it.permutations(s, 3))
lst = []
for term in perms:
    word = ''.join(term)
    lst.append(word)

print(lst)


# count(start, step)
for i in it.count(5, 1):
    if i == 135:
        break
    else:
        print(i, end =" ")


it.cycle()

count=0
for i in it.cycle('ABC'):
    print(i, end = " ")
    count += 1

    if count > 50:
        break

li = [[1,2,3],[4,5,6],[7,8,9]]
print(li)


numpy
array












