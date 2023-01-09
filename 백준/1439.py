s = list(input())
count_1 = 0
count_0 = 0
box = s[0]
for i in range(len(s)):
    
    if s[i] != box:
        if box == '0':
            count_0 += 1
        else:
            count_1 += 1
        box = s[i]
        
    if i == (len(s) - 1): #마지막 숫자 세는 역할
        if s[i] == '0':
            count_0 += 1
        else:
            count_1 += 1
        
print(min(count_1, count_0))
