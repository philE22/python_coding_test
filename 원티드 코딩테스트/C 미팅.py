from itertools import combinations
import sys
input = sys.stdin.readline

n, m, c = map(int, input().split())
 
W = [list(map(int, input().split())) for i in range(c)]
A = list(map(int, input().split()))
B = list(map(int, input().split()))

group_l = []
group_s = []
if len(A) >= len(B):
    group_l = A
    group_s = B
else:
    group_l = B
    group_s = A

result = []

for i in combinations(group_l, len(group_s)):
    box = 0
    for j in range(len(i)):
        box += W[i[j]-1][group_s[j]-1]
    result.append(box)
        
print(max(result))