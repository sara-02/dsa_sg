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


def hadamard_maultiplication(A, B):
    ra, ca = get_shape(A)
    rb, cb = get_shape(B)
    C = []
    if ra == rb and ca == cb:
        if ra == 0 or ca == 0:
            return C
        if ra == 1:
            C = [x * y for x, y in zip(A, B)]
            return C
        for i in range(ra):
            C.append([0] * cb)
        for i in range(ra):
            for j in range(ca):
                C[i][j] = A[i][j] * B[i][j]
    return C


def print_hadamard(H):
    if len(H) == 0:
        print "Multipcation not possible"
    else:
        print "Hadamard: %s" % H


def main():
    A = [[2, 3], [3, 4]]
    B = [[1, 0], [1, 2]]
    print "\n## For"
    print "A: %s" % A
    print "B: %s" % B
    H = hadamard_maultiplication(A, B)
    print_hadamard(H)
    A = [[1], [2]]
    B = [[2], [3]]
    print "\n## For"
    print "A: %s" % A
    print "B: %s" % B
    H = hadamard_maultiplication(A, B)
    print_hadamard(H)
    A = [1, 2]
    B = [3, 4]
    print "\n## For"
    print "A: %s" % A
    print "B: %s" % B
    H = hadamard_maultiplication(A, B)
    print_hadamard(H)
    A = []
    B = []
    print "\n## For"
    print "A: %s" % A
    print "B: %s" % B
    H = hadamard_maultiplication(A, B)
    print_hadamard(H)

if __name__ == '__main__':
    main()
