import math
n = int(input())

def func(x):
    arr = []
    for i in range(1, math.sqrt(x) + 1):
        if x % i == 0:
            arr.append(i)
    
    return sum(arr)

result = 0
for i in range(1, n):
    result += func(i)
    
print(result)