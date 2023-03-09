from itertools import combinations
N = int(input())
m = [list(map(int, input().split())) for _ in range(N)]

result = 1e9
def diff(start_list, link_list):
    start_box = 0
    link_box = 0
    for i in range(N//2 - 1):
        for j in range(i+1, N//2):
            start_box = start_box + m[start_list[i]][start_list[j]] + m[start_list[j]][start_list[i]]
            link_box = link_box + m[link_list[i]][link_list[j]] + m[link_list[j]][link_list[i]]
    return abs(start_box - link_box)

def dfs(start_list):
    global result
    if len(start_list) == N//2:
        link_list = []
        for i in range(N):
            if i not in start_list:
                link_list.append(i)
        result = min(result, diff(start_list, link_list))
        return
    
    for i in range(N):
        if i in start_list:
            continue
        if len(start_list) > 0 and start_list[len(start_list) - 1] > i:
            continue
        start_list.append(i)
        dfs(start_list)
        start_list.pop()
            
dfs([])
print(result)

## 조합 사용 방식
# members = [i for i in range(N)]
# for half in combinations(members, N//2):
#     li = []
#     for i in range(N):
#         if i not in half:
#             li.append(i)
    
#     sum1 = 0
#     for a, b in combinations(half, 2):
#         sum1 += m[a][b]
#         sum1 += m[b][a]
    
#     sum2 = 0
#     for a, b in combinations(li, 2):
#         sum2 += m[a][b]
#         sum2 += m[b][a]
    
#     result = min(result, abs(sum1 - sum2))
#     if result == 0:
#         break

# print(result)
