def euclid_gcd(A, B):
    if B == 0:
        return A
    if A > B:
        A = A - B
        return euclid_gcd(A, B)
    else:
        B = B - A
        return euclid_gcd(A, B)


def check_num(n):
    return abs(n)


def main():

    gcd = euclid_gcd(check_num(-2), check_num(-4))
    assert gcd == 2
    gcd = euclid_gcd(8, 4)
    assert gcd == 4
    gcd = euclid_gcd(9, 13)
    assert gcd == 1


if __name__ == '__main__':
    main()
