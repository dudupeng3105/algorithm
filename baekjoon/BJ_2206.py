import sys
from collections import deque


def bfs():
    q = deque()
    q.append((0, 0, 0)) # row, col, 벽 부숨 유무
    dist[0][0][0] = 1  # 방문 및 길이 처리
    while q:
        row, col, wall_truth = q.popleft()
        for i in range(4):
            n_row, n_col = row + dr[i], col + dc[i]
            if n_row < 0 or n_row > n - 1 or n_col < 0 or n_col > m - 1:
                continue
            if arr[n_row][n_col]:  # 벽이면
                if wall_truth:  # 벽 부순 적 있으면 더 이상 못 부숨
                    continue
                else:  # 부순적 없음 wall_truth = 0
                    if dist[n_row][n_col][1]:  # 이미 부수고 온 적 있으면
                        continue
                    else:
                        dist[n_row][n_col][1] = dist[row][col][wall_truth] + 1
                        q.append((n_row, n_col, 1))
                        continue
            # 벽 아닐 때
            if dist[n_row][n_col][wall_truth]:  # 이미 경로 있으면
                continue
            if n_row == n - 1 and n_col == m - 1: # 끝나는 조건
                return dist[row][col][wall_truth] + 1

            dist[n_row][n_col][wall_truth] = dist[row][col][wall_truth] + 1
            q.append((n_row, n_col, wall_truth))

    return -1


n, m = map(int, sys.stdin.readline().split())
arr = [[0 for _ in range(m)] for __ in range(n)]
wall_lst = []

for i in range(n):
    arr[i] = list(map(int, sys.stdin.readline().rstrip()))

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

# 젤 안쪽 [r][c][0] --> 벽 안부숨 [r][c][1] --> 벽 부숨
dist = [[[0, 0] for _ in range(m)] for __ in range(n)]
if n == m == 1:
    print(1)
else:
    print(bfs())





