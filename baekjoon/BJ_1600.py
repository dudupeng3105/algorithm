import sys
from collections import deque

input = sys.stdin.readline


def bfs():
    while q:
        r, c, cnt = q.popleft()
        # 말 움직임
        for i in range(4):
            n_r, n_c, n_cnt = r + dr[i], c + dc[i], cnt
            if 0 <= n_r < row and 0 <= n_c < col and arr[n_r][n_c] != 1 \
                    and dist_map[n_r][n_c][n_cnt] == 0:
                dist_map[n_r][n_c][n_cnt] = dist_map[r][c][cnt] + 1
                q.append((n_r, n_c, n_cnt))
                if n_r == row - 1 and n_c == col - 1:
                    return print(dist_map[n_r][n_c][n_cnt])

        if cnt < k:
            for i in range(8):
                n_r, n_c, n_cnt = r + horse_dr[i], c + horse_dc[i], cnt + 1
                if 0 <= n_r < row and 0 <= n_c < col and arr[n_r][n_c] != 1 \
                        and dist_map[n_r][n_c][n_cnt] == 0:
                    dist_map[n_r][n_c][n_cnt] = dist_map[r][c][cnt] + 1
                    q.append((n_r, n_c, n_cnt))
                    if n_r == row - 1 and n_c == col - 1:
                        return print(dist_map[n_r][n_c][n_cnt])

    return print(-1)


k = int(input())
col, row = map(int, input().split())
arr = [[0 for _ in range(col)] for __ in range(row)]
dist_map = [[[0 for _ in range(k + 1)] for __ in range(col)] for ___ in range(row)]
for i in range(row):
    arr[i] = list(map(int, input().split()))

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
horse_dr = [2, 2, 1, 1, -1, -1, -2, -2]
horse_dc = [1, -1, 2, -2, 2, -2, 1, -1]

q = deque()
q.append((0, 0, 0))  # r, c, horse_move_cnt
if row == 1 and col == 1:
    print(0)
else:
    bfs()
