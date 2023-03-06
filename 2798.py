N, M = map(int, input().split())
cards = list(map(int, input().split()))
result = -1
li = []
def dfs(li):
    global result
    if len(li) == 3:
        if sum(li) <= M:
            result = max(result, sum(li))
        return
    for card in cards:
        if card in li:
            continue
        li.append(card)
        dfs(li)
        li.pop()

dfs(li)

print(result)

# 조합 방식
# from itertools import combinations

# N, M = map(int, input().split())
# cards = list(map(int, input().split()))

# result = -1
# for li in combinations(cards, 3):
#     if sum(li) <= M:
#         result = max(result, sum(li))
    
# print(result)