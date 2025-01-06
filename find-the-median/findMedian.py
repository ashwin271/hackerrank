
def findMedian(arr):
    hash = {}
    for i in arr: 
        hash[i]=hash.get(i,0)+1
    pos = int((len(arr)+1)/2)
    for key, value in hash.items():
        pos-=value
        if pos<1:
            return key

arr = [0,1,2,4,6,5,3]
print(findMedian(arr))

