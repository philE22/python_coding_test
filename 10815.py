#계수정렬 풀이
# import sys
# input = sys.stdin.readline

# int(input())
# user_list = list(map(int, input().split()))
# int(input())
# compare_list = list(map(int, input().split()))
# list = [0] * 20000001
# for i in user_list:
#     if i >= 0:
#         list[i] += 1
#     else:
#         list[10000000 - i] += 1
        
# result = []

# for i in compare_list:
#     if i < 0:
#         i = 10000000 - i
#     if list[i] == 1:
#         result.append('1')
#     else:
#         result.append('0')
    
# print(" ".join(result))





#이진 탐색 풀이
def is_exist(arr, num):
    start = 0
    end = len(arr) - 1
    
    while start <= end:
        mid = (end + start) // 2
        #해당 숫자가 배열의 왼쪽에 있을 때
        if arr[mid] == num:
            return True
        #오른쪽에 있을 때
        elif arr[mid] < num:
            start = mid + 1
        else:
            end = mid - 1
        
    return False

int(input())
user_list = list(map(int, input().split()))
int(input())
compare_list = list(map(int, input().split()))
result = []
#유저 카드 정렬
user_list.sort()

for i in compare_list:
    if is_exist(user_list, i):
        result.append('1')
    else:
        result.append('0')

print(" ".join(result))