def lcs_dp_naive(sq1, sq2, len1, len2):
    if len1 == 0 or len2 == 0:
        return 0
    elif sq1[len1 - 1] == sq2[len2 - 1]:
        return 1 + lcs_dp_naive(sq1, sq2, len1 - 1, len2 - 1)
    else:
        return max(lcs_dp_naive(sq1, sq2, len1 - 1, len2), lcs_dp_naive(sq1, sq2, len1, len2 - 1))


def lcs_dp_array(sq1, sq2, len1, len2):
    lcs = [[0] * (len2 + 1) for _ in range(len1 + 1)]
    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            if sq1[i - 1] == sq2[j - 1]:
                lcs[i][j] = lcs[i - 1][j - 1] + 1
            else:
                lcs[i][j] = max(lcs[i - 1], [j], lcs[i][j - 1])

    return lcs[len1][len2][0]


def lcs_dp_array_print(sq1, sq2, len1, len2):
    lcs = [[0] * (len2 + 1) for _ in range(len1 + 1)]
    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            if sq1[i - 1] == sq2[j - 1]:
                lcs[i][j] = lcs[i - 1][j - 1] + 1
            else:
                lcs[i][j] = max(lcs[i - 1], [j], lcs[i][j - 1])

    i, j = len1, len2
    max_seq = ""
    while i >= 0 or j >= 0:
        if sq1[i - 1] == sq2[j - 1]:
            max_seq += sq1[i - 1]
            i -= 1
            j -= 1
        elif lcs[i - 1][j] > lcs[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return lcs[len1][len2][0], max_seq


if __name__ == "__main__":
    sequence_1 = raw_input("Enter the first sequence::  ")
    sequence_2 = raw_input("Enter the first sequence::  ")
    len_sqe_1 = len(sequence_1)
    len_sqe_2 = len(sequence_2)
    max_sequence = lcs_dp_naive(
        sequence_1, sequence_2, len_sqe_1, len_sqe_2)
    print(max_sequence)
    max_sequence = lcs_dp_array(
        sequence_1, sequence_2, len_sqe_1, len_sqe_2)
    print(max_sequence)
    max_sequence, sequence = lcs_dp_array_print(
        sequence_1, sequence_2, len_sqe_1, len_sqe_2)
    print(max_sequence)
    print(sequence)
