# coding: utf-8
from __future__ import division
import math

""" Suppose a family has children, one of which is a boy. What is the probability that both children are boys?"""


def atleast_1_boy(S):
    total = 0
    boy = 0
    for e in S:
        if "B" in e:
            boy += 1
        total += 1
    return boy / total


def prob_both_boy(S):
    total = 0
    boys = 0
    for e in S:
        if e == "BB":
            boys += 1
        total += 1
    return boys / total


"""You draw cards from a standard -card deck without replacing them. What is the probability that both cards are of the same suit?"""


def combination(n, r):
    a = math.factorial(n)
    b = math.factorial(n - r)
    c = math.factorial(r)
    return a / (b * c)


"""A bag contains red marbles and blue marbles. Then, marbles are drawn from the bag, at random, without replacement. If the first marble drawn is red, what is the probability that the second marble is blue?"""


def marbles():
    pr = 1
    pb = 4 / 6
    prob = pr * pb
    return prob


def main():
    S = {"BB", "GB", "BG", "GG"}
    p1b = atleast_1_boy(S)
    pbb = prob_both_boy(S)
    print "The probability of atleast one boy is %f " % p1b
    print "The probability of both boys %f " % p1b
    prob = pbb / p1b
    assert prob == 1 / 3
    print"The probability of both are boys if one is %f " % prob
    p1 = 1
    p2 = 12 / 51
    p = p1 * p2
    p1_ = combination(4, 1) * combination(13, 2)
    p2_ = combination(52, 2)
    p_ = p1_ / p2_
    assert p_ == p
    print "The probability that both cards are from same deck %f" % p_
    prob = marbles()
    print "The probability that second marble is blue %f" % prob

if __name__ == '__main__':
    main()
