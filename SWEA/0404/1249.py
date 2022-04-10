from collections import deque

test_case = int(input())
for tc in range(1, test_case+1):
    n = int(input())
    arr = [list(map(int, input())) for _ in range(n)]
    #print(arr)
    cost_map = [[99999 for _ in range(n)] for __ in range(n)]

    q = deque()
    q.append((0, 0))
    cost_map[0][0] = 0
    while q:
        r, c = q.popleft()
        for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            n_r, n_c = r + dr, c + dc
            if 0 <= n_r < n and 0 <= n_c < n:
                if cost_map[r][c] + arr[n_r][n_c] < cost_map[n_r][n_c]:
                    cost_map[n_r][n_c] = cost_map[r][c] + arr[n_r][n_c]
                    q.append((n_r, n_c))
            else:
                continue

    print(f'#{tc} {cost_map[n-1][n-1]}')