N, B = map(int, input().split())
result = ""
for i in range(30, -1, -1):
    if N < B**i and result == "":
        continue

    num = N // (B ** i)

    if num >= 10:
        result += chr(num + 55)
    else:
        result += str(num)

    N -= num *(B ** i)

print(result)