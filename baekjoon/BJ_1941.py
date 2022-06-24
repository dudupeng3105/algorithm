import sys

input = sys.stdin.readline

arr = [input().rstrip() for _ in range(5)]
# 7명
# 인접해야함
# S가 4개 이상
# 오른쪽, 아래 탐색
dr = [0, 1]
dc = [1, 0]


def dfs(r, c, depth, y_cnt, visited):
    global cnt
    print(r, c)
    if y_cnt > 3:
        return
    if depth == 7:
        cnt += 1
        print("답", visited)
        return

    # 들어가기
    n_r, n_c = r + dr[0], c + dc[0]
    if 0 <= n_r < 5 and 0 <= n_c < 5:
        if [n_r, n_c] not in visited:
            if arr[n_r][n_c] == 'Y':
                dfs(n_r, n_c, depth + 1, y_cnt + 1, visited + [[n_r, n_c]])
            else:
                dfs(n_r, n_c, depth + 1, y_cnt, visited + [[n_r, n_c]])

    n_r, n_c = r + dr[1], c + dc[1]
    if 0 <= n_r < 5 and 0 <= n_c < 5:
        if [n_r, n_c] not in visited:
            if arr[n_r][n_c] == 'Y':
                dfs(n_r, n_c, depth + 1, y_cnt + 1, visited + [[n_r, n_c]])
            else:
                dfs(n_r, n_c, depth + 1, y_cnt, visited + [[n_r, n_c]])

    return


cnt = 0
# for i in range(5):
#     for j in range(5):
if arr[1][0] == 'Y':
    dfs(1, 0, 1, 1, [[1, 0]])
else:
    dfs(1, 0, 1, 0, [[1, 0]])

print(cnt)
