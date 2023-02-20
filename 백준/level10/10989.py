import sys
input = sys.stdin.readline

arr = [0] * 10001
n = int(input())

for _ in range(n):
    arr[int(input())] += 1
    
for i in range(1, 10001):
    time = arr[i]
    if time > 0:
        for j in range(time):
            print(i)