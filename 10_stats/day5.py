# coding: utf-8
from __future__ import division
import math


def poisson(l, k):
    v1 = math.pow(l, k)
    v2 = math.pow(math.e, -l)
    v3 = math.factorial(k)
    p = v1 * v2 / v3
    return p


def poisson_atmost(l, k):
    sum = 0
    for i in range(0, k + 1):
        p = poisson(l, i)
        sum += p
    return sum


def ex2(l):
    return l + l * l


def cummulative_normal_dist(x, u, s):
    z = (x - u) / (2 * math.sqrt(2))
    e = math.erf(z)
    d = 0.5 * (1 + e)
    return d

"""
Task
The manager of a industrial plant is planning to buy a machine of either A type or B type . For each day’s operation:

    The number of repairs X, that machine needs is a Poisson random variable with mean 0.88. The daily cost of operating is ca=160+40*x^2.
    The number of repairs Y, that machine needs is a Poisson random variable with mean 1.55. The daily cost of operating is cb=128+40*y^2.

Assume that the repairs take a negligible amount of time and the machines are maintained nightly to ensure that they operate like new at the start of each day. Find and print the expected daily cost for each machine.
"""


def operations():
    machines = ['A', 'B']
    one_time_cost = [160, 128]
    cost_factor = [40, 40]
    mean_repairs = [0.88, 1.05]
    daily_cost = {}
    n = len(machines)
    for i in range(n):
        dc = one_time_cost[i] + cost_factor[i] * ex2(mean_repairs[i])
        mh = machines[i]
        print "## Cost of operation %s is %f" % (mh, dc)


"""
Task
In a certain plant, the time taken to assemble a car is a random variable, X, having a normal distribution with a mean of 20 hours and a standard deviation of 2 hours. What is the probability that a car can be assembled at this plant in:

    Less than hours 19.5?
    Between 20 and 22 hours?

"""


def car_assembly():
    u = 20
    s = 2
    t = 19.5
    at = cummulative_normal_dist(t, u, s)
    t1 = 20
    t2 = 22
    at1 = cummulative_normal_dist(t1, u, s)
    at2 = cummulative_normal_dist(t2, u, s)
    atc = at2 - at1
    print "## The probability of assmebly within 19.5 hours is %f" % at
    print "## The probability of assmebly between 20-22 hours is %f" % atc

"""
Task
The final grades for a Physics exam taken by a large group of students have a mean of 70 and a standard deviation of 10. If we can approximate the distribution of these grades by a normal distribution, what percentage of the students:

    Scored higher than 80?
    Passed the test >=60?
    Failed the test <60?

"""


def grades():
    u = 70
    s = 10
    p1 = 100 * cummulative_normal_dist(60, u, s)
    p2 = 100 - p1
    p3 = 100 * cummulative_normal_dist(60, u, s)
    p4 = 100 - p3
    print "## The percentage of students with >80 is % f" % p4
    print "## The percentage of students with >=60 is %f" % p2
    print "## The percentage of students with <60 is %f" % p1


def main():
    print("\n")
    """
    Task:
    A random variable, X, follows Poisson distribution with mean of 2.5. Find the probability with which the random variable is equal to 5.
    """
    p = poisson(2.5, 5)
    print "## Probability that X=5 is %f" % p
    """
    Task:
    Suppose the average number of lions seen by tourists on a one-day safari is 5. What is the probability that tourists will see fewer than 4 lions on the next one-day safari?
    """
    p = poisson_atmost(5, 3)
    print "## Probability of X<4 is %f" % p
    operations()
    car_assembly()
    grades()
    print("\n")

if __name__ == '__main__':
    main()
