# 인구이동

import sys
from collections import deque

input = sys.stdin.readline


def bfs(row, col):
    global cnt, l, r
    q = deque()
    result_sum, result_num = 0, 0
    q.append((row, col))
    visited[row][col] = cnt
    result_num += 1
    result_sum += arr[row][col]
    while q:
        o_r, o_l = q.popleft()
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            n_r, n_c = o_r + dr, o_l + dc
            if 0 <= n_r < n and 0 <= n_c < n:
                if l <= abs(arr[n_r][n_c] - arr[o_r][o_l]) <= r:
                    if not visited[n_r][n_c]:
                        visited[n_r][n_c] = cnt
                        result_num += 1
                        result_sum += arr[n_r][n_c]
                        q.append((n_r, n_c))

    return result_sum, result_num


n, l, r = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
turn = 0
# bfs, cnt, flag
while True:
    visited = [[0 for _ in range(n)] for __ in range(n)]
    cnt = 1
    population = [0]  # union_sum // num 담음 (바뀔 수)
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                union_sum, union_num = bfs(i, j)
                population.append(union_sum // union_num)
                cnt += 1

    # for i in range(n):
    #     print(arr[i])
    # print()

    if (cnt - 1) == n * n:  # 연합이 없으면 끝난거임
        print(turn)
        break

    # 값 바꿔 버리기
    for i in range(n):
        for j in range(n):
            arr[i][j] = population[visited[i][j]]

    turn += 1
