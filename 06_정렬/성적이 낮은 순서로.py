times = int(input())
arr = []

for i in range(times):
    input_list = input().split()
    arr.append((input_list[0], int(input_list[1])))
    
arr1 = sorted(arr, key=lambda x: x[1])

for i in arr1:
    print(i[0], end=' ')
