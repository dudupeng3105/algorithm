def check(x):
    for i in range(x):
        if rows[x] == rows[i] or abs(rows[x] - rows[i]) == x - i:
            return False
    return True


def dfs(x):
    global cnt

    if x == n:
        cnt += 1
        return

    for i in range(n):
        if visited[i]:
            continue

        rows[x] = i
        if check(x):
            visited[i] = True
            dfs(x+1)
            visited[i] = False


test_case = int(input())
for tc in range(1, test_case+1):
    n = int(input())
    rows = [0] * n
    visited = [False] * n
    cnt = 0

    dfs(0)
    print(f'#{tc} {cnt}')