n, m = map(int, input().split())

arr1 = [list(map(int, input().split())) for i in range(m)]
arr2 = [list(map(int, input().split())) for i in range(m)]

result = [[0 for i in range(n)] for j in range(m)]

for i in range(m):
    for j in range(n):
        result[i][j] = str(arr1[i][j] + arr2[i][j])
        
for i in range(m):
    print(" ".join(result[i]))
    
