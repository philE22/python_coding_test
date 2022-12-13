import itertools

n, m = map(int, input().split())

# n길이 만큼의 배열 만듦
arr = [i for i in range(1, n+1)]

# 조합 리스트 뽑아서 하나씩 출력
nPr = itertools.permutations(arr, m)
for i in nPr:
    for j in i:
        print(j, end=' ')
    print()
    
    
# """
# 백트래킹이란
#  """
# result=[]
# visited = [False] * (n + 1)
# def permu(num):
#     if num == m:
#         print(' '.join(map(str, result)))
#         return
    
#     for i in range(1, n + 1):
#         if not visited[i]:
#             visited[i] = True
#             result.append(i)
#             permu(num + 1)
#             visited[i] = False
#             result.pop()
            
# permu(0)