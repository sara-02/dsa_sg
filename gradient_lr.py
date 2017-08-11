# coding: utf-8
# Linear regression with one variable, gradient descent
# Batch gradient descent

from __future__ import division
import random


def fx(x, m, c):  # find f(x)= y = mx+c
    return m * x + c


def jcost(X, Y, n, m, c):  # find cost function value
    sum = 0
    for x, y in zip(X, Y):
        v = fx(x, m, c) - y
        sum += v * v
    return sum / n


def dm(X, Y, n, m, c):  # partial diff of m
    sum = 0
    for x, y in zip(X, Y):
        sum += fx(x, m, c)
    return sum / n


def dc(X, Y, n, m, c):  # partial diff of c
    sum = 0
    for x, y in zip(X, Y):
        sum += (fx(x, m, c) - y) * x
    return sum / n


def gd(X, Y, n, mold, cold):  # gradient descent function
    al = 0.001  # learning rate
    ep = 0.0001  # tolerance rateW
    count = 5000  # max number of iteration
    jcold = jcost(X, Y, n, mold, cold)
    mnew, cnew, jcnew = 0, 0, 0

    while count != 0:
        print mold, cold, jcold
        mnew = mold - al * dm(X, Y, n, mold, cold)  # i+1th value from ith value
        cnew = cold - al * dc(X, Y, n, mold, cold)
        if mnew == mold or cnew == cold:  # minima reached
            break
        jcnew = jcost(X, Y, n, mnew, cnew)
        if abs(jcnew - jcold) <= ep:  # cost tolerence exceeeded
            break
        mold = mnew
        cold = cnew
        jcold = jcnew
        count = count - 1
    return mnew, cnew


def main():
    X = random.sample(range(500), 5)  # independent variable
    Y = random.sample(range(1000), 5)  # dependent variable
    n = len(Y)  # number of samples
    mold = 1  # intial value for m
    cold = 0  # intial value for c
    m, c = gd(X, Y, n, mold, cold)
    print "\n#################################################"
    print "m = %f" % m
    print "c = %f" % c
    print "#################################################\n"

if __name__ == '__main__':
    main()
