import sys
from collections import deque
input = sys.stdin.readline


def bfs():
    while q_2:
        r, c = q_2.popleft()
        t = sangguen_map[r][c]
        for i in range(4):
            n_r, n_c = r + dr[i], c + dc[i]
            if n_r >= row or n_r < 0 or n_c >= col or n_c < 0:
                return print(t + 1)
            if sangguen_map[n_r][n_c] == -1 and arr[n_r][n_c] != '#'\
                    and fire_map[n_r][n_c] > t + 1:
                sangguen_map[n_r][n_c] = t + 1
                q_2.append((n_r, n_c))

    return print('IMPOSSIBLE')


test_case = int(input())
dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]
for _ in range(test_case):
    col, row = map(int, input().split())
    arr = ['' for __ in range(row)]
    fire_map = [[1000001 for _ in range(col)] for __ in range(row)]
    sangguen_map = [[-1 for _ in range(col)] for __ in range(row)]
    for i in range(row):
        arr[i] = list(input().rstrip())

    q = deque()
    # 불 맵을 일단 bfs로 처리 ㅇㅋ
    for i in range(row):
        for j in range(col):
            if arr[i][j] == '*':
                q.append((i, j))
                fire_map[i][j] = 0

    while q:
        r, c = q.popleft()
        t = fire_map[r][c]
        for i in range(4):
            n_r, n_c = r + dr[i], c + dc[i]
            if (0 <= n_r < row) and (0 <= n_c < col) and\
                    fire_map[n_r][n_c] == 1000001 and arr[n_r][n_c] != '#':
                fire_map[n_r][n_c] = t+1
                q.append((n_r, n_c))

    q_2 = deque()
    for i in range(row):
        flag = 0
        for j in range(col):
            if arr[i][j] == '@':
                q_2.append((i, j))
                sangguen_map[i][j] = 0
                flag = 1
                break
        if flag:
            break

    bfs()