def alternatingCharacters(s):
    deletions, prev = 0, s[0]
    for i in range(1, len(s)):
        if s[i] == prev:
            deletions += 1
        else:
            prev = s[i]
    return deletions


if __name__ == "__main__":
    a = ["AAAA", "BBBBB", "ABABABAB", "BABABA", "AAABBB"]

    op = map(alternatingCharacters, a)

    print(list(op))
