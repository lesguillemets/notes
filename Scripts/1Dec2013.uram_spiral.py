#!/usr/bin/python2

import numpy as np
import Image
import operator as op

def sieve_of_Eratosthenes(n):
    """ returns a list of primes <= n """
    
    table = np.ones(n+1, dtype=bool)
    table[0], table[1] = False, False
    
    upperlimit = int(n/2)
    for i in xrange(2, upperlimit+1):
        if table[i]:
            jupper = n//i
            ind = i
            for j in xrange(2, jupper+1):
                ind += i
                table[ind] = False
    
    return [p for p in xrange(n+1) if table[p] ]



class SpiralGrid(object):
    
    dirs = ((-1,0), (0,1), (1,0), (0,-1))
    
    def __init__(self, n, f):
        
        self.f = f
        self.n = n
        self.grid = np.zeros((n,n), dtype=np.uint8)
        self.loc = [n//2, n//2]
        self.d = 3 # direction
        self.l = 1 # length
        self.c_dir = 1 # when to change direction
        self.count = 1 # we are on n'th grid.
        self.c_lengthen = 2 # when to lengthen
    
    def move(self):
        
        self.__setvalue(self.f(self.count)) # sets the value at the first grid
        self.__change_dir()
        
        for i in xrange(self.n**2-1):
            self.__stepforward()
        
        return self.grid
    
    def __change_dir(self):
        self.d = (self.d + 1) % 4 # rotate and
        self.c_dir = self.l # l more grids to go!
        self.c_lengthen -= 1
    
    def __stepforward(self):
        """ move -> change value -> set dirs"""
        self.loc = map(op.add, self.loc, self.dirs[self.d]) # move
        self.count += 1 # we've moved!
        self.c_dir -= 1
        
        self.__setvalue(self.f(self.count)) # set value
        
        if self.c_dir == 0:
            self.__change_dir()
        if self.c_lengthen == 0:
            self.c_lengthen = 2
            self.l += 1
        #print "currently at {},length{}, lengthen{}, cdir{}".format(
        #                        self.loc, self.l, self.c_lengthen, self.c_dir)
    
    def __setvalue(self, value):
        try:
            self.grid[self.loc[0], self.loc[1]] = value
        except ValueError as e:
            raise ValueError, "error in SG.setvalue.\n {}".format(e)

    

def main():
    N = 601
    primes = set(sieve_of_Eratosthenes(N**2))
    f = lambda n : 0 if n in primes else 255 # black point for primes, else white
    
    grid = SpiralGrid(N, f)
    grid.move()
    # print grid.grid
    img = Image.fromarray(grid.grid)
    img.show()
    img.save("Ulam_spiral_{}.png".format(N))

if __name__ == '__main__':
    main()
