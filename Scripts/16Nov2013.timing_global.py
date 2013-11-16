#!/usr/bin/python
import time

x = time.time()
for i in xrange(1000):
    for j in xrange(1000):
        a=3
        b=5
        if a < b:
            pass
        else:
            pass
y = time.time()
print y-x

x = time.time()
def g():
    global i,j,a,b
    for i in xrange(1000):
        for j in xrange(1000):
            a=3
            b=5
            if a < b:
                pass
            else:
                pass
y = time.time()
print y-x

x2 = time.time()
g()
y2 = time.time()
print y2-x2

