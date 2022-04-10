from collections import deque


def bfs():
    q = deque()
    q.append((0, 0, arr[0][0]))  # r, c, height
    dist_map[0][0] = 0
    while q:
        r, c, height = q.popleft()
        for i in range(n):
            print(dist_map[i])
        print('--------------------')
        for dr, dc in [(1, 0), (0, -1), (0, 1), (-1, 0)]:
            n_r, n_c = r + dr, c + dc
            if 0 <= n_r < n and 0 <= n_c < n:
                if arr[n_r][n_c] > height:
                    if dist_map[r][c] + (arr[n_r][n_c] - height) + 1 < dist_map[n_r][n_c]:
                        dist_map[n_r][n_c] = dist_map[r][c] + (arr[n_r][n_c] - height) + 1
                        q.append((n_r, n_c, arr[n_r][n_c]))
                else:
                    if dist_map[r][c] + 1 < dist_map[n_r][n_c]:
                        dist_map[n_r][n_c] = dist_map[r][c] + 1
                        q.append((n_r, n_c, arr[n_r][n_c]))


test_case = int(input())
for tc in range(1, test_case + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    dist_map = [[99999999 for _ in range(n)] for __ in range(n)]
    bfs()
    print(f'#{tc} {dist_map[n-1][n-1]}')
