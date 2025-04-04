def funnyString(s):
    for i in range(int(len(s) / 2)):
        if abs(ord(s[i]) - ord(s[i + 1])) != abs(ord(s[-(i + 1)]) - ord(s[-(i + 2)])):
            return "Not Funny"
    return "Funny"


if __name__ == "__main__":
    a = "acxz"
    b = "bcxz"
    print(funnyString(a))
    print(funnyString(b))
