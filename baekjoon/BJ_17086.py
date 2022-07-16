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
                if arr[n_r][n_c]:
                    for i in range(r):
                        print(visited[i])
                    return visited[n_r][n_c] - 2
                q.append((n_r, n_c))

ans = 0
for i in range(r):
    for j in range(c):
        if arr[i][j]:
            temp = bfs(i, j)
            print(temp)
            if temp > ans:
                ans = temp

print(ans)




