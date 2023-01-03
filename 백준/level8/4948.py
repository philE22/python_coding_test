import math

while(True):
    n = int(input())
    if n == 0:
        break
    if n == 1:
        print(1)
        continue
    
    count = 0
    for i in range(n + 1, n * 2 + 1):
        check = True
        for j in range(2, int(math.sqrt(i)) + 1):
            if i % j == 0:
                check = False
                break
        
        if check:
            count += 1
    
    print(count)