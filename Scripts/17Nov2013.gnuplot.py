#!/usr/bin/python

import subprocess as sub
import sys

gnuplot = sub.Popen(["gnuplot"], stdin=sub.PIPE,)

gnuplot.stdin.write("set sample 1000\n")
gnuplot.stdin.write("set xrange[-2:2]\n")
gnuplot.stdin.write("plot sin(x)")

for i in xrange(2,10):
    gnuplot.stdin.write("replot sin({}*x)\n".format(i))

gnuplot.stdin.write("set term png size 1000, 250\n")
gnuplot.stdin.write('set output "./foo.png" \n')
gnuplot.stdin.write("replot")
