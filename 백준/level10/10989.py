import sys
import heapq

input = sys.stdin.readline

n = int(input())
arr = [0] * 10001
for _ in range(n):
    arr[int(input())] += 1
    
for i in range(1, 10001):
    time = arr[i]
    if time > 0:
        for j in range(time):
            print(i)