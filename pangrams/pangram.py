def pangrams(s):
    return "pangram" if len(set("".join(s.split()).lower())) == 26 else "not pangram"


if __name__ == "__main__":
    a = "Hello my name is ashwin"
    print(pangrams(a))
