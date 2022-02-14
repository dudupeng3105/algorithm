import sys

n, m = map(int, sys.stdin.readline().split())

arr = [[0 for _ in range(m)] for __ in range(n)]
truth_map = [[False for _ in range(m)] for __ in range(n)]

r, c, d = map(int, sys.stdin.readline().split())
if d == 1:
    d = 3
elif d == 3:
    d = 1

for i in range(n):
    arr[i] = list(map(int, sys.stdin.readline().split()))


def direction(num):
    if num == 0:  # 북쪽
        add_x, add_y = 0, -1

    elif num == 1:  # 서
        add_x, add_y = -1, 0

    elif num == 2:  # 남
        add_x, add_y = 0, +1

    else:  # 동(3)
        add_x, add_y = 1, 0

    return add_x, add_y


flag = 1
flag_2 = 0
cnt = 1
while flag:
    truth_map[r][c] = True
    flag_2 = 0
    for i in range(4):
        d = (d + 1) % 4
        dx, dy = direction(d)
        temp_r, temp_c = r + dy, c + dx
        if arr[temp_r][temp_c] == 0 and \
                truth_map[temp_r][temp_c] == False:
            r = temp_r
            c = temp_c
            break
        if i == 3: # 3까지 왔는데 없었으면
            flag_2 = 1

    if flag_2: # 후진 상황
        dx, dy = direction(d)
        r, c = r - dy, c - dx
        if arr[r][c] == 1:
            flag = 0

cnt = 0
for i in range(n):
    for j in range(m):
        if truth_map[i][j]:
            cnt += 1


print(cnt)
