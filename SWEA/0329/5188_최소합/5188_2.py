test_case = int(input())


def dfs(r, c, depth, temp):
    global ans
    visited[r][c] = True

    if temp > ans:
        return

    if depth == 2 * (n - 1):
        if temp < ans:
            ans = temp
        return

    for dr, dc in [(0, 1), (1, 0)]:
        n_r, n_c = r + dr, c + dc
        if 0 <= n_r < n and 0 <= n_c < n:
            if not visited[n_r][n_c]:
                dfs(n_r, n_c, depth + 1, temp + arr[n_r][n_c])
                visited[n_r][n_c] = False


for tc in range(1, test_case + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [[False for _ in range(n)] for __ in range(n)]
    ans = 9999
    dfs(0, 0, 0, arr[0][0])
    print(f'#{tc} {ans}')