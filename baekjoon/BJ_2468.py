import sys
from collections import deque

input = sys.stdin.readline


def bfs(a, b):
    q = deque()
    q.append((a, b))
    truth_map[a][b] = True
    while q:
        r, c = q.popleft()
        for i in range(4):
            n_r, n_c = r + dr[i], c + dc[i]
            if 0 <= n_r < n and 0 <= n_c < n and arr[n_r][n_c] > h \
                    and truth_map[n_r][n_c] == False:
                q.append((n_r, n_c))
                truth_map[n_r][n_c] = True


dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]
n = int(input())
arr = [[0 for _ in range(n)] for __ in range(n)]
for i in range(n):
    arr[i] = list(map(int, input().split()))

# max height 구하기
max_height = 0
for i in range(n):
    for j in range(n):
        if arr[i][j] > max_height:
            max_height = arr[i][j]

# 높이 0(비가 안 내릴수도)부터 max_height -1 까지 섬구하기 알고리즘
max_cnt = 0
for h in range(0, max_height):
    truth_map = [[False for _ in range(n)] for __ in range(n)]
    temp_cnt = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] > h and truth_map[i][j] == False:
                bfs(i, j)
                temp_cnt += 1

    if temp_cnt > max_cnt:
        max_cnt = temp_cnt

print(max_cnt)