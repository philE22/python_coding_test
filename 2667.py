from collections import deque

n = int(input())

m = []
for i in range(n):
    m.append(list(map(int, input())))
    
count = 0
result = []
q = deque()
move = [(1, 0), (-1, 0), (0, 1), (0, -1)]

for x in range(n):
    for y in range(n):
        if m[x][y] == 1:
            q.append((x, y))
            m[x][y] = 2
            box = 1
            
            while q:
                a, b = q.popleft()
                m[a][b] = 2

                for m_x, m_y in move:
                    mx = a + m_x
                    my = b + m_y
                    if mx >= 0 and mx < n and my >= 0  and my < n:     
                        if m[mx][my] == 1:
                            q.append((mx, my))
                            m[mx][my] = 2
                            box += 1
                        
            result.append(box)
            count += 1            

            
result.sort()

print(count)
for i in result:
    print(i)