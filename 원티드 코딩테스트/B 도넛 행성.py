import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

# bfs로 돌면서 0을 1로 채워나감
move = [[1, 0], [-1, 0], [0, 1], [0, -1]]

def func(arr, i, j): # i가 y축 j가 x축
    q = deque()
    arr[i][j] = 1
    q.append([i, j])
    while q:
        i, j = q.popleft()
        for k in move:
            move_y = i + k[1]
            move_x = j + k[0]
            if move_x < 0:
                move_x = m - 1
            if move_x >= m:
                move_x = 0
            if move_y < 0:
                move_y = n -1
            if move_y >= n:
                move_y = 0
            
            if arr[move_y][move_x] == 0:
                q.append([move_y, move_x])
                arr[move_y][move_x] = 1
                
    

count = 0;
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            func(arr, i, j)
            count += 1

print(count)