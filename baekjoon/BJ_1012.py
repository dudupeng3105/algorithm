from collections import defaultdict, deque
import sys
input = sys.stdin.readline


def bfs(s_r, s_j):
    q = deque()
    q.append((s_r, s_j))
    truth_map[s_r][s_j] = True
    while q:
        r, c = q.popleft()
        for i in range(4):
            n_r, n_c = r + dr[i], c + dc[i]
            if 0 <= n_r < row and 0 <= n_c < col and arr[n_r][n_c] == 1:
                if not truth_map[n_r][n_c]:
                    truth_map[n_r][n_c] = True
                    q.append((n_r, n_c))


test_case = int(input())
for _ in range(test_case):
    row, col, cabbage_num = map(int, input().split())
    arr = [[0 for _ in range(col)] for __ in range(row)]
    # 배추심기
    for _ in range(cabbage_num):
        cabbage_r, cabbage_c = map(int, input().split())
        arr[cabbage_r][cabbage_c] = 1

    dr = [1, 0, -1, 0]
    dc = [0, 1, 0, -1]
    truth_map = [[False for _ in range(col)] for __ in range(row)]
    ans = []
    cnt = 0
    for i in range(row):
        for j in range(col):
            if arr[i][j] == 1 and truth_map[i][j] == False:
                cnt += 1
                bfs(i, j)

    print(cnt)
