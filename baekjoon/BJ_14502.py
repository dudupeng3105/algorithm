import sys
from collections import deque


def bfs():
    q = deque()
    for r, c in virus_lst:
        q.append((r, c))
        truth_map[r][c] = True

    while q:
        row, col = q.popleft()

        for i in range(4):
            n_row, n_col = row + dr[i], col + dc[i]
            if n_row < 0 or n_row > n - 1 or n_col < 0 or n_col > m - 1:  # 맵 범위 밖이거나
                continue
            if truth_map[n_row][n_col]:  # 이미 바이러스거나
                continue
            if arr[n_row][n_col] == 1:  # 벽이거나
                continue
            truth_map[n_row][n_col] = True
            q.append((n_row, n_col))

    # 끝나면 바이러스 개수 셈
    virus_cnt = 0
    for r in range(n):
        for c in range(m):
            if truth_map[r][c]:  # 바이러스면
                virus_cnt += 1

    return virus_cnt


n, m = map(int, sys.stdin.readline().split())
arr = [[0 for _ in range(m)] for __ in range(n)]

for i in range(n):
    arr[i] = list(map(int, sys.stdin.readline().split()))

# 벽 놓을 예비자리 0 찾기
zero_idx_lst = []
virus_lst = []
wall_cnt = 0
for r in range(n):
    for c in range(m):
        if arr[r][c] == 0:
            zero_idx_lst.append((r, c))
        if arr[r][c] == 1:
            wall_cnt += 1
        if arr[r][c] == 2:
            virus_lst.append((r, c))

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

# 벽 놓고 안전지대 확인 반복
length = len(zero_idx_lst)
max_safety_zone = 0
for i in range(length):
    for j in range(i + 1, length):
        for k in range(j + 1, length):
            r_1, c_1 = zero_idx_lst[i]  # 벽 1 위치
            r_2, c_2 = zero_idx_lst[j]  # 벽 2 위치
            r_3, c_3 = zero_idx_lst[k]  # 벽 3 위치
            arr[r_1][c_1] = 1
            arr[r_2][c_2] = 1
            arr[r_3][c_3] = 1
            # bfs 돌리고
            truth_map = [[False for _ in range(m)] for __ in range(n)]
            virus_num = bfs()
            safety_zone = m * n - virus_num - wall_cnt - 3  # 벽 3개 추가했으니까
            max_safety_zone = max(safety_zone, max_safety_zone)
            # 다시 빼고
            arr[r_1][c_1] = 0
            arr[r_2][c_2] = 0
            arr[r_3][c_3] = 0

print(max_safety_zone)
