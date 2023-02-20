import sys
input = sys.stdin.readline

n = int(input())

arr = []
for _ in range(n):
    arr.append(input())

arr = list(set(arr))
arr.sort()
arr.sort(key=lambda x: len(x))

print("".join(arr))