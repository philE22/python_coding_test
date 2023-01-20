import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())
g = [[INF] * (n + 1) for i in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    if g[a][b] > c:
        g[a][b] = c

#현재 최단 거리인 노드 찾는 함수
def get_smallest_node():
    min_value = INF
    idx = 0
    for i in range(n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            idx = i
    return idx

#i에서 j로 가는 경우 반복
for i in range(1, n + 1):
    #힙큐를 사용하기 위한 설정
    q = []
    heapq.heappush(q, (0, i))
    #최단거리 배열 초기화
    distance = [INF] * (n + 1)
    distance[i] = 0
    #방문여부 배열 초기화
    visited = [False] * (n + 1)
    visited[i] = True
    
    while q:
        # 최단거리인 노드정보 꺼내기
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        
        for j in g[now]:
            cost = dist + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost
                heapq.heappush(q, (cost, j[0]))

    
    distance = distance[1:]
    for j in distance:
        print(j, end=" ")
    print()
