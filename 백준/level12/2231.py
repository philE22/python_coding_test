N = int(input())

for i in range(N + 1):
    s = str(i)
    result = i
    for n in s:
        result += int(n)

    if result == N:
        print(i)
        break
    
    if i == N:
        print("0")