# # 순열 방식
# from itertools import permutations

# n = int(input())
# arr = list(map(int, input().split()))

# result = -1
# length = len(arr)
# for case in permutations(arr, length):
#     box = 0
#     for i in range(length - 1):
#         box += abs(case[i] - case[i + 1])
    
#     result = max(result, box)

# print(result)


#dfs 방식
n = int(input())
arr = list(map(int, input().split()))

result = -1
visited = [False] * n

def dfs(li):
    global result

    if len(li) == n:
        box = 0
        for i in range(n-1):
            box += abs(li[i] - li[i + 1])
        result = max(result, box)
    
    for i in range(n):
        if not visited[i]:
            li.append(arr[i])
            visited[i] = True
            dfs(li)
            visited[i] = False
            li.pop()
dfs([])
print(result)