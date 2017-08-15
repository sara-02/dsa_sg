# coding: utf-8
from __future__ import division
import math


def cummulative_normal_dist(x, u, s):
    z = (x - u) / (s * math.sqrt(2))
    e = math.erf(z)
    d = 0.5 * (1 + e)
    return d


def n_mean(n, u):
    return n * u


def n_std(n, s):
    return s * math.sqrt(n)


def clt(n, x, u, s):
    u1 = n_mean(n, u)
    s1 = n_std(n, s)
    return cummulative_normal_dist(x, u1, s1)


def zscore(n, z, u, s):
    u1 = n_mean(n, u)
    s1 = n_std(n, s)
    v1 = u1 / n
    v2 = s1 * z / n
    za = v1 - v2
    zb = v1 + v2
    return (za, zb)

"""
A large elevator can transport a maximum of 9800 pounds. Suppose a load of cargo containing 49 boxes must be transported via the elevator. The box weight of this type of cargo follows a distribution with a mean of 205 pounds and a standard deviation of 15 pounds. Based on this information, what is the probability that all boxes can be safely loaded into the freight elevator and transported?
"""


def elevator():
    x = 9800
    n = 49
    u = 205
    s = 15
    c = clt(n, x, u, s)
    print "## The probability of load success is % f" % c


"""
The number of tickets purchased by each student for the University X vs. University Y football game follows a distribution that has a mean of 2.4 and a standard deviation of 2.0.

A few hours before the game starts, 100 eager students line up to purchase last-minute tickets. If there are only 250 tickets left, what is the probability that all students will be able to purchase tickets?
"""


def tickets():
    n = 100
    x = 250
    u = 2.4
    s = 2
    c = clt(n, x, u, s)
    print "## The probabilty of getting 100 tickets is %f" % c

"""
Task
You have a sample of 100 values from a population with mean 500 and with standard deviation 80. Compute the interval that covers the middle of 95% the distribution of the sample mean; in other words, A and B compute and such that P(A<x<B) is 0.95. Use the value of z=1.96. Note that is the z-score.
"""


def population():
    n = 100
    z = 1.96
    u = 500
    s = 80
    A, B = zscore(100, 1.96, 500, 80)
    print "## The lower limit is %f" % A
    print "## The upper limit is %f" % B


def main():
    print "\n"
    elevator()
    tickets()
    population()
    print "\n"

if __name__ == '__main__':
    main()
