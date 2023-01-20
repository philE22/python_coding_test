import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())
g = [[] for i in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    check = True
    for i in g[a]:
        if i[0] == b:
             i[1] = min(i[1], c)
             check = False
    if check:
        g[a].append([b, c])

#현재 최단 거리인 노드 찾는 함수
def get_smallest_node():
    min_value = INF
    idx = 0
    for i in range(n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            idx = i
    return idx

result = []
#i에서 j로 가는 경우 반복
for i in range(1, n + 1):
    #최단거리 배열 초기화
    distance = [INF] * (n + 1)
    distance[i] = 0
    #방문여부 배열 초기화
    visited = [False] * (n + 1)
    visited[i] = True
    #최단 거리 초기화
    for j in g[i]:
        distance[j[0]] = j[1]

    for j in range(n - 1):
        #최단 거리가 가장 짧은 노드를 꺼내서, 방문처리
        now = get_smallest_node()
        visited[now] = True
        
        for k in g[now]:
            cost = distance[now] + k[1]
            
            if distance[k[0]] > cost:
                distance[k[0]] = cost
    
    distance = distance[1:]
    for j in distance:
        print(j, end=" ")
    print()
