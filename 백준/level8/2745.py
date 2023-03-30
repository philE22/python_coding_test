N, B = input().split()
result = 0

for i in range(len(N)):
    s = N[i]
    if str.isdigit(s):
        result += int(s)*int(B)**(len(N) - i - 1)
        continue
    result += (ord(s) - 55)*int(B)**(len(N) - i - 1)
    
print(result)