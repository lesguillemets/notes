#!/usr/bin/python

# from : http://urasunday.com/u-2_09/comic/002_001.html

class B(object):
    def __init__(self, m, n, f=lambda n: n+1):
        self.m = m
        self.n = n
        self.f = f
        self.value = None
    
    def calc(self):
        if isinstance(self.n, B):
            self.n.calc()
            if self.n.value is not None:
                self.n = self.n.value
        elif isinstance(self.m, B):
            self.m.calc()
            if self.m.value is not None:
                self.m = self.m.value
        else:
            if self.m == 0:
                self.value = self.f(self.n)
            elif self.n == 0:
                self.m -= 1
                self.n = 1
            else:
                self.m -= 1
                self.n = B(self.m+1, self.n-1)
    
    def __str__(self):
        return 'B(' + str(self.m) + ', ' + str(self.n) + ')'

b = B(3,3)

while True:
    print b
    b.calc()
    if b.value is not None:
        print b.value
        break
