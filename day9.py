# coding: utf-8
from __future__ import division


def transpose(X):
    r = len(X)
    c = len(X[0])
    Xt = []
    for i in range(c):
        temp = []
        for j in range(r):
            temp.append(X[j][i])
        Xt.append(temp)
    return Xt


def multiply(A, B):
    if type(A[0]) != list:
        ca = len(A)
        ra = 1
    else:
        ra = len(A)
        ca = len(A[0])
    if type(B[0]) != list:
        cb = len(B)
        rb = 1
    else:
        rb = len(B)
        cb = len(B[0])
    if ca != rb:
        return
    C = []
    for i in range(ra):
        temp = []
        for j in range(cb):
            s = 0
            for k in range(ca):
                if ra == 1:
                    a = A[k]
                else:
                    a = A[i][k]
                if rb == 1:
                    b = B[k]
                else:
                    b = B[k][j]
                v = a * b
                s = s + v
            temp.append(s)
        C.append(temp)
    return C


""" The following code taken from: https://stackoverflow.com/questions/32114054/matrix-inversion-without-numpy"""
# Stack voerflow code starts


def getMatrixMinor(m, i, j):
    return [row[:j] + row[j + 1:] for row in (m[:i] + m[i + 1:])]


def getMatrixDeternminant(m):
    # base case for 2x2 matrix
    if len(m) == 2:
        return m[0][0] * m[1][1] - m[0][1] * m[1][0]

    determinant = 0
    for c in range(len(m)):
        determinant += ((-1)**c) * m[0][c] * \
            getMatrixDeternminant(getMatrixMinor(m, 0, c))
    return determinant


def getMatrixInverse(m):
    determinant = getMatrixDeternminant(m)
    # special case for 2x2 matrix:
    if len(m) == 2:
        return [[m[1][1] / determinant, -1 * m[0][1] / determinant],
                [-1 * m[1][0] / determinant, m[0][0] / determinant]]

    # find matrix of cofactors
    cofactors = []
    for r in range(len(m)):
        cofactorRow = []
        for c in range(len(m)):
            minor = getMatrixMinor(m, r, c)
            cofactorRow.append(((-1)**(r + c)) * getMatrixDeternminant(minor))
        cofactors.append(cofactorRow)
    cofactors = transpose(cofactors)
    for r in range(len(cofactors)):
        for c in range(len(cofactors)):
            cofactors[r][c] = cofactors[r][c] / determinant
    return cofactors

# Stack overflow code ends


def main():
    X = [[1, 0.18, 0.89],
         [1, 1.0, 0.26],
         [1, 0.92, 0.11],
         [1, 0.07, 0.37],
         [1, 0.85, 0.16],
         [1, 0.99, 0.41],
         [1, 0.87, 0.47]]

    Y = [[109.85],
         [155.72],
         [137.66],
         [76.17],
         [139.75],
         [162.6],
         [151.77]]

    X1 = [[1, 0.49, 0.18],
          [1, 0.57, 0.83],
          [1, 0.56, 0.64],
          [1, 0.76, 0.18]]

    Xt = transpose(X)
    R = multiply(Xt, X)
    R2 = getMatrixInverse(R)
    R3 = multiply(R2, Xt)
    B = multiply(R3, Y)
    Y1 = multiply(X1, B)
    print Y1


if __name__ == '__main__':
    main()
