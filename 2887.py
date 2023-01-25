#최소 신장 트리 알고리즘(크루스칼)을 이용한 문제
#신장 트리란 모든 노드를 포함하면서 사이클이 존재하지 않는 부분 그래프
"""
5
11 -15 -15
14 -5 -15
-1 -1 -5
10 -4 -1
19 -4 19
"""
from itertools import combinations
import sys
input = sys.stdin.readline
#모든 입력 받기
n = int(input())
g = [list(map(int, input().split())) for i in range(n)]

#두 노드 사이 비용 계산하는 함수
def get_cost(a, b):
    a = g[a]
    b = g[b]
    return min(abs(a[0] - b[0]), abs(a[1] - b[1]), abs(a[2] - b[2]))

#모든 노드의 간선 비용을 구해와야함
#간선 배열 초기화 [비용, a행성, b행성]
edges = []
arr = combinations(list(range(n)), 2)

for i in arr:
    a, b = i
    cost = get_cost(a, b)
    edges.append([cost, a, b])

edges.sort(key=lambda x: x[0])

#신장트리 시작
#부모노드 초기화
parent = [0] * (n + 1)
for i in range(n+1):
    parent[i] = i

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a

#비용이 작은 간선들부터 확인하며 사이클이 아니면 추가
result = 0
for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) == find_parent(parent, b):
        continue
    else:
        union_parent(parent, a, b)
        result += cost

print(result)