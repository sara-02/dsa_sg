"""
Given n friends, each one can remain single
or can be paired up with some other friend.
Each friend can be paired only once.
Find out the total number of ways
in which friends can remain single or can be paired up.

References:
[1]:https://www.geeksforgeeks.org/friends-pairing-problem/
[2]: http://codrspace.com/sainadhreddy92/friends-pairing-problem/
"""


def pair_recursive(n):
    if n <= 2:
        return n
    else:
        return pair_recursive(n - 1) + (n - 1) * pair_recursive(n - 2)


def pair_dp_full_array(n):
    pair_dp = []
    for i in range(n + 1):
        if i <= 2:
            pair_dp.append(i)
        else:
            pair_dp.append(pair_dp[i - 1] + (i - 1) * pair_dp[i - 2])
    return pair_dp[n]


def pair_dp_vars(n):
    dp_1 = 1
    dp_2 = 2
    if n <= 2:
        return n
    else:
        for i in range(3, n + 1):
            dp_new = dp_2 + (i - 1) * dp_1
            dp_1 = dp_2
            dp_2 = dp_new
        return dp_new

if __name__ == '__main__':
    for i in range(11):
        s = pair_dp_vars(i)
        assert pair_recursive(i) == pair_dp_full_array(i) == s
        print("{}   {}").format(i, s)
