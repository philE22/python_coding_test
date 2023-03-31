while True:
    n = int(input())
    if n == -1:
        break
    
    li = []
    for i in range(1, n):
        if n % i == 0:
            li.append(i)
            
    if sum(li) == n:
        li = list(map(str, li))
        print(str(n) + " = " + " + ".join(li))
    else:
        print(str(n) + " is NOT perfect.")