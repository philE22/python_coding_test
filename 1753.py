import sys
import heapq
input = sys.stdin.readline

# V = 노드의 개수, E = 간선의 개수
V, E = map(int, input().split())
# K = 시작 노드
K = int(input())

graph = [[] for i in range(V + 1)]
distance = [int(1e9)] * (V + 1)

for _ in range(E):
    # u에서 v로 가는 가중치 w인 간선
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    
    while q:
        #가장 최단거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        #처리된 적 있는 노드면 무시
        if distance[now] < dist:
            continue
        
        #현재노드와 연결된 노드들 확인
        for togo, d in graph[now]:
            cost = dist + d
            
            #cost가 더 짧은 경우
            if cost < distance[togo]:
                distance[togo] = cost
                heapq.heappush(q, (cost, togo))

dijkstra(K)

for i in distance[1:]:
    if i == int(1e9):
        print("INF")
        continue
    print(i)