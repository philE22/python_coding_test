from collections import deque

N = int(input())
K = int(input())
apple = []
for _ in range(K):
    apple.append(list(map(int, input().split())))
L = int(input())
turn = []
for _ in range(L):
    x, y = input().split()
    turn.append((int(x), y))
#방향
direction = {
    'U' : (-1, 0),
    'D' : (1, 0),
    'L' : (0, -1),
    'R' : (0, 1)
}
direction_arr = ['U', 'R', 'D', 'L']
#보드 생성
board = [[0] * N for _ in range(N)]
#보드에 사과 입력
for x, y in apple:
    board[x -1][y - 1] = 1
#보드에 뱀 입력
board[0][0] = 2

#뱀의 시작 방향
snake_direction = "R"
snake_head = [0, 0]
snake_tail = [0, 0]
move_history = deque()
count = 0

def direction_change(change, now):
    idx = direction_arr.index(now)
    if change == 'L':
        if (idx - 1) >= 0:
            return direction_arr[idx - 1]
        else:
            return direction_arr[-1]
    else:
        if (idx + 1) < 4:
            return direction_arr[idx + 1]
        else:
            return direction_arr[0]
        

while True:
    # 시간을 확인해서 방향 전환
    for a, b in turn:
        if a == count:
            snake_direction = direction_change(b, snake_direction)
    
    move_history.append(snake_direction)
    #뱀 이동
    snake_head[0] += direction[snake_direction][0]
    snake_head[1] += direction[snake_direction][1]
    
    #이동한 곳에 뱀의 몸이나 벽이 있을 때
    if snake_head[0] >= N or snake_head[0] < 0 or snake_head[1] >= N or snake_head[1] < 0 or board[snake_head[0]][snake_head[1]] == 2 :
    # 반복문을 끝낸다
        break
    
    #이동한 곳에 아무 것도 없을 때
    if board[snake_head[0]][snake_head[1]] == 0:
    #1. 해당 위치를 뱀으로 바꾼다
        board[snake_head[0]][snake_head[1]] = 2
    #2. 꼬리 위치의 보드을 0으로 바꾼다
        board[snake_tail[0]][snake_tail[1]] = 0
    #3. 꼬리 위치를 해당방향으로 한칸 이동 시킨다 -> 꼬리가 이동하는 방향이 틀려질 수 있음
        tail_direction = move_history.popleft()
        snake_tail[0] += direction[tail_direction][0]
        snake_tail[1] += direction[tail_direction][1]
                    
    #이동한 곳에 사과가 있을때
    if board[snake_head[0]][snake_head[1]] == 1:
    #1. 해당 위치를 뱀(2)으로 바꾼다
        board[snake_head[0]][snake_head[1]] = 2
    #2. 꼬리 위치의 보드를 그대로 둔다
    
    
    
    count += 1

print(count + 1)