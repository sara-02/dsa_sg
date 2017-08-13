# coding: utf-8
# Mean, Median Mode, Weighted Mean

from __future__ import division
import operator


def sort(a):
    l = len(a)
    for i in range(l):
        for j in range(i + 1, l):
            if a[i] > a[j]:
                a[j], a[i] = a[i], a[j]
    return a


def mean_a(a):
    sum_a = 0
    count = 0
    for i in a:
        sum_a += i
        count += 1
    return sum_a / count


def median_a(a):
    n = len(a)
    if n % 2 == 1:
        pos = int(n / 2)
        med = a[pos]
    else:
        pos = int(n / 2)
        med = a[pos]
        pos += 1
        med += a[pos]
        med = med / 2
    return med


def mode_a(a):
    d = {k: 0 for k in a}
    for i in a:
        d[i] += 1
    sorted_x = sorted(d.items(), key=operator.itemgetter(1, 0), reverse=True)
    max = sorted_x[0][1]
    max_list = []
    k = 0
    while k < len(sorted_x) and sorted_x[k][1] == max:
        max_list.append(sorted_x[k][0])
        k += 1
    return max_list


def weg_mean(a, w):
    sum = 0
    sum_w = 0
    for i, j in zip(a, w):
        sum = sum + i * j
        sum_w += j
    return sum / sum_w


def main():
    array = [64630, 11735, 14216, 99233, 14470,
             4978, 73429, 38120, 51135, 67060]
    sa = []
    sa = sort(array)
    sa
    m = mean_a(sa)
    print "##Mean is %f" % m
    m = median_a(sa)
    print "##Median is %f" % m
    m = mode_a(sa)
    print "##Mode is %s" % m
    a = [10, 40, 30, 50, 20]
    w = [1, 2, 3, 4, 5]
    wm = weg_mean(a, w)
    print "## Weighted mean is %f" % wm

if __name__ == '__main__':
    main()
