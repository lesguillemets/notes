#!/usr/bin/python

import random
import operator
import numpy as np
import Image
import math


class PerlinGrid(object):
    
    """
    PerlinGrid:

        (x0,y1)                  (x1,y1)
        --------------------------
        | Grad:g3                | Grad:g2
        |                        |
        |   u                v   |
        |                        |
        |      *(x,y)            |
        |                        |
        |                        |
        |   s                t   |
        |                        |
        | Grad:g0                | Grad:g1
        -------------------------- (x1, y0)
        (x0, y0)

    """
    def __init__(self, x0, y0, x1, y1, g0, g1, g2, g3):
        self.x0, self.y0, self.x1, self.y1 = x0, y0, x1, y1
        self.g0, self.g1, self.g2, self.g3 = g0, g1, g2, g3
    
    def noise_at(self, x, y):
        s = inner_product([x-self.x0,y-self.y0], self.g0)
        t = inner_product([x-self.x1,y-self.y0], self.g1)
        u = inner_product([x-self.x0,y-self.y1], self.g3)
        v = inner_product([x-self.x1,y-self.y1], self.g2)
        sx0 = ease_mean(s,t, x - self.x0)
        sx1 = ease_mean(u,v, x - self.x0)
        return ease_mean(sx0, sx1, y - self.y0)
    
    def __str__(self):
        return self.__repr__()
    
    def __repr__(sf):
        return (
        """Perlin Grid at {},{} to {},{}, with g0-g4 {},{},{},{}""".format(
            sf.x0, sf.y0, sf.x1, sf.y1, sf.g0, sf.g1, sf.g2, sf.g3))
    def getvectors(self):
        return [self.g0, self.g1, self.g2, self.g3]


        
def ease_mean(s, t, x):
    ''' 0 <= x <= 1, s, t is the weights.'''
    return s + (t-s)*easecurve(x)

def easecurve(p):
    return 3*p**2 - 2*p**3

def inner_product(vec1, vec2):
    return sum((reduce(operator.__mul__, coord, 1) for coord in zip(vec1,vec2)))

def random_grad(length = 2):
    vect = [random.random() - 0.5 for i in range(length)]
    l = sum([x*x for x in vect])
    return [x/l for x in vect]

def main():
    # create single grid.
    mygrid = PerlinGrid(0,0,1,1, 
                        *[random_grad() for j in (0,1,2,3)])
    imgwidth = 500
    imgheight = 500
    # we take dots from the centres of the grids.
    dif = (1.0/min(imgwidth, imgheight)) / 2
    img_ary = np.zeros((imgheight,imgwidth))
    for i in xrange(imgheight):
        for j in xrange(imgwidth):
            img_ary[i,j] = mygrid.noise_at(
                            i/float(imgheight)+dif, j/float(imgwidth)+dif)
    # convert to 0-255 gray scale.
    img_ary = (img_ary - img_ary.min()) * 255 / img_ary.max()
    img = Image.fromarray(np.float64(img_ary))
    img.show()


if __name__ == '__main__':
    main()
import random
import operator
import numpy as np
import Image


class PerlinGrid(object):
    
    """
    PerlinGrid:

        (x0,y1)                  (x1,y1)
        --------------------------
        | Grad:g3                | Grad:g2
        |                        |
        |   u                v   |
        |                        |
        |      *(x,y)            |
        |                        |
        |                        |
        |   s                t   |
        |                        |
        | Grad:g0                | Grad:g1
        -------------------------- (x1, y0)
        (x0, y0)

    """
    def __init__(self, x0, y0, x1, y1, g0, g1, g2, g3):
        self.x0, self.y0, self.x1, self.y1 = x0, y0, x1, y1
        self.g0, self.g1, self.g2, self.g3 = g0, g1, g2, g3
    
    def noise_at(self, x, y):
        s = inner_product([x-self.x0,y-self.y0], self.g0)
        t = inner_product([x-self.x1,y-self.y0], self.g1)
        u = inner_product([x-self.x0,y-self.y1], self.g3)
        v = inner_product([x-self.x1,y-self.y1], self.g2)
        sx0 = ease_mean(s,t, x - self.x0)
        sx1 = ease_mean(u,v, x - self.x0)
        return ease_mean(sx0, sx1, y - self.y0)
    
    def __str__(self):
        return self.__repr__()
    
    def __repr__(sf):
        return (
        """Perlin Grid at {},{} to {},{}, with g0-g4 {},{},{},{}""".format(
            sf.x0, sf.y0, sf.x1, sf.y1, sf.g0, sf.g1, sf.g2, sf.g3))
    def getvectors(self):
        return [self.g0, self.g1, self.g2, self.g3]


        
def ease_mean(s, t, x):
    ''' 0 <= x <= 1, s, t is the weights.'''
    return s + (t-s)*easecurve(x)

def easecurve(p):
    return 3*p**2 - 2*p**3

def inner_product(vec1, vec2):
    return sum((reduce(operator.__mul__, coord, 1) for coord in zip(vec1,vec2)))


def main():
    # create single grid.
    mygrid = PerlinGrid(0,0,1,1, 
                        *[[random.random() for i in (0,1)] for j in (0,1,2,3)])
    imgwidth = 500
    imgheight = 500
    dif = (1.0/min(imgwidth, imgheight)) / 2  # we take dots from the centres of the grids.
    
    img_ary = np.zeros((imgheight,imgwidth))
    
    # let's take samples
    for i in xrange(imgheight):
        for j in xrange(imgwidth):
            img_ary[i,j] = mygrid.noise_at(
                            i/float(imgheight)+dif, j/float(imgwidth)+dif)
    
    # convert to 0-255 gray scale.
    img_ary = (img_ary - img_ary.min()) * 255 / img_ary.max()
    img = Image.fromarray(np.float64(img_ary))
    img.show()


if __name__ == '__main__':
    main()
