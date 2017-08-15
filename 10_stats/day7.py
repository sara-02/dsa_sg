# coding: utf-8
from __future__ import division
import math


def mean_a(a):
    sum_a = 0
    count = 0
    for i in a:
        sum_a += i
        count += 1
    return sum_a / count


def std(a):
    u = mean_a(a)
    n = len(a)
    sum = 0
    for x in a:
        v = x - u
        sum += v * v
    std = math.sqrt(sum / n)
    return std


def cov(X, Y):
    mx = mean_a(X)
    my = mean_a(Y)
    sum = 0
    for x, y in zip(X, Y):
        sum += (x - mx) * (y - my)
    c = sum / len(X)
    return c


def pearson(X, Y):
    stdx = std(X)
    stdy = std(Y)
    c = cov(X, Y)
    pear = c / (stdx * stdy)
    return pear


def rank(X):
    d = {x: 0 for x in X}
    s = sorted(X)
    r = 1
    for i in s:
        if d[i] == 0:
            d[i] = r
            r = r + 1
        else:
            continue
    rk = []
    for i in X:
        rk.append(d[i])
    return rk


def sp_unique_formula(X, Y):
    n = len(X)
    rkx = rank(X)
    rky = rank(Y)
    s = sum([math.pow(x - y, 2) for x, y in zip(rkx, rky)])
    v1 = 6 * s
    v2 = n * (n + 1) * (n - 1)
    v3 = v1 / v2
    r = 1 - v3
    return r


def main():
    print "\n"
    X = [10, 9.8, 8, 7.8, 7.7, 1.7, 6, 5, 1.4, 2]
    Y = [200, 44, 32, 24, 22, 17, 15, 12, 8, 4]
    p = pearson(X, Y)
    print "## Pearson Correlation coefficient is %f " % p
    rkx = rank(X)
    rky = rank(Y)
    prk = pearson(rkx, rky)
    sp = sp_unique_formula(X, Y)
    assert round(prk, 5) == round(sp, 5)
    print "## Spearman's Rank Correlation Coefficient is %f" % sp
    print "\n"

if __name__ == '__main__':
    main()
