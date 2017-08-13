# coding: utf-8
from __future__ import division
import random


def fx(x, m, c):
    return m * x + c


def jcost(X1, Y1, n, m, c):
    sum = 0
    for x, y in zip(X1, Y1):
        v = fx(x, m, c) - y
        sum += v * v
    return sum / n


def dm(X1, Y1, n, m, c):
    sum = 0
    for x, y in zip(X1, Y1):
        sum += fx(x, m, c)
    return sum / n


def dc(X1, Y1, n, m, c):
    sum = 0
    for x, y in zip(X1, Y1):
        sum += (fx(x, m, c) - y) * x
    return sum / n


def gd(X, Y, n, mold, cold, count):
    al = 0.01
    ep = 0.001
    mnew, cnew = 0, 0
    jcnew = 0
    m = int(len(X) / n)
    while count != 0:
        print("###Epoch %d" % count)
        p = 0
        for i in range(m):
            X1 = X[p:p + n]
            Y1 = Y[p:p + n]
            jcold = jcost(X1, Y1, n, mold, cold)
            print(mold, cold, jcold)
            mnew = mold - al * dm(X1, Y1, n, mold, cold)
            cnew = cold - al * dc(X1, Y1, n, mold, cold)
            cold = cnew
            jcold = jcnew
            p = p + n
        count = count - 1
    return mold, cold


def main():
    X = random.sample(range(500), 500)
    Y = random.sample(range(1000), 500)
    # n = len(Y)
    n = 250
    # n = 1
    count = 100
    mold = 1
    cold = 0
    m, c = gd(X, Y, n, mold, cold, count)
    print("############################################")
    print("m = %f" % m)
    print("c = %f" % c)
    print("############################################")


if __name__ == '__main__':
    main()
