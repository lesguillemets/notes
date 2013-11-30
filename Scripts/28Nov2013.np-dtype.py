#!/usr/bin/python

import numpy as np

def main1():

    print(dir(np.array([32])))

    arrays = {
        'a' : np.array([1,2,3]),
        'b' : np.array([1.0, 2]),
        'c' : np.array([True, False]),
        'd' : np.array([]),
        'e' : np.array(['t', 'h', 'e']),
        'f' : np.array(['there']),
        'g' : np.zeros(2),
        'h' : np.empty(2),
        'i' : np.zeros(2,dtype=int),
        'j' : np.zeros(2,dtype='int8'),
        'k' : np.zeros(2,dtype=np.int8),
    }

    for (p,q) in  arrays.iteritems():
        print p,q,q.dtype


def main2():
    
    a = np.zeros(6, dtype='int8')
    a[0] = 3
    a[1] = 255
    a[2] = 256
    a[3] = 256/2 -1
    a[4] = 256/2 
    a[5] = 12631
    print a

def main3():
    
    a = np.array([3.0, int(2), True])
    print a, a.dtype

    b = np.array([3.0, int(2), True, 't'])
    print b, b.dtype
    
    class A(object):
        pass
    c = np.array([A()])
    print c, c.dtype
    d = np.array([3, A()])
    print d, d.dtype
    e = np.array([3, 'the', A()])
    print e, e.dtype

def main4():
    mydt16 = np.dtype([('my_type_name', np.int16)])
    mydt8 = np.dtype([('my_type_name', np.int8)])
    print mydt16, mydt8


main4()
