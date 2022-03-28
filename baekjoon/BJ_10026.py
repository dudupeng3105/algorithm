from collections import deque
import sys
input = sys.stdin.readline


def bfs(s_r, s_c):
    global color
    q = deque()
    q.append((s_r, s_c))
    truth_map[s_r][s_c] = True
    while q:
        r, c = q.popleft()
        for i in range(4):
            n_r, n_c = r + dr[i], c + dc[i]
            if 0 <= n_r < n and 0 <= n_c < n and truth_map[n_r][n_c] == False:
                if arr[n_r][n_c] == color:
                    truth_map[n_r][n_c] = True
                    q.append((n_r, n_c))


def bfs_2(s_r, s_c):
    global color
    q = deque()
    q.append((s_r, s_c))
    truth_map_2[s_r][s_c] = True
    while q:
        r, c = q.popleft()
        for i in range(4):
            n_r, n_c = r + dr[i], c + dc[i]
            if 0 <= n_r < n and 0 <= n_c < n and truth_map_2[n_r][n_c] == False:
                if color == 'B':
                    if arr[n_r][n_c] == color:
                        truth_map_2[n_r][n_c] = True
                        q.append((n_r, n_c))
                else:  # G, R
                    if not arr[n_r][n_c] == 'B':
                        truth_map_2[n_r][n_c] = True
                        q.append((n_r, n_c))


n = int(input())
arr = ['' for __ in range(n)]
for i in range(n):
    arr[i] = input()

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

region_num = 0
truth_map = [[False for _ in range(n)] for __ in range(n)]
for i in range(n):
    for j in range(n):
        if not truth_map[i][j]:
            color = arr[i][j]
            bfs(i, j)
            region_num += 1

region_num_2 = 0
truth_map_2 = [[False for _ in range(n)] for __ in range(n)]
for i in range(n):
    for j in range(n):
        if not truth_map_2[i][j]:
            color = arr[i][j]
            bfs_2(i, j)
            region_num_2 += 1

print(region_num, region_num_2)



