import sys
input = sys.stdin.readline

n = int(input())

#다이나믹 프로그래밍?
# 점화식으로 푸는건가?
#기존에 계산한 값과 뒤에 이어지는 값의 합으로 했을때 무엇이 나을지
# 1 1 2 1 2 1 1 1 2 2 1
#-> 2 -1 1 -1 3 -2 1
# 처음부터 끝까지 순회 한다고했을때
# 지금까지의 점수, 중간에 - 되는 점수, 그 이후에 더해질 점수
# a, b, c라고하면
# 3, -2, 6, -4, 2, -1, 3
arr = list(map(int, input().split()))

# 배열에서 왼쪽과 오른쪽이 연속적으로 있으면 합쳐서 배열로 만드는 과정
if arr[0] == 1:
    box = 1
else:
    box = -1
status = arr[0]

result = []
for i in arr[1:]:
    if status == i:
        if i == 1:
            box += 1
        else:
            box -= 1
    else:
        result.append(box)
        status = i
        if i == 1:
            box = 1
        else:
            box = -1
result.append(box)

# 배열이 음수로 시작하면 자르는 과정
if result[0] <= 0:
    result = result[1:]

print(result)
# 양수 음수 양수가 있을때
# a, b, c
# a+b+c, c 중에 더 큰애로 고름
# + - + - + - + - + -

if len(result) <= 2:
    print(result[0])
else:
    point = result[0]
    for i in range(1, len(result)-1, 2):
        point = max(point + result[i] + result[i+1], result[i+1])
    print(point)

    