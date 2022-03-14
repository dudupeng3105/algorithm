import sys
from collections import deque

input = sys.stdin.readline


def bfs():
    while q:
        r, c, mode = q.popleft()
        if r == end_r and c == end_c and mode == e_mode:
            return print(dist_map[r][c][mode])
        if mode == 0:  # 가로
            for i in range(5):
                if i == 0:  # 상
                    if r - 1 >= 0 and arr[r - 1][c - 1] != '1' and arr[r - 1][c] != '1' \
                            and arr[r - 1][c + 1] != '1':
                        if dist_map[r - 1][c][mode] == 0:
                            dist_map[r - 1][c][mode] = dist_map[r][c][mode] + 1
                            q.append((r - 1, c, mode))
                elif i == 1:  # 하
                    if r + 1 < n and arr[r + 1][c - 1] != '1' and arr[r + 1][c] != '1' \
                            and arr[r + 1][c + 1] != '1':
                        if dist_map[r + 1][c][mode] == 0:
                            dist_map[r + 1][c][mode] = dist_map[r][c][mode] + 1
                            q.append((r + 1, c, mode))
                elif i == 2:  # 좌
                    if c - 2 >= 0 and arr[r][c - 2] != '1' and arr[r][c - 1] != '1' \
                            and arr[r][c] != '1':
                        if dist_map[r][c - 1][mode] == 0:
                            dist_map[r][c - 1][mode] = dist_map[r][c][mode] + 1
                            q.append((r, c - 1, mode))

                elif i == 3:  # 우
                    if c + 2 < n and arr[r][c + 2] != '1' and arr[r][c + 1] != '1' \
                            and arr[r][c] != '1':
                        if dist_map[r][c + 1][mode] == 0:
                            dist_map[r][c + 1][mode] = dist_map[r][c][mode] + 1
                            q.append((r, c + 1, mode))

                elif i == 4:  # 회전(모드변경 가로->세로, 세로->가로)
                    if r - 1 >= 0 and arr[r - 1][c - 1] != '1' and arr[r - 1][c] != '1' \
                            and arr[r - 1][c + 1] != '1':
                        if r + 1 < n and arr[r + 1][c - 1] != '1' and arr[r + 1][c] != '1' \
                                and arr[r + 1][c + 1] != '1':

                            if dist_map[r][c][1] == 0:
                                dist_map[r][c][1] = dist_map[r][c][mode] + 1
                                q.append((r, c, 1))

        else:  # mode(1) 세로
            for i in range(5):
                if i == 0:  # 상
                    if r - 2 >= 0 and arr[r - 2][c] != '1' and arr[r - 1][c] != '1' \
                            and arr[r][c] != '1':
                        if dist_map[r - 1][c][mode] == 0:
                            dist_map[r - 1][c][mode] = dist_map[r][c][mode] + 1
                            q.append((r - 1, c, mode))
                elif i == 1:  # 하
                    if r + 2 < n and arr[r + 2][c] != '1' and arr[r + 1][c] != '1' \
                            and arr[r][c] != '1':
                        if dist_map[r + 1][c][mode] == 0:
                            dist_map[r + 1][c][mode] = dist_map[r][c][mode] + 1
                            q.append((r + 1, c, mode))
                elif i == 2:  # 좌
                    if c - 1 >= 0 and arr[r + 1][c - 1] != '1' and arr[r][c - 1] != '1' \
                            and arr[r - 1][c - 1] != '1':
                        if dist_map[r][c - 1][mode] == 0:
                            dist_map[r][c - 1][mode] = dist_map[r][c][mode] + 1
                            q.append((r, c - 1, mode))

                elif i == 3:  # 우
                    if c + 1 < n and arr[r + 1][c + 1] != '1' and arr[r][c + 1] != '1' \
                            and arr[r - 1][c + 1] != '1':
                        if dist_map[r][c + 1][mode] == 0:
                            dist_map[r][c + 1][mode] = dist_map[r][c][mode] + 1
                            q.append((r, c + 1, mode))

                elif i == 4:  # 회전(모드변경 가로->세로, 세로->가로)
                    if c - 1 >= 0 and arr[r - 1][c - 1] != '1' and arr[r][c - 1] != '1' \
                            and arr[r + 1][c - 1] != '1':
                        if c + 1 < n and arr[r - 1][c + 1] != '1' and arr[r][c + 1] != '1' \
                                and arr[r + 1][c + 1] != '1':
                            if dist_map[r][c][0] == 0:
                                dist_map[r][c][0] = dist_map[r][c][mode] + 1
                                q.append((r, c, 0))

    return print(0)


n = int(input())
arr = ['' for _ in range(n)]
# (가로모드, 세로모드) * r * c
dist_map = [[[0 for i in range(2)] for i in range(n)] for i in range(n)]
for i in range(n):
    arr[i] = input().rstrip()

# 1. BBB 위치 찾기 (가로모드, 세로모드 구분)
flag = 0
for i in range(n):
    for j in range(n):
        if arr[i][j] == 'B':
            if j + 1 < n and arr[i][j + 1] == 'B':  # b 가로
                start_r, start_c, b_mode = i, j + 1, 0
                flag = 1
                break
            elif i + 1 < n and arr[i + 1][j] == 'B':
                start_r, start_c, b_mode = i + 1, j, 1  # 세로
                flag = 1
                break
    if flag:
        break
# 2. EEE 위치 찾기 (가로모드, 세로모드 구분)
flag = 0
for i in range(n):
    for j in range(n):
        if arr[i][j] == 'E':
            if j + 1 < n and arr[i][j + 1] == 'E':  # E 가로
                end_r, end_c, e_mode = i, j + 1, 0
                flag = 1
                break
            elif i + 1 < n and arr[i + 1][j] == 'E':
                end_r, end_c, e_mode = i + 1, j, 1  # 세로
                flag = 1
                break
    if flag:
        break

q = deque()
q.append((start_r, start_c, b_mode))

bfs()