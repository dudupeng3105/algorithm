w, h = map(int, input().split())
p, q = map(int,input().split())
t = int(input())
tx = t % (2*w)  # x방향 주기 2w
ty = t % (2*h)  # y방향 주기 2h

x = p
time = 0
direction_x = 1
while time != tx:
    time += 1
    x = x + direction_x
    # x 방향 체크
    if x == w or x == 0:  # x 좌표가 양쪽 벽이면 x 변화량 바뀜
        if direction_x == 1:
            direction_x = -1
        else:  # direction_x == -1
            direction_x = 1

y = q
time = 0
direction_y = 1
while time != ty:
    time += 1
    y = y + direction_y
    # y 방향 체크
    if y == h or y == 0:  # y 좌표가 위아래 벽이면 y 변화량 바뀜
        if direction_y == 1:
            direction_y = -1
        else:  # direction_y == -1
            direction_y = 1

print(x, y)