def libraryFine(d1, m1, y1, d2, m2, y2):
    if y2<y1:
        return 10000
    elif y2>y1:
        return 0 
    elif m2<m1:
        return 500*(m1-m2)
    elif m2>m1:
        return 0
    elif d2<d1:
        return 15*(d1-d2)
    else:
        return 0


return_date = "14,7,2018"
due_date = "5,7,2018"

d1, m1, y1 = list(map(int, return_date.split(",")))

d2, m2, y2 = list(map(int, due_date.split(",")))

print(libraryFine(d1, m1, y1, d2, m2, y2))
