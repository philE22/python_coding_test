N, M = map(int, input().split())
li = [str(i) for i in range(1, N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    
    for i in range((b-a+1)//2):
        tmp = li[b-i]
        li[b-i] = li[a+i]
        li[a+i] = tmp
    
print(" ".join(li))