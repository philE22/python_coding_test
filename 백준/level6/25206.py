grade = {"A+":4.5, "A0":4.0, "B+":3.5, "B0":3.0, "C+":2.5, "C0":2.0, "D+":1.5, "D0":1.0, "F":0.0}

a = 0
b = 0
li = []

# while True:
#     try:
#         li.append(list(input().split()))
#     except:
#         break
    
# print(li)

for _ in range(20):
    li.append(list(input().split()))

for subject, point, g in li:
    if g == "P":
        continue
    
    point = float(point)
    
    a += grade[g] * point
    b += point

print(a/b)