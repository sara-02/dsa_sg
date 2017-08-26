# coding: utf-8
from random import randint


def get_shape(M):
    r = len(M)
    c = 1
    if r <= 0:
        return 0, 0
    if type(M[0]) == list:
        c = len(M[0])
    else:
        r, c = c, r
    return r, c


def check_shape(r, c):
    return r == c


def get_random_r(n):
    R = []
    for i in range(n):
        R.append([randint(0, 1)])
    return R


def multiply_single(M, R, n):
    X = []
    for i in range(n):
        X.append([0])
    for i in range(n):
        for j in range(n):
            X[i][0] += M[i][j] * R[j][0]
    return X


def epoch(k, A, B, C, n):
    P = []
    for i in range(k):
        R = get_random_r(n)
        Cr = multiply_single(C, R, n)
        Br = multiply_single(B, R, n)
        Ar = multiply_single(A, Br, n)
        p = [x[0] - y[0] for x, y in zip(Ar, Cr)]
        P.append(not any(p))
    p_true = sum(P)
    p_false = k - p_true
    if p_true > p_false:
        return True
    return False


def print_result(e):
    if e is not None:
        if e:
            print "Freivalds: Yes"
        else:
            print "Freivalds: No"
    else:
        print "Multipication not possible"


def freivalds(A, B, C, k):
    ra, ca = get_shape(A)
    rb, cb = get_shape(B)
    rc, cc = get_shape(C)
    if check_shape(ra, ca) and check_shape(rb, cb) and check_shape(rc, cc):
        if ra != 0 and (ra == rb and rb == rc):
            return epoch(k, A, B, C, ra)
    return None


def main():
    A = [[2, 3], [3, 0]]
    B = [[1, 0], [1, 2]]
    C = [[6, 5], [8, 7]]
    print "\n## For"
    print "A: %s" % A
    print "B: %s" % B
    print "C: %s" % C
    e = freivalds(A, B, C, 20)
    print_result(e)
    A = [[2, 3], [3, -11]]
    B = [[1, 0], [1, 2]]
    C = [[6, 5], [8, 7]]
    print "\n## For"
    print "A: %s" % A
    print "B: %s" % B
    print "C: %s" % C
    e = freivalds(A, B, C, 20)
    print_result(e)


if __name__ == '__main__':
    main()
