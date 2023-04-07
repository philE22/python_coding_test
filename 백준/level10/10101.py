li = []
for _ in range(3):
    li.append(int(input()))
    
if sum(li) != 180:
    print("Error")
else:
    s = set(li)
    if len(s) == 3:
        print("Scalene")
    elif len(s) == 2:
        print("Isosceles")
    elif len(s) == 1:
        print("Equilateral")