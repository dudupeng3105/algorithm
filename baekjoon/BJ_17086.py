# 아기 상어

import sys
from collections import deque
input = sys.stdin.readline

r, c = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(r)]

def bfs(row, col):
    q = deque()
    visited = [[0 for _ in range(c)] for __ in range(r)]
    q.append((row, col))
    visited[row][col] = 1

    while q:
        o_r, o_c = q.popleft()
        for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, -1), (-1, 1)]:
            n_r, n_c = o_r + dr, o_c + dc
            if 0 <= n_r < r and 0 <= n_c < c and not visited[n_r][n_c]:
                visited[n_r][n_c] = visited[o_r][o_c] + 1
                # 상어 만나면 끝내면됨(가장 가까이 있는 상어 -> 안전거리)
                if arr[n_r][n_c]:
                    return visited[n_r][n_c] - 1
                q.append((n_r, n_c))

ans = 0
for i in range(r):
    for j in range(c):
        # 0 에서만 출발
        if not arr[i][j]:
            temp = bfs(i, j)
            # 최장 거리 구함
            if temp > ans:
                ans = temp

print(ans)




