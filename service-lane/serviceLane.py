
def serviceLane(w, c):
    op = []
    for i, j in c:
        op.append(min(w[i:j+1]))
    return op


w = [2, 3, 1, 2, 3, 2, 3, 3]
c = [[0, 3], [4, 6], [6, 7], [3, 5], [0, 7]]

print(serviceLane(w,c))
