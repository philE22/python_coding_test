from itertools import permutations
import copy
from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(n)]

# 3개의 벽을 세우는 모든 경우의 수를 구하고
# 바이러스가 퍼지게 한  후
# 안전 영역의 크기를 구하고
# 그 중  가장 큰  것을 출력
result = []
move = [(1, 0), (-1, 0), (0, 1), (0, -1)]

#숫자가 num 인 배열의 위치를 리턴해주는 범용 함수
def find_num_idx(g, num):
    arr = []
    for i in range(n):
        for j in range(m):
            if g[i][j] == num:
                arr.append((i,j))
    return arr

   
        
#3개의 벽을 세우는 모든 경우의 수를 구함

nPr = permutations(find_num_idx(g, 0), 3)
for i in nPr:
    print(i)