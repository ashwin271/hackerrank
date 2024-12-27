def cutTheSticks(arr):
    op = []

    while len(arr)>0:
        op.append(len(arr))
        
        smallest=min(arr)
        
        arr = [stick - smallest for stick in arr if stick-smallest>0]

    return op
