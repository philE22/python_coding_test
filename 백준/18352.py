from collections import deque
import sys
input = sys.stdin.readline
"""
도시의 개수: n
도로의 개수: m
거리 정보: k
출발 도시의 번호: x
"""
n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    
distance = [-1] * (n + 1)
distance[x] = 0

q = deque([x])

while q:
    now = q.popleft()
    for next_city in graph[now]:
        if distance[next_city] == -1:
            distance[next_city] = distance[now] + 1
            q.append(next_city)

check = True
for i in range(1, n + 1):
    if distance[i] == k:
        print(i)
        check = False
        
if check:
    print(-1)