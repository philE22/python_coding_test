from collections import deque

N, M = map(int, input().split())
m = [list(map(int, input())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
move = [(1, 0), (-1, 0), (0, 1), (0, -1)]
q = deque()
q.append((0, 0, 0))
visited[0][0] = True

while q:
    x, y, count = q.popleft()
    
    if x == N - 1 and y == M - 1:
        print(count + 1)
        break
    
    for a, b in move:
        m_x = x + a
        m_y = y + b
        if m_x >= 0 and m_x < N and m_y >= 0 and m_y < M:
            if visited[m_x][m_y] == False:
                if m[m_x][m_y] == 1:
                    q.append((m_x, m_y, count + 1))
                    visited[m_x][m_y] = True
        
