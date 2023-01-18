n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

result = [arr[0][0]]

for i in range(1, len(arr)):
    #result 배열에 다음 배열인 after을 더함
    after = arr[i]
    new_result = []
    #두가지 경우의 수 중 더 큰걸 선택
    for j in range(len(after)):
        #j-1 인덱스와 j 인덱스의 result와 더해서 둘중 큰 값을 result에 저장
        after_num = after[j]
        
        if j - 1 >= 0:
            result_num1 = result[j - 1] # 이거 예외처리 해줘야함
        else:
            result_num1 = -100
            
        if len(result) - 1 >= j:
            result_num2 = result[j]
        else:
            result_num2 = -100
        
        max_num = max(result_num1, result_num2) + after_num
        new_result.append(max_num)
    
    # result 배열을 새로 만든 배열로 초기화    
    result = new_result
    
print(max(result))