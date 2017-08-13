# coding: utf-8

# Standard deviation
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


# Quartiles
def sort(a):
    l = len(a)
    for i in range(l):
        for j in range(i + 1, l):
            if a[i] > a[j]:
                a[j], a[i] = a[i], a[j]
    return a


def split(a):
    n = len(a)
    p = int(n / 2)
    if n % 2 == 0:
        ua = a[p:]
    else:
        ua = a[p + 1:]
    la = a[:p]
    return la, ua


def median_a(a):
    n = len(a)
    if n % 2 == 1:
        pos = int(n / 2) - 1
        med = a[pos]
    else:
        pos = int(n / 2) - 1
        med = a[pos]
        pos += 1
        med += a[pos]
        med = med / 2
    return med


def main():
    a = [10, 40, 30, 50, 20]
    sd = std(a)
    print "\n## Standard Deviation is %f\n" % sd
    a = [3, 7, 8, 5, 12, 14, 21, 13, 18]
    a = sort(a)
    la, ua = split(a)
    q1 = median_a(la)
    q3 = median_a(ua)
    m = median_a(a)
    print "## Lower Quartile is %f" % q1
    print "## Median is %f" % m
    print "## Upper Quartile is %f" % q3
    # Interquartile range
    ir = q3 - q1
    print "## Inter Quartile range is %f" % ir
    qd = ir / 2
    coeff_qd = (q3 - q1) / (q3 + q1)
    print "## Quartile Deviation is %f" % qd
    print "## Coefficient of Quartile Deviation is %f" % coeff_qd
    lower_fence = q1 - 1.5 * ir
    upper_fence = q3 + 1.5 * ir
    print "## Lower Inner Fence is %f" % lower_fence
    print "## Upper Inner Fence is %f" % upper_fence
    lower_fence = q1 - 3 * ir
    upper_fence = q3 + 3 * ir
    print "## Lower Outer Fence is %f" % lower_fence
    print "## Upper Outer Fence is %f\n" % upper_fence


if __name__ == '__main__':
    main()
