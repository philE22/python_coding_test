n = int(input())
numbers = list(map(int, input().split()))
plus, minus, multi, div = list(map(int, input().split()))

min_value = 1e9
max_value = -1e9

def dfs(i, now):
    global min_value, max_value, plus, minus, multi, div
    
    if i == n:
        min_value = min(min_value, now)
        max_value = max(max_value, now)
    else:
        if plus > 0:
            plus -= 1
            dfs(i + 1, now + numbers[i])
            plus += 1
            
        if minus > 0:
            minus -= 1
            dfs(i + 1, now - numbers[i])
            minus += 1
            
        if multi > 0:
            multi -= 1
            dfs(i + 1, now * numbers[i])
            multi += 1
            
        if div > 0:
            div -= 1
            dfs(i + 1, int(now / numbers[i]))
            div += 1
            
dfs(1, numbers[0])

print(max_value)
print(min_value)