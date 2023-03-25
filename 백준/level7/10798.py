li = []

for _ in range(5):
    li.append(list(input()))

result = ""

for index in range(15):
    for word in li:
        if len(word)-1 < index:
            continue
        else:
            result += word[index]

print(result)