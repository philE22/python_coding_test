import sys
from collections import deque

n = int(input())
m = int(input())

connect = [[] for _ in range(n + 1)]
needs = [[0] * (n + 1) for _ in range(n + 1)]
q = deque()
degree = [0] * (n + 1)

for _ in range(m):
    a,b,c = map(int, input().split())
    connect[b].append((a, c))
    degree[a] += 1

for i in range(1, n + 1):
    if degree[i] == 0:
        q.append(i)
    
while q:
    now = q.popleft()
    #현 제품의 다음 번호, 현 제품이 얼마나 필요한지
    for next_pd, next_need in connect[now]:
        #현 제품이 기본 부품이면
        if needs[now].count(0) == n + 1:
            needs[next_pd][now] += next_need
        else:
            for i in range(1, n + 1):
                needs[next_pd][i] += needs[now][i] * next_need
        
        degree[next_pd] -= 1
        if degree[next_pd] == 0:
            q.append(next_pd)

result = list(enumerate(needs[n]))[1:]
for x, y in result:
    if y > 0:
        print(x, y)

