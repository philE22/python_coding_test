import sys
input = sys.stdin.readline

n = int(input())

arr = []
times_arr = [0] * (8001)

for _ in range(n):
    num = int(input())
    arr.append(num)
    if num < 0:
        num = 4000-num
    times_arr[num] += 1

arr.sort()
#산술평균
print(sum(arr) // n)

#중앙값
print(arr[len(arr)//2])

#최빈값
most = max(times_arr)
li = []
for i in range(len(times_arr)):
    if times_arr[i] == most:
        num = i
        if i > 4000:
            num = 4000 - i
        li.append(num)
        
if len(li) != 1:
    li.sort()
    print(li[1])
else:
    print(li[0])

#범위
print(arr[-1] - arr[0])
