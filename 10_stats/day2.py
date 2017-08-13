# coding: utf-8
from __future__ import division


def hcf(a, b):
    m = min(a, b)
    h = 1
    for i in range(1, m + 1):
        if a % i == 0 and b % i == 0:
            h = i
    return h


"""
In a rool of 2 unbaised dice what is the probability of having a sum at most 9
"""


def atmost_9():
    total_count = 0
    condition_count = 0
    for d1 in range(1, 7):
        for d2 in range(1, 7):
            sum = d1 + d2
            if sum <= 9:
                condition_count += 1
            total_count += 1
    h = hcf(total_count, condition_count)
    condition_count = condition_count / h
    total_count = total_count / h
    prob = str(condition_count) + "/" + str(total_count)
    print "Probability is %s " % prob


"""
In a rool of 2 unbaised dice what is the probability of having a sum as 6, when both faces are different
"""


def diff_6():
    total_count = 0
    condition_count = 0
    for d1 in range(1, 7):
        for d2 in range(1, 7):
            sum = d1 + d2
            if sum == 6 and d1 != d2:
                condition_count += 1
            total_count += 1
    h = hcf(total_count, condition_count)
    #     print h
    condition_count = condition_count / h
    total_count = total_count / h
    prob = str(condition_count) + "/" + str(total_count)
    print "Probability is %s " % prob


"""
There are urns labeled , , and .

    Urn contains red balls and black balls.
    Urn contains red balls and black balls.
    Urn contains red balls and black balls.

One ball is drawn from each of the urns. What is the probability that, of the balls drawn, are red and is black?
"""


def prob(u):
    s = u[0] + u[1]
    pa = u[0] / s
    pb = u[1] / s
    return pa, pb


def prob_urn():
    ux = (4, 3)
    uy = (5, 4)
    uz = (4, 4)
    pax, pbx = prob(ux)
    pay, pby = prob(uy)
    paz, pbz = prob(uz)
    c1 = pax * pay * pbz
    c2 = pax * pby * pbz
    c3 = pbx * pay * paz
    p = c1 + c2 + c3
    assert p == (17 / 42)
    print "Probability is 17/42 or %f" % p


def main():
    atmost_9()
    diff_6()
    prob_urn()


if __name__ == '__main__':
    main()
