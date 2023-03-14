import copy
from collections import deque

N = int(input())
m = [list(map(int, input().split())) for _ in range(N)]


def bfs(m, x, y, depth):
    move = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        for a, b in move:
            m_x = x + a
            m_y = y + b
            if m_x >= 0 and m_x < N and m_y >= 0 and m_y < N:
                if m[m_x][m_y] > depth:
                    m[m_x][m_y] = 0
                    q.append((m_x, m_y))

def safe_space(depth):
    count = 0
    copy_map = copy.deepcopy(m)
    for x in range(N):
        for y in range(N):
            if copy_map[x][y] > depth:
                copy_map[x][y] = 0
                bfs(copy_map, x, y, depth)
                count += 1
    return count

result = 0
for i in range(101):
    result = max(result, safe_space(i))
    
print(result)