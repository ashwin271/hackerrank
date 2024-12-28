import math

def squares(a, b):
    count = 0
    num = a
    num = int(math.sqrt(num))
    while True:
        sqr = num**2
        if ((sqr>=a)and(sqr<=b)):
            count+=1
        elif(sqr>b):
            break
        num+=1

    return count


print(squares(100, 1000))




