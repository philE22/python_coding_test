N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
color = ['W', 'B']
index = 0

result = 1e9

for i in range(N-7):
    for j in range(M-7):
        #8 * 8 체스판 다시 칠하는 수 카운트 하기
        count1 = 0
        count2 = 0
        for x in range(8):
            for y in range(8):
                if board[i + x][j + y] != color[index % 2]:
                    count1 += 1
                else:
                    count2 += 1
                index += 1
            index -= 1
        
        result = min(result, count1, count2)
        
print(result)