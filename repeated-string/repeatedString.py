# Need to find the occurance of a in a string of length n, where the string content is s. 
# So the string s is repeated again and again until it reaches size n.

def repeatedString(s, n):
    l = len(s)
    if n==l: 
        return s.count("a")
    elif n<l: 
        return s[:n+1].count("a")
    else:
        count_in_s = s.count("a")
        times = n//l 
        extra = n%l 
        return (count_in_s * times) + s[:extra].count("a")


s = "aba"
n = 10

print(repeatedString(s, n))
