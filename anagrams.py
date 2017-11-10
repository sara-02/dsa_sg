def check_anagram(string1, string2):
    if len(string1) != len(string2):
        return "Lengths don't match, strings are NOT anagrams."
    NUM_APLHA = 26
    bucket_count = [0] * NUM_APLHA
    str1 = string1.lower()
    str2 = string2.lower()
    for s1, s2 in zip(str1, str2):
        bucket_count[ord(s1) - 97] += 1
        bucket_count[ord(s2) - 97] -= 1

    if all([b == 0 for b in bucket_count]):
        return "Strings are anagrams."
    return "Strings are Not anagrams."


def main():
    string1 = raw_input("Enter the frist string:: ")
    string2 = raw_input("Enter the second string:: ")
    print(check_anagram(string1, string2))


if __name__ == '__main__':
    main()
