def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return x

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a
    
#노드의 개수와 간선의 개수 받기
v, e = map(int, input().split())

#부모테이블 초기화
parent = [0] * (v + 1)

for i in range(1, v + 1):
    parent[i] = i
    
cycle = False

for i in range(e):
    a, b = map(int, input().split())
    
    #두 노드의 부모가 같으면 사이클 발생했다는 의미
    if find_parent(parent, a) == find_parent(parent, b):
        cycle = True
        break
    else:
        union_parent(parent, a, b)

print(parent)
if cycle: print("사이클이 발생했습니다.")
else: print("사이클이 발생하지 않았습니다.")

#하지만 이렇게될 경우 확인하는 간선의 순서에 따라 사이클인지 아닌지가 달라진다.