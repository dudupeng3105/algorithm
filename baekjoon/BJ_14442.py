import sys
from collections import deque


def bfs():
    dist = [[[0] * m for _ in range(n)] for __ in range(k+1)]
    q = deque()
    q.append((0, 0, 0))
    dist[0][0][0] = 1

    while q:
        wall_broken_num, row, col = q.popleft()
        if row == n - 1 and col == m - 1:
            return dist[wall_broken_num][row][col]
        for i in range(4):
            n_row, n_col = row + dr[i], col + dc[i]
            if 0 <= n_row < n and 0 <= n_col < m:
                if arr[n_row][n_col] == '1':
                    if wall_broken_num < k and dist[wall_broken_num + 1][n_row][n_col] == 0:
                        dist[wall_broken_num + 1][n_row][n_col] = dist[wall_broken_num][row][col] + 1
                        q.append((wall_broken_num + 1, n_row, n_col))
                else:
                    if dist[wall_broken_num][n_row][n_col] == 0:
                        dist[wall_broken_num][n_row][n_col] = dist[wall_broken_num][row][col] + 1
                        q.append((wall_broken_num, n_row, n_col))

    return -1


n, m, k = map(int, sys.stdin.readline().strip().split())
arr = [sys.stdin.readline().strip() for _ in range(n)]
dr = (1, 0, -1, 0)
dc = (0, 1, 0, -1)
print(bfs())


# 3차원배열의 순서에 따라 속도가 달라지는 현상
# 스트링으로 입력