import sys
from collections import deque


def check(r, c):
    flag = 0
    for dr, dc in [(1, 0), (0, -1), (-1, 0), (0, 1)]:
        checked_r, checked_c = r + dr, c + dc
        if arr[checked_r][checked_c] == '#':
            flag = 1
            return flag

    return flag


def bfs():
    adjacent_flag = check(s_r, s_c)
    q = deque()
    q.append((s_r, s_c, adjacent_flag))  # r, c, 벽에인접한칸이였는지..
    dist_map[s_r][s_c] = 0
    while q:
        r, c, adj_flag = q.popleft()
        for dr, dc in [(1, 0), (0, -1), (-1, 0), (0, 1)]:
            n_r, n_c = r + dr, c + dc
            if 0 <= n_r < row and 0 <= n_c < col and arr[n_r][n_c] != '#':
                next_adj_flag = check(n_r, n_c)
                if adj_flag and next_adj_flag:
                    if dist_map[n_r][n_c] > dist_map[r][c]:
                        dist_map[n_r][n_c] = dist_map[r][c]
                        if n_r == l_r and n_c == l_c:
                            return dist_map[n_r][n_c]
                        q.appendleft((n_r, n_c, next_adj_flag))  # 0 - 1 bfs?
                else:
                    if dist_map[n_r][n_c] > dist_map[r][c] + 1:
                        dist_map[n_r][n_c] = dist_map[r][c] + 1
                        if n_r == l_r and n_c == l_c:
                            return dist_map[n_r][n_c]
                        q.append((n_r, n_c, next_adj_flag))
            else:
                continue


input = sys.stdin.readline
row, col = map(int, input().split())
arr = [list(input().strip()) for _ in range(row)]
dist_map = [[50000 for _ in range(col)] for __ in range(row)]

# 시작점 찾기, 종료점 찾기
s_r, s_c = 0, 0
l_r, l_c = 0, 0
for i in range(row):
    for j in range(col):
        if arr[i][j] == 'S':
            s_r, s_c = i, j
        if arr[i][j] == 'E':
            l_r, l_c = i, j

print(bfs())