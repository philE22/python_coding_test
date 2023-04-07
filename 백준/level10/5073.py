while True:
    li = sorted(list(map(int, input().split())))
    if li[0] == 0:
        break
    s = set(li)
    
    if li[2] >= li[0] + li[1]:
        print("Invalid")
        continue
    
    if len(s) == 2:
        print("Isosceles")
        continue
    if len(s) == 1:
        print("Equilateral")
        continue
    if len(s) == 3:
        print("Scalene")
        continue