from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
S, X, Y = map(int, input().split())

#해당 바이러스의 위치를 찾아서 초기화
virus_idx = []
for i in range(N):
    for j in range(N):
        if arr[i][j] != 0:
            virus_idx.append([arr[i][j], (i, j)])

virus_idx.sort(key = lambda x : x[0])
q = deque(virus_idx)
q.append('count')
print(q)

#바이러스가 퍼지는 메서드
m = [(1, 0), (-1, 0), (0, 1), (0, -1)]
def virus(idx, arr, v):
    for x, y in m:
        move_x = x + idx[0]
        move_y = y + idx[1]
        
        if move_x >= 0 and move_x < N and move_y >= 0 and move_y < N:
            if arr[move_x][move_y] == 0:
                arr[move_x][move_y] = v
                q.append([v, (move_x, move_y)])


#S초 동안 진행
for _ in range(S):
    while True:
        idx = q.popleft()
        if idx == 'count':
            q.append('count')
            break
        virus(idx[1], arr, idx[0])

print(arr[X-1][Y-1])