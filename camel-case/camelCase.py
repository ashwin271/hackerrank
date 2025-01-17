
def camelcase(s):
    if len(s)!=0:
        n=1
    else:
        n=0

    for i in s:
        if i.isupper():
            n+=1

    return n

s = "saveChangesInTheEditor"

print(camelcase(s))
