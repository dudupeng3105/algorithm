import sys
from collections import deque

input = sys.stdin.readline
tc = int(input())


def bfs(r, c):
    global cnt
    q = deque()
    q.append((r, c))
    visited[r][c] = True
    while q:
        o_r, o_c = q.popleft()
        for dr, dc in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
            n_r, n_c = o_r + dr, o_c + dc
            if 0 <= n_r < row and 0 <= n_c < col:
                if not visited[n_r][n_c] and arr[n_r][n_c] != '*':

                    if arr[n_r][n_c] == '.':
                        visited[n_r][n_c] = True
                        q.append((n_r, n_c))

                    elif arr[n_r][n_c].islower():  # 소문자
                        know_key.append(arr[n_r][n_c])
                        arr[n_r][n_c] = '.'  # 갈 수 있는 곳으로 변경
                        return 1

                    else:  # 대문자, 달러
                        if arr[n_r][n_c] == '$':
                            arr[n_r][n_c] = '.'
                            cnt += 1
                            visited[n_r][n_c] = True
                            q.append((n_r, n_c))

                        elif arr[n_r][n_c].lower() in know_key:
                            arr[n_r][n_c] = '.'  # 갈 수 있게 만들어버림
                            visited[n_r][n_c] = True
                            q.append((n_r, n_c))

    return 0


for _ in range(tc):
    row, col = map(int, input().split())
    arr = [list(input().rstrip()) for _ in range(row)]
    know_key = list(input().rstrip())
    cnt = 0
    while True:
        # 가장자리
        flag = 0
        visited = [[False for _ in range(col)] for __ in range(row)]
        for i in range(row):
            if i == 0 or i == row - 1:
                for j in range(col):
                    # 벽이아니거나,,, know_key로 가능
                    if arr[i][j] == '*':
                        continue
                    else:
                        if arr[i][j] == '.':
                            if not visited[i][j]:
                                flag += bfs(i, j) ###
                        else:
                            if arr[i][j].islower():  # 소문자
                                know_key.append(arr[i][j])
                                arr[i][j] = '.'  # 갈 수 있는 곳으로 변경
                                if not visited[i][j]:
                                    flag += bfs(i, j)

                            else:  # 대문자, 달러
                                if arr[i][j] == '$':
                                    arr[i][j] = '.'
                                    cnt += 1
                                    flag += bfs(i, j)

                                elif arr[i][j].lower() in know_key:
                                    if not visited[i][j]:
                                        arr[i][j] = '.'
                                        flag += bfs(i, j)


            else:
                for j in (0, col - 1):
                    # 벽이아니거나,,, know_key로 가능
                    if arr[i][j] == '*':
                        continue
                    else:
                        if arr[i][j] == '.':
                            if not visited[i][j]:
                                flag += bfs(i, j)
                        else:
                            if arr[i][j].islower():  # 소문자
                                know_key.append(arr[i][j])
                                arr[i][j] = '.'  # 갈 수 있는 곳으로 변경
                                if not visited[i][j]:
                                    flag += bfs(i, j)

                            else:  # 대문자, 달러
                                if arr[i][j] == '$':
                                    arr[i][j] = '.'
                                    cnt += 1
                                    flag += bfs(i, j)

                                elif arr[i][j].lower() in know_key:
                                    if not visited[i][j]:
                                        arr[i][j] = '.'
                                        flag += bfs(i, j)

        #flag 판단
        # print(flag)
        # for i in range(row):
        #     print(arr[i])

        if flag:  # 이번턴에서 키를 먹었으면
            continue
        else:
            break  # 더 이상 키를 못 먹음

    print(cnt)