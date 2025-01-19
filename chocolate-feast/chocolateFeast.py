
def chocolateFeast(n,c,m):
    bars = int(n/c)
    op = 0
    wrappers = 0
    while bars!=0:
        op += bars
        wrappers += bars
        bars = wrappers//m
        wrappers -= bars*m
    return op 

n, c, m = 15, 3, 2

print(chocolateFeast(n,c,m))
