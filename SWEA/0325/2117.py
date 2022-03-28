from collections import deque
test_case = int(input())

dr = [1, -1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(s_r, s_c):
    q = deque()
    truth_map = [[False for _ in range(n)] for __ in range(n)]
    q.append((s_r, s_c))
    truth_map[s_r][s_c] = True
    total_home_revenue = 0
    home_cnt = 0
    if arr[s_r][s_c]:
        total_home_revenue += m*arr[s_r][s_c]
        home_cnt += 1
    ans = home_cnt  # 초기화
    k = 1
    while q:
        size = len(q)

        for _ in range(size):  # k=1 일때 돌고, k=2 일때 돌고, k=3 일때 돌고
            r, c = q.popleft()
            for i in range(4):
                n_r, n_c = r + dr[i], c + dc[i]
                if 0 <= n_r <n and 0 <= n_c < n and truth_map[n_r][n_c] == False:
                    truth_map[n_r][n_c] = True
                    if arr[n_r][n_c]:
                        total_home_revenue += m* arr[n_r][n_c]
                        home_cnt += 1
                    q.append((n_r, n_c))

        k += 1
        operation_cost = k * k + (k - 1) * (k - 1)
        if total_home_revenue - operation_cost >= 0:
            ans = home_cnt

    return ans


for tc in range(1, test_case + 1):
    # n, m = 크기, 비용
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    result_ans = 0
    for i in range(n):
        for j in range(n):
            temp = bfs(i, j)
            if temp > result_ans:
                result_ans = temp

    print(f'#{tc} {result_ans}')
