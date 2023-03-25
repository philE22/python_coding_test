n = int(input())

canvas = [[0] * 100 for _ in range(100)] 
papers = []

for _ in range(n):
    papers.append(list(map(int, input().split())))
    
count = 0

for x, y in papers:
    x -= 1
    y -= 1
    for i in range(10):
        for j in range(10):
            canvas[x + i][y + j] = 1

for i in range(100):
    for j in range(100):
        if canvas[i][j] == 1:
            count += 1
            
print(count)



        