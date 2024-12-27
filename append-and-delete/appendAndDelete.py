def appendAndDelete(s, t, k):
    s_len = len(s)
    t_len = len(t)
    cont_same_count = 0

    # Find the length of the common prefix
    for i in range(min(s_len, t_len)):
        if s[i] == t[i]:
            cont_same_count += 1
        else:
            break

    # Minimum operations needed to convert s to t
    diff = (s_len + t_len) - (2 * cont_same_count)

    # Check if the conversion is possible
    if diff > k:
        return "No"
    elif (k - diff) % 2 == 0 or k >= (s_len + t_len):
        return "Yes"
    else:
        return "No"
