from itertools import combinations
import copy
from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(n)]
virus_idx = []
wall_idx = []
for i in range(n):
    for j in range(m):
        if g[i][j] == 2:
            virus_idx.append((i,j))
        if g[i][j] == 0:
            wall_idx.append((i,j))

# 3개의 벽을 세우는 모든 경우의 수를 구하고
# 바이러스가 퍼지게 한  후
# 안전 영역의 크기를 구하고
# 그 중  가장 큰  것을 출력
result = 0
move = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def virus(g, start):
    q = deque()
    q.append(start)
    
    while q:
        x, y = q.popleft()
        g[x][y] = 2
        for a, b in move:
            move_x = x + a
            move_y = y + b
            if (move_x >= 0 and move_x < n) and (move_y >= 0 and move_y < m):
                if g[move_x][move_y] == 0:
                    q.append((move_x, move_y))

            


#3개의 벽을 세우는 모든 경우의 수를 구함
nPr = combinations(wall_idx, 3)
for i in nPr:
    copy_g = copy.deepcopy(g)
    #벽 새우기
    for x,y in i:
        copy_g[x][y] = 1

    #바이러스 퍼지기
    for j in virus_idx:
        virus(copy_g, j)
    
    #안전 지역 세기
    count = 0
    for j in copy_g:
        count += j.count(0)
    
    result = max(result, count)
    
print(result)