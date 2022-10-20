# 모든 행을 거치면서 해당 행에서 가장 작은 값을 구하고 그중 가장 큰 값이 있는 행을 반환한다

# 각 행을 리스트에 담는다
n, m = map(int, input().split())
row = []
for i in range(n):
    row.append(list(map(int, input().split())))

max = 0;
#행을 돌면서 최소값중 가장 큰값을 찾는다.
for i in row:
    if max < min(i):
        max = min(i)
    
print(max)