import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)


def dfs(r, c, depth):
    global ans

    if arr[r][c] == 'H':  # 구멍이면
        if depth > ans:
            ans = depth
        return

    visited[r][c] = True

    step_size = int(arr[r][c])
    for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        n_r, n_c = r + step_size * dr, c + step_size * dc
        if not (0 <= n_r < row and 0 <= n_c < col):  # 범위 밖이면
            if depth + 1 > ans:
                ans = depth + 1
            continue

        if visited[n_r][n_c]:  # 방문했던곳이면(싸이클 만들어짐)
            ans = -1
            return -1

        else:  # 방문한 적 없음
            if depth + 1 > dp[n_r][n_c]:
                dp[n_r][n_c] = depth + 1
                result = dfs(n_r, n_c, depth + 1)
                visited[n_r][n_c] = False
                if result:
                    return -1
            else:
                continue


row, col = map(int, input().split())
arr = [input() for _ in range(row)]

ans = 0
visited = [[False for _ in range(col)] for __ in range(row)]
dp = [[0 for _ in range(col)] for __ in range(row)]

cycle = dfs(0, 0, 0)
if cycle:
    print(cycle)
else:
    print(ans)