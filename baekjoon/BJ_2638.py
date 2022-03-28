from collections import deque
import sys
input = sys.stdin.readline


def bfs():
    q = deque()
    q.append((0, 0))
    truth_map = [[False for _ in range(m)] for __ in range(n)]
    truth_map[0][0] = True

    while q:
        r, c = q.popleft()

        for i in range(4):
            n_r = r + dr[i]
            n_c = c + dc[i]

            if 0 <= n_r < n and 0 <= n_c < m:
                if not truth_map[n_r][n_c]:
                    if arr[n_r][n_c] >= 1:  # 치즈
                        arr[n_r][n_c] += 1
                    else:  # 공기
                        truth_map[n_r][n_c] = True
                        q.append((n_r, n_c))


n, m = map(int, input().split())
arr = [[0 for _ in range(m)] for __ in range(n)]
for i in range(n):
    arr[i] = list(map(int, input().split()))
day = 0

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

while True:
    bfs()
    flag = 0

    for i in range(n):
        for j in range(m):
            if arr[i][j] >= 3:
                arr[i][j] = 0
                flag = 1  # 치즈가 하나라도 녹음
            elif arr[i][j] == 2:  # 공기가 한면만 닿음
                arr[i][j] = 1  # 다시 초기화

    if flag == 1:
        day += 1
    else:
        break

print(day)