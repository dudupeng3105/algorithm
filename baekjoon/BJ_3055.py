import sys
from collections import deque

input = sys.stdin.readline


def bfs():
    q = deque()
    q.append((dochi_start[0], dochi_start[1], 0))  # row, col, time
    truth_map = [[False for _ in range(c)] for __ in range(r)]
    truth_map[dochi_start[0]][dochi_start[1]] = True
    while q:
        row, col, time = q.popleft()
        for i in range(4):
            n_row, n_col, n_time = row + dr[i], col + dc[i], time + 1
            if 0 <= n_row < r and 0 <= n_col < c and truth_map[n_row][n_col] == False:
                if forest_map[n_row][n_col] != 'X' and water_map[n_row][n_col] > n_time:
                    if n_row == bieber[0] and n_col == bieber[1]:
                        return n_time
                    else:
                        q.append((n_row, n_col, n_time))
                        truth_map[n_row][n_col] = True

    return 'KAKTUS'


r, c = map(int, input().split())
forest_map = ['' for _ in range(r)]
for i in range(r):
    forest_map[i] = input()

# 물맵 만들고 by bfs
water_map = [[10000 for _ in range(c)] for __ in range(r)]
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

# 물 시작 위치 찾기
water_start = [0, 0]
for i in range(r):
    water_flag = 0
    for j in range(c):
        if forest_map[i][j] == '*':
            water_start = [i, j]
            water_flag = 1
            break
    if water_flag:
        break

# 물이 없을 수도 있음
# 물 bfs, 물 차는 시간 미리 계산해놈
if water_flag:
    q = deque()
    q.append((water_start[0], water_start[1], 0))  # row, col, time
    water_map[water_start[0]][water_start[1]] = 0
    while q:
        row, col, time = q.popleft()
        for i in range(4):
            n_row, n_col, n_time = row + dr[i], col + dc[i], time + 1
            if 0 <= n_row < r and 0 <= n_col < c:
                if forest_map[n_row][n_col] != 'X' and forest_map[n_row][n_col] != 'D' and \
                        water_map[n_row][n_col] == 10000:
                    q.append((n_row, n_col, n_time))
                    water_map[n_row][n_col] = n_time

# 고슴도치 간다
# 고슴도치 위치 찾기
# 물 시작 위치, 비버굴 위치 찾기
dochi_start = [0, 0]
bieber = [0, 0]
for i in range(r):
    flag = 0
    for j in range(c):
        if forest_map[i][j] == 'S':
            dochi_start = [i, j]
            flag = 1
            break
    if flag:
        break

for i in range(r):
    flag = 0
    for j in range(c):
        if forest_map[i][j] == 'D':
            bieber = [i, j]
            water_map[bieber[0]][bieber[1]] = 10000
            flag = 1
            break
    if flag:
        break

# 수달 bfs
print(bfs())