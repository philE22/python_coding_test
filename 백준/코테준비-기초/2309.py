"""
9명의 키를 다 더한 후 - 100
반복문으로 2명의 합이 해당하는 숫자가 되는지 찾는다
"""
arr = []

for i in range(9):
    arr.append(int(input()))
    
num = sum(arr) - 100

for i in range(8):
    for j in range(i + 1, 9):
        if((arr[i] + arr[j]) == num):
            a = arr[i]
            b = arr[j]
            arr.remove(a)
            arr.remove(b)
            break
    if(len(arr) == 7):
        break
        
        
arr.sort()
for i in arr:
    print(i)
    
    
#재귀로 풀어보기