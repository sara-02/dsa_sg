# coding: utf-8
from __future__ import division
import math
import cmath


def euclidean(X, Y):
    d = 0
    for x, y in zip(X, Y):
        v = math.pow((x - y), 2)
        d = d + v
    return math.sqrt(d)


def cosine(X, Y):
    d = 0
    a = sum([x * x for x in X])
    a = math.sqrt(a)
    b = sum([y * y for y in Y])
    b = math.sqrt(b)
    for x, y in zip(X, Y):
        d = d + x * y
    d = d / (a * b)
    return d


def jaccard(X, Y):
    d1 = 0
    d2 = 0
    for x, y in zip(X, Y):
        d1 = d1 + min(x, y)
        d2 = d2 + max(x, y)
    d = d1 / d2
    return d


def chebyshev(X, Y):
    d = -1
    for x, y in zip(X, Y):
        v = abs(x - y)
        if v > d:
            d = v
    return d


def minkowski(X, Y, p):
    d = 0
    for x, y in zip(X, Y):
        v = math.pow((x - y), p)
        d = d + v
    n = cmath.exp(p * cmath.log(d))
    return n.real


def main():
    X = [1, 2]
    Y = [2, 3]
    print "\nInputs is %s " % X
    print "Input is %s \n" % Y
    d = euclidean(X, Y)
    print "## Euclidean::  %f" % d
    d = cosine(X, Y)
    print "## Cosine::  %f" % d
    d = jaccard(X, Y)
    print "## Jaccard::  %f" % d
    d = chebyshev(X, Y)
    print "## Chebyshev::  %f" % d
    d = minkowski(X, Y, 3)
    print "## Minskowski::  %f" % d

if __name__ == '__main__':
    main()
