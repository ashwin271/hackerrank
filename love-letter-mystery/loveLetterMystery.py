def loveLetterMystery(s):
    operations = 0
    for i in range(int(len(s) / 2)):
        operations += abs(ord(s[i]) - ord(s[-(i + 1)]))
    return operations


if __name__ == "__main__":
    a = ["abc", "abcba", "abcd", "cba"]

    op = map(loveLetterMystery, a)

    print(list(op))
