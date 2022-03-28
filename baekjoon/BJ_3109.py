from collections import deque, defaultdict
import sys
input = sys.stdin.readline


def dfs(r, c):
    visited[r][c] = True
    if arr[r][c] == 'x':
        return

    if c == col - 1:
        return 1

    for i in range(3):
        n_r, n_c = r + d[i][0], c + d[i][1]
        if 0 <= n_r < row and 0 <= n_c < col:
            if not visited[n_r][n_c]:
                result = dfs(n_r, n_c)
                if result:
                    return 1


row, col = map(int, input().split())
visited = [[False for _ in range(col)] for __ in range(row)]
arr = [input() for _ in range(row)]
d = [(-1, 1), (0, 1), (1, 1)]
ans = 0
for start_r in range(row):
    temp = dfs(start_r, 0)
    if temp:
        ans += 1
print(ans)