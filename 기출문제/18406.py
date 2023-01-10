n = input()

arr = list(map(int, n))
arr1 = arr[:len(arr)//2:]
arr2 = arr[len(arr)//2::]

if sum(arr1) == sum(arr2):
    print("LUCKY")
else:
    print("READY")