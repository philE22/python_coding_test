"""
n = 세로, m = 가로

d 
0: 북쪽
1: 동쪽
2: 남쪽
3: 서쪽

0이 육지 1이 바다

바라보는 순서
1. 처음 보는 방향의 왼쪽
2. 1의 반대쪽
3. 처음보는 방향
4. 왔던길로 돌아감
"""
n, m = map(int, input().split())
x, y, d = map(int, input().split())
game_map = []

for i in range(n):
    game_map.append(list(map(int, input().split())))

#현재 위치를 바다로 바꿈
game_map[x][y] = 1

#처음 위치는 무조건 들르는 칸이기 때문에 1부터 시작
count = 1

now_x = x
now_y = y

#바라보는 위치의 index계산
move_x = [-1, 0, 1, 0]
move_y = [0, 1, 0, -1]

while True:
    #회전 횟수
    times = 0
    for i in range(4):
        #시작하면 왼쪽 바라봄
        d -= 1
        if d < 0:
            d = 3
        look_x = now_x + move_x[d]
        look_y = now_y + move_y[d]
        
        if game_map[look_x][look_y] == 0:
            now_x = look_x
            now_y = look_y
            game_map[now_x][now_y] = 1
            count += 1
            break
        else:
            times += 1
    #4방향 다 없으면 끝
    if times == 4:
        break

print(count)