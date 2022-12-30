m = int(input())
n = int(input())
arr =[]

for i in range(m, n+1):
    if i > 1:
        check = True
        for j in range(2, i):
            if i % j == 0:
                check = False
                break
        if check:
            arr.append(i)

if len(arr) > 0:
    print(sum(arr))
    print(min(arr))
else:
    print(-1)