N, M = map(int, input().split())

li = [i for i in range(1, N + 1)]
turns= []
for _ in range(M):
    turns.append(list(map(int, input().split())))

for i, j, k in turns:
    i -= 1
    j -= 1
    k -= 1
    
    box = [0] * N
    for index in range(i, j + 1):
        box[index] = li[index]
    
    for n in range(j - k + 1):
        li[i+n] = box[k + n]
    
    for n in range(k - i):
        li[i + (j - k) + n + 1] = box[i + n]
print(li)