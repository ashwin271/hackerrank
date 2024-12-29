
def findMedian(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
        if i>int(len(arr)/2)-1:
            break
    print(f"Sorted Array: {arr}")
    pos = int((len(arr)/2))
    print(f"Median Pos: {pos}")
    return arr[pos]


arr = [0,1,2,4,6,5,3]
print(findMedian(arr))

