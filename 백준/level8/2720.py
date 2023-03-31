T = int(input())
li = [25, 10, 5, 1]
for _ in range(T):
    result = []
    C = int(input())
    for coin in li:
        result.append(str(C // coin))
        C = C % coin

    print(" ".join(result))
    