# Pangram example
# The quick brown fox jumps over the lazy dog


def check_pangram(string):
    NUM_APLHA = 26
    if len(string) < NUM_APLHA:
        return "String is Not a pangram."

    bucket_count = [0] * NUM_APLHA
    st = string.lower()
    for s in st:
        if s.isalpha():
            bucket_count[ord(s) - 97] += 1
    if all([b >= 1 for b in bucket_count]):
        return "Strings is a  pangram."
    return "Strings is Not a pangrams."


def main():
    string = raw_input("Enter the string:: ")
    print(check_pangram(string))


if __name__ == '__main__':
    main()
