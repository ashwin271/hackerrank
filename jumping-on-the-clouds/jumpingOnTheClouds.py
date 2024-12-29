
def jumpingOnClouds(c):
    n = len(c)
    jumps = 0
    i=0
    while i<n:
        if i+1==n-1 or i+2==n-1:
            jumps+=1
            break
        if i==n-1:
            break
        # Jumping Logic
        if c[i+2]==0:
            i+=2
        else:
            i+=1
        jumps+=1
    return jumps


c1 = [0,0,1,0,0,1,0]
c2 = [0,0,0,1,0,0]


print(jumpingOnClouds(c1))
print(jumpingOnClouds(c2))
