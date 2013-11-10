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
    l = math.sqrt(sum([x*x for x in vect]))
    return [x/l for x in vect]


class PerlinNoise(object):
    
    def __init__(self, gridwidth, gridheight, horizontal_grids, vertical_grids):
        self.gwidth = gridwidth    # int
        self.gheight = gridheight  # how many pixels are taken from one grid?
        self.sqw = 1.0/gridwidth
        self.sqh = 1.0/gridheight
        self.hgrids = horizontal_grids #int
        self.vgrids = vertical_grids # how many grids make up the image?
        # stores values.
        self.img_ary = np.empty((self.gheight*self.vgrids,
                                 self.gwidth*self.hgrids), dtype=np.float64)
        
        self.setlattice()
    
    def setlattice(self):
        self.lat = np.array([[random_grad() for x in xrange(self.hgrids+1)]
                                         for y in xrange(self.vgrids+1)])
    
    def gather_data(self):
        for x in xrange(self.hgrids):
            for y in xrange(self.vgrids):
                self.gather_grid_data(x,y)
    
    def gather_grid_data(self,x,y):
        grid = PerlinGrid(0, 0, 1, 1,
                          self.lat[y, x], self.lat[y, x+1], 
                          self.lat[y+1, x+1], self.lat[y+1, x])
        for n in xrange(self.gwidth):
            for m in xrange(self.gheight):
                self.img_ary[self.gheight*y + m, self.gwidth*x +n] = (
                    grid.noise_at(self.sqw*(0.5+n), self.sqh*(0.5+m)) )
    
    def convert_to_256(self):
        self.img_ary = (
            (self.img_ary - self.img_ary.min()) *255 / self.img_ary.max())



def main():
    gridwidth = 50
    gridheight = 50
    horizontal_grids = 10
    vertical_grids = 10
    perlin = PerlinNoise(gridwidth, gridheight, 
                         horizontal_grids, vertical_grids)
    perlin.gather_data()
    perlin.convert_to_256()
    img = Image.fromarray(np.float64(perlin.img_ary))
    img.show()


if __name__ == '__main__':
    main()
