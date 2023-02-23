import sys
input = sys.stdin.readline

int(input())
user_list = list(map(int, input().split()))
int(input())
compare_list = list(map(int, input().split()))
list = [0] * 20000001
for i in user_list:
    if i >= 0:
        list[i] += 1
    else:
        list[10000000 - i] += 1
        
result = []

for i in compare_list:
    if i < 0:
        i = 10000000 - i
    if list[i] == 1:
        result.append('1')
    else:
        result.append('0')
    
print(" ".join(result))