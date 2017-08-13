# coding: utf-8

from __future__ import division
import math


def combination(n, r):
    a = math.factorial(n)
    b = math.factorial(n - r)
    c = math.factorial(r)
    return a / (b * c)


def binom_atleast(n, r, p, q):
    sum = 0
    for i in range(r, n + 1):
        c = combination(n, i)
        p1 = math.pow(p, i)
        q1 = math.pow(q, (n - i))
        sum += c * p1 * q1
    return sum


def binom_atmost(n, r, p, q):
    sum = 0
    for i in range(0, r + 1):
        c = combination(n, i)
        p1 = math.pow(p, i)
        q1 = math.pow(q, (n - i))
        sum += c * p1 * q1
    return sum


def geometric_dis(n, p, q):
    q1 = math.pow(q, n - 1)
    return q1 * p


def geometric_atleast(n, p, q):
    sum = 0
    for i in range(1, n + 1):
        g = geometric_dis(i, p, q)
        sum = sum + g
    return sum


"""The ratio of boys to girls for babies born in Russia is 1.09/1. If there is child born per birth, what proportion of Russian families with exactly 6 children will have at least 3 boys?"""


def russia():
    p = 1.09 / (1.09 + 1)
    q = 1 / (1.09 + 1)
    n = 6
    r = 3
    s = binom_atmost(n, r, p, q)
    print "## The probability of at least 3 boys in 6 is %f" % s


"""A manufacturer of metal pistons finds that, on average, 12 % of the pistons they manufacture are rejected because they are incorrectly sized. What is the probability that a batch of pistons will contain: 
    No more than 2 rejects?
    At least 2 rejects?
"""


def pistons():
    n = 10
    p = 0.12
    q = 0.88
    r = 2
    pa = binom_atmost(n, r, p, q)
    pb = binom_atleast(n, r, p, q)
    print "## The probability of atmost 2 rejects is % f" % pa
    print "## The probability of at least 2 rejects is % f" % pb


"""The probability that a machine produces a defective product is 1/3. What is the probability that the 1st defect is found during the 5th inspection?"""


def basic_nth(n, p, q):
    qs = 1
    for i in range(1, n):
        qs = qs * q
    return qs * p


def machines(n, p, q):
    n = 5
    p = 1 / 3
    q = 1 - p
    gd = geometric_dis(n, p, q)
    return gd


"""The probability that a machine produces a defective product is 1/3. What is the probability that the 1st defect is found during the first 5 inspection?"""


def basic_first_nth(n, p, q):
    sum = 0
    for i in range(n):
        q1 = math.pow(q, i)
        sum = sum + q1
    return sum * p


def main():
    print("\n")
    russia()
    pistons()
    n = 5
    p = 1 / 3
    q = 2 / 3
    pmb = basic_nth(n, p, q)
    pm = machines(n, p, q)
    assert round(pmb, 6) == round(pm, 6)
    print "## The probability of rejection on 5th trial is %f" % round(pm)
    pmb = basic_first_nth(n, p, q)
    pm = geometric_atleast(n, p, q)
    assert round(pmb, 6) == round(pm, 6)
    print "## The probability of rejection within first 5th trial is %f" % pm
    print("\n")

if __name__ == '__main__':
    main()
