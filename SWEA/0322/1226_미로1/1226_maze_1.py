from collections import deque


def bfs():
    while q:
        r, c = q.popleft()
        for i in range(4):
            n_r, n_c = r + dr[i], c + dc[i]
            if 0 <= n_r < 16 and 0 <= n_c < 16 and arr[n_r][n_c] != '1' \
                    and truth_map[n_r][n_c] == False:
                truth_map[n_r][n_c] = True
                if n_r == l_r and n_c == l_c:
                    return 1  # True
                q.append((n_r, n_c))

    return 0


dr = [0, 0, 1, -1]
dc = [-1, 1, 0, 0]
for _ in range(10):
    tc = int(input())
    arr = [input() for _ in range(16)]
    truth_map = [[False for _ in range(16)] for __ in range(16)]
    # 2와 3 찾기
    s_r, s_c = 0, 0
    l_r, l_c = 0, 0
    for i in range(16):
        for j in range(16):
            if arr[i][j] == '2':
                s_r, s_c = i, j
            if arr[i][j] == '3':
                l_r, l_c = i, j

    q = deque()
    q.append((s_r, s_c))
    truth_map[s_r][s_c] = True
    result = bfs()
    print(f'#{tc} {result}')