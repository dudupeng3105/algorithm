from collections import deque
test_case = int(input())


def bfs(s_r, s_c):
    q = deque()
    q.append((s_r, s_c, ''))
    while q:
        r, c, result = q.popleft()
        for dr, dc in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
            n_r, n_c = r + dr, c + dc
            if 0 <= n_r < 4 and 0 <= n_c < 4:
                if len(result) <= 6:
                    q.append((n_r, n_c, result + str(arr[n_r][n_c])))
                else:  # 6 이면
                    result_set.add(result)
                    continue


for tc in range(1, test_case + 1):
    arr = [list(map(int, input().split())) for _ in range(4)]

    result_set = set()
    for i in range(4):
        for j in range(4):
            bfs(i, j)

    print(f'#{tc} {len(result_set)}')
