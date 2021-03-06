import sys
from collections import deque

input = sys.stdin.readline


def bfs():
    while q:
        r, c = q.popleft()
        for i in range(4):
            n_r, n_c = r + dr[i], c + dc[i]
            if 0 <= n_r < n and 0 <= n_c < n:  # 맵 범위 안이고
                if truth_map[n_r][n_c]:  # 방문한적있음
                    if arr[n_r][n_c] == '0':  # 검은방이면 
                        # 방문한적 있으니까 broken_map[n_r][n_c]는 -1이 아님
                        if broken_map[n_r][n_c] <= broken_map[r][c] + 1:
                            continue
                        else:
                            q.append((n_r, n_c))
                            broken_map[n_r][n_c] = broken_map[r][c] + 1

                    else:  # 검은방 아니면
                        if broken_map[n_r][n_c] <= broken_map[r][c]:
                            continue
                        else:
                            q.append((n_r, n_c))
                            # 벽 안부수니까 전에 위치에서의 값이랑 같음
                            broken_map[n_r][n_c] = broken_map[r][c]

                else:  # 방문한 적 없음
                    if arr[n_r][n_c] == '0':  # 검은방이면
                        q.append((n_r, n_c))
                        truth_map[n_r][n_c] = True
                        # 부수고 감
                        broken_map[n_r][n_c] = broken_map[r][c] + 1

                    else:  # 벽 아니면
                        q.append((n_r, n_c))
                        truth_map[n_r][n_c] = True
                        broken_map[n_r][n_c] = broken_map[r][c]


n = int(input())
arr = ['' for _ in range(n)]
for i in range(n):
    arr[i] = input().rstrip()

truth_map = [[False for _ in range(n)] for __ in range(n)]
broken_map = [[-1 for _ in range(n)] for __ in range(n)]  # dist_map같은 느낌
q = deque()
q.append((0, 0))
truth_map[0][0] = True
broken_map[0][0] = 0

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
bfs()
print(broken_map[n-1][n-1])
