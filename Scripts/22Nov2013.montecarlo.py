#!/usr/bin/python

N = 100000
from random import random as rand

# Normally, one can write
counter = 0
for i in xrange(N):
    if rand()**2 + rand()**2 <= 1:
        counter += 1
pi = counter * 4.0 / N
print pi


# using list comprehension.
pi = len(filter(lambda x: x, [rand()**2 + rand()**2 <= 1 for i in xrange(N)]))*4.0/N
print pi

# another way
pi = len([None for i in xrange(N) if rand()**2 + rand()**2 <= 1])*4.0/N
print pi

# using `sum` seems better, as it can handle generators.
pi = sum((rand()**2 + rand()**2 <= 1 for i in xrange(N)))*4.0/N
print pi

# makes list of dots.
pi = len(filter(lambda v: sum(map(lambda x: x**2, v))<=1, 
                ((rand(), rand()) for i in xrange(N))))*4.0/N
print pi

# what you can do with list comprehension, you can do with map function.
pi = sum(map(lambda x: rand()**2 + rand()**2 <= 1, xrange(N)))*4.0/N
print pi

# filter 
pi = len(filter(lambda x: rand()**2 + rand()**2 <=1, xrange(N)))*4.0/N

# yay lambda!?
pi = reduce(lambda x,y: x+1 if rand()**2 + rand()**2 <= 1 else x, xrange(N), 0)*4.0/N
print pi

# let's use reduce again.
pi = reduce(lambda x,y : x+1 if y else x, 
            (rand()**2 + rand()**2 <= 1 for i in xrange(N)), 0) *4.0/N
print pi

# recursion...
def montec1(n):
    if n == 0:
        return 0
    else:
        if rand()**2 + rand()**2 <= 1:
            return montec1(n-1) + 1
        else:
            return montec1(n-1)
print montec1(500)*4.0/500

# tail recursion
def montec_tail(n, counter):
    if n == 0:
        return counter
    else:
        if rand()**2 + rand()**2 <= 1:
            return montec_tail(n-1, counter+1)
        else:
            return montec_tail(n-1, counter)

def montec2(n):
    return montec_tail(n, 0)

print montec2(500)*4.0/500
