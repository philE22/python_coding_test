T = int(input())

def f(result, arr):
    global count
    
    if  sum(arr) > result: # 해당 숫자 넘어가면 끝냄
        return
    if  sum(arr)== result: #해당 숫자에 도달하면 끝내면서 표시
        count += 1
        return

    for i in range(1, 4):
        arr.append(i)
        f(result, arr)
        arr.pop()


for _ in range(T):
    n = int(input())
    count = 0
    arr = []
    #정수 n을 1, 2, 3의 합으로 나타내는 경우의 수 찾기
    #1부터 시작해서 더하기?
    f(n, arr)
    print(count)
    
