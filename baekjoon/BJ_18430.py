import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
checked = [[False for _ in range(m)] for __ in range(n)]

ans = 0


def dfs(power, cnt):
    global ans
    if cnt == n * m:
        if power > ans:
            ans = power
        return

    i = cnt // m
    j = cnt % m

    if not checked[i][j]:
        for case in range(4):

            if case == 0:  # 왼쪽, 아래쪽
                if j - 1 >= 0 and not checked[i][j - 1]:
                    if i + 1 < n and not checked[i + 1][j]:
                        checked[i][j] = True
                        checked[i][j - 1] = True
                        checked[i + 1][j] = True
                        add_score = 2 * arr[i][j] + arr[i][j - 1] + arr[i + 1][j]
                        dfs(power + add_score, cnt + 1)
                        checked[i][j] = False
                        checked[i][j - 1] = False
                        checked[i + 1][j] = False

            elif case == 1:  # 왼쪽, 위쪽
                if j - 1 >= 0 and not checked[i][j - 1]:
                    if i - 1 >= 0 and not checked[i - 1][j]:
                        checked[i][j] = True
                        checked[i][j - 1] = True
                        checked[i - 1][j] = True
                        add_score = 2 * arr[i][j] + arr[i][j - 1] + arr[i - 1][j]
                        dfs(power + add_score, cnt + 1)
                        checked[i][j] = False
                        checked[i][j - 1] = False
                        checked[i - 1][j] = False

            elif case == 2:  # 위쪽, 오른쪽
                if j + 1 < m and not checked[i][j + 1]:
                    if i - 1 >= 0 and not checked[i - 1][j]:
                        checked[i][j] = True
                        checked[i][j + 1] = True
                        checked[i - 1][j] = True
                        add_score = 2 * arr[i][j] + arr[i][j + 1] + arr[i - 1][j]
                        dfs(power + add_score, cnt + 1)
                        checked[i][j] = False
                        checked[i][j + 1] = False
                        checked[i - 1][j] = False

            else:  # 3   # 아래쪽, 오른쪽
                if j + 1 < m and not checked[i][j + 1]:
                    if i + 1 < n and not checked[i + 1][j]:
                        checked[i][j] = True
                        checked[i][j + 1] = True
                        checked[i + 1][j] = True
                        add_score = 2 * arr[i][j] + arr[i][j + 1] + arr[i + 1][j]
                        dfs(power + add_score, cnt + 1)
                        checked[i][j] = False
                        checked[i][j + 1] = False
                        checked[i + 1][j] = False

    dfs(power, cnt + 1)


dfs(0, 0)
print(ans)
