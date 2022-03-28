import sys
sys.stdin = open("test.txt")

test_case = int(input())
for tc in range(1, test_case + 1):
    n = int(input())
    arr = [[0 for _ in range(n)] for __ in range(n)]
    for i in range(n):
        arr[i] = list(map(int, input().split()))
    dr = [0, 1, 0, -1]
    dc = [-1, 0, 1, 0]
    visited = [0 for _ in range(n**2 + 1)]

    for r in range(n):
        for c in range(n):
            for k in range(4):
                n_r, n_c = r + dr[k], c + dc[k]
                if 0 <= n_r < n and 0 <= n_c < n:
                    if arr[n_r][n_c] == arr[r][c] + 1:
                        visited[arr[r][c]] = 1

    s = 0
    max_cnt = 0
    temp = 0
    for i in range(1, n**2 + 1):
        temp += 1
        if not visited[i]:
            if max_cnt < temp:
                s = i - temp + 1
                max_cnt = temp
            temp = 0

    print(f'#{tc} {s} {max_cnt}')

