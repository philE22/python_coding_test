T = int(input())

min_x = 1e9
max_x = -1e9
min_y = 1e9
max_y = -1e9

for _ in range(T):
    x, y = map(int, input().split())
    min_x = min(x, min_x)
    max_x = max(x, max_x)
    min_y = min(y, min_y)
    max_y = max(y, max_y)
    
print((max_x - min_x) * (max_y - min_y))