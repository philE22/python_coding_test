import math

while(True):
    n = int(input())
    if n == 0:
        break

    arr = [1] * (2 * n+1)
    arr[0] = 0
    arr[1] = 0

    for i in range(2, int(math.sqrt(2*n)) + 1):
        for j in range(i * 2, 2*n + 1, i):
            arr[j] = 0
        
    print(sum(arr[n + 1::]))