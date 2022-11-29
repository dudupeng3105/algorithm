import sys
from collections import deque
input = sys.stdin.readline
# 보물섬
# bfs, dfs 상관없을듯
# 최단거리업데이트하면서
# 최단거리 중 최장거리 구하면됨

def bfs(s_r, s_c):
    global ans
    q = deque()
    q.append((s_r, s_c))
    dist[s_r][s_c] = 0
    while q:
        r, c = q.popleft()
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            n_r, n_c = r + dr, c + dc
            if 0 <= n_r < R and 0 <= n_c < C and arr[n_r][n_c] == 'L':
                new_distance = dist[r][c] + 1
                if dist[n_r][n_c] == -1 or new_distance < dist[n_r][n_c]:
                    dist[n_r][n_c] = new_distance
                    ans = max(ans, new_distance)
                    q.append((n_r, n_c))


R, C = map(int, input().split())
arr = [input().rstrip() for _ in range(R)]
dist = [[-1 for _ in range(C)] for __ in range(R)]
ans = 0
for i in range(R):
    for j in range(C):
        if arr[i][j] == 'L':
            cnt = 0
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                temp_i, temp_j = i + dr, j + dc
                if 0 <= temp_i < R and 0 <= temp_j < C and arr[temp_i][temp_j] == 'L':
                    cnt += 1
            if cnt == 1:  # 3면이 막혀있음
                print(i, j)
                bfs(i, j)

# for i in range(R):
#     print(dist[i])

print(ans)