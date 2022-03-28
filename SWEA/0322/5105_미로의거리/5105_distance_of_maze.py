from collections import deque


def bfs():
    while q:
        r, c = q.popleft()
        for i in range(4):
            n_r, n_c = r + dr[i], c + dc[i]
            if 0 <= n_r < n and 0 <= n_c < n and arr[n_r][n_c] != '1' \
                    and dist_map[n_r][n_c] == -1:
                dist_map[n_r][n_c] = dist_map[r][c] + 1
                if n_r == l_r and n_c == l_c:
                    return dist_map[n_r][n_c]
                q.append((n_r, n_c))

    return 0


dr = [0, 0, 1, -1]
dc = [-1, 1, 0, 0]
test_case = int(input())
for tc in range(1, test_case + 1):
    n = int(input())
    arr = [input() for _ in range(n)]
    dist_map = [[-1 for _ in range(n)] for __ in range(n)]
    # 2와 3 찾기
    s_r, s_c = 0, 0
    l_r, l_c = 0, 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] == '2':
                s_r, s_c = i, j
            if arr[i][j] == '3':
                l_r, l_c = i, j

    q = deque()
    q.append((s_r, s_c))
    dist_map[s_r][s_c] = 0
    result = bfs()
    if result:
        print(f'#{tc} {result-1}')
    else:
        print(f'#{tc} 0')
