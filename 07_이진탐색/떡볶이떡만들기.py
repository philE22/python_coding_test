"""
중간을 자르고 총합이 원하는 길이보다 길면 오른쪽에서 중간을 자름
짧으면 왼쪽에서 중간을 자름
4 6
19 15 10 17
"""

n, m = map(int, input().split())

arr = list(map(int, input().split()))

start = 0
end = max(arr)

result = 0
while (start <= end):
    middle = (start + end)//2
    total = sum([dduk - middle for dduk in arr if (dduk - middle) > 0])
    
    # 총합이 원하는 것보다 크면 높이를 높게
    if total >= m:
        #크면 조건에 충족하는 것이므로 기록
        result = middle
        start = middle + 1
    # 총합이 작으면 높이를 낮게
    else:
        end = middle - 1
        
print(result)
