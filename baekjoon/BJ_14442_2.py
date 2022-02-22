import sys
from collections import deque


def bfs():
    dist = [[[0] * (k + 1) for _ in range(m)] for __ in range(n)]
    q = deque()
    q.append((0, 0, 0))  # row, col, 벽 부숨 횟수
    dist[0][0][0] = 1  # 방문 및 길이 처리
    while q:
        row, col, wall_broken_num = q.popleft()
        if row == n - 1 and col == m - 1:
            return dist[row][col][wall_broken_num]
        for i in range(4):
            n_row, n_col = row + dr[i], col + dc[i]
            if 0 <= n_row < n and 0 <= n_col < m:
                if arr[n_row][n_col] == '1':
                    if wall_broken_num < k and dist[n_row][n_col][wall_broken_num + 1] == 0:  # 벽이면
                        dist[n_row][n_col][wall_broken_num + 1] = dist[row][col][wall_broken_num] + 1
                        q.append((n_row, n_col, wall_broken_num + 1))
                else:
                    if dist[n_row][n_col][wall_broken_num] == 0:
                        dist[n_row][n_col][wall_broken_num] = dist[row][col][wall_broken_num] + 1
                        q.append((n_row, n_col, wall_broken_num))

    return -1


n, m, k = map(int, sys.stdin.readline().strip().split())
arr = [sys.stdin.readline().strip() for _ in range(n)]
dr = (1, 0, -1, 0)
dc = (0, 1, 0, -1)
# 젤 안쪽 [r][c][0] --> 벽 안부숨 [r][c][1] --> 벽 부숨
print(bfs())