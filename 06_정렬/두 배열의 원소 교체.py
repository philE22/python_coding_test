"""
n은 배열 길이, k는 바꾸기 횟수
A배열은 낮은 숫자 순으로 정렬
B배열은 높은 숫자 순으로 정렬하여
0번 인덱스부터 k까지 바꿈
5 3
1 2 5 4 3
5 5 6 6 5
"""
n, k = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort(reverse=True)

for i in range(k):
    if(A[i] < B[i]):
        A[i], B[i] = B[i], A[i]
        
    else:
        break
    
print(sum(A))