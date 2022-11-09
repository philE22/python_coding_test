"""
1이 갈 수 있는 길
BFS를 이용
현재 위치에서 갈 수 있는 길을 큐에 담는다
"""
    
from collections import deque


n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

#3번째는 지금까지 이동한 거리
now = [0, 0, 1]
count = 1
move_x = [1, 0, -1, 0]
move_y = [0, 1, 0, -1]

q = deque()
q.append(now)
check = False

while q:
    now = q.popleft()
    if now[0] == n - 1 and now[1] == m - 1:
        print(now[2])
        break
    for i in range(4):
        x = now[0] + move_x[i]
        y = now[1] + move_y[i]
        if x < 0 or x >= n or y < 0 or y >= m or graph[x][y] == 0:
            continue
        else:
            q.append([x, y, now[2] + 1])
    
            
    

