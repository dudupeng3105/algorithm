import sys

input = sys.stdin.readline


def displacement(d):
    if d == 'D':
        return 1, 0
    elif d == 'R':
        return 0, 1
    elif d == 'L':
        return 0, -1
    else:  # U
        return -1, 0


def not_matching(d):
    if d == 'D':
        return 'U'
    elif d == 'R':
        return 'L'
    elif d == 'L':
        return 'R'
    else:  # U
        return 'D'


def dfs(r, c, d):
    global num_path
    visited[r][c] = num_path

    dr, dc = displacement(d)
    not_matching_arrow = not_matching(d)

    n_r, n_c = r + dr, c + dc
    if 0 <= n_r < row and 0 <= n_c < col:
        if visited[n_r][n_c] == -1:
            return

        elif not visited[n_r][n_c]:  # 0(방문한적이없음)
            if arr[n_r][n_c] == not_matching_arrow:  # 반대 방향 화살표와 만난경우
                visited[r][c] = -1  # safe_zone
                return
            else:  # 갈 수 있으면
                dfs(n_r, n_c, arr[n_r][n_c])

        else:
            if visited[n_r][n_c] == num_path:
                visited[n_r][n_c] = -1
                return
            else:
                return


row, col = map(int, input().split())
arr = [input() for _ in range(row)]
visited = [[0 for _ in range(col)] for __ in range(row)]  # 0: false 1~...: true -1: safe_zone

num_path = 1
for i in range(row):
    for j in range(col):
        if not visited[i][j]:
            direction = arr[i][j]
            dfs(i, j, direction)
            num_path += 1

# for i in range(row):
#     print(visited[i])

cnt = 0
for i in range(row):
    for j in range(col):
        if visited[i][j] == -1:
            cnt += 1

print(cnt)
