
def equalizeArray(arr):
    count = {}
    for i in arr:
        count[i]=count.get(i, 0) + 1
    print(f"Count Dict: {count}")
    key = None
    maxVal = 0
    for k, v in count.items():
        if v > maxVal:
            key = k
            maxVal = v
    print(f"Max Key: {key}, Max Value: {maxVal}")
    return len(arr)-maxVal

arr = [3,3,2,1,3]
print(equalizeArray(arr))
