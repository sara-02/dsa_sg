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


def find_slope(X, Y):
    n = len(X)
    v1 = sum([x * y for x, y in zip(X, Y)])
    v2 = sum(X)
    v3 = sum(Y)
    v4 = sum([x * x for x in X])
    v5 = v2 * v2
    b = (n * v1 - v2 * v3) / (n * v4 - v5)
    return b


def find_constant(X, Y, m):
    mx = mean_a(X)
    my = mean_a(Y)
    c = my - m * mx
    return c


def predict(X, m, c):
    Y = []
    for x in X:
        y = m * x + c
        Y.append(y)
    return Y


def main():
    print"\n"
    X = [95,
         85,
         80,
         70,
         60]

    Y = [85,
         95,
         70,
         65,
         70]

    m = find_slope(X, Y)
    c = find_constant(X, Y, m)
    X1 = [80]
    Y1 = predict(X1, m, c)
    print Y1
    print"\n"
if __name__ == '__main__':
    main()
