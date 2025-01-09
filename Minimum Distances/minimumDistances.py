
def minimumDistances(a):
    indx = {}
    for i in range(len(a)):
        if a[i] not in indx.keys():
            indx[a[i]] = [i]
        else:
            indx[a[i]].append(i)

    op = None
    for i in indx.values():
        l = len(i) 
        if l>1:
            for j in range(0, l-1):
                if op is None:
                    op = abs(i[j]-i[j+1])
                elif abs(i[j]-i[j+1])<op:
                    op = abs(i[j]-i[j+1])

    return -1 if op is None else op


a = [7, 1, 3, 4, 1, 7]
print(minimumDistances(a))
