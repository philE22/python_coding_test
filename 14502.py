from itertools import permutations
import copy
from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(n)]

# 3개의 벽을 세우는 모든 경우의 수를 구하고
# 바이러스가 퍼지게 한  후
# 안전 영역의 크기를 구하고
# 그 중  가장 큰  것을 출력
result = 0
move = [(1, 0), (-1, 0), (0, 1), (0, -1)]

#숫자가 num 인 배열의 위치를 리턴해주는 범용 함수
def find_num_idx(g, num):
    arr = []
    for i in range(n):
        for j in range(m):
            if g[i][j] == num:
                arr.append((i,j))
    return arr

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
def dfs(count):
    global result
    
    if count == 3:
        copy_g = copy.deepcopy(g)
        #바이러스 퍼지기
        arr = find_num_idx(g, 2)
        for j in arr:
            virus(copy_g, j)
        #안전 지역 세기
        count = 0
        for j in copy_g:
            count += j.count(0)
        
        result = max(result, count)
        return
        
    for i in range(n):
        for j in range(m):
            if g[i][j] == 0:
                g[i][j] = 1
                count += 1
                dfs(count)
                g[i][j] = 0
                count -= 1
dfs(0)
print(result)