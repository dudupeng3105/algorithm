import time
start = time.time()


def dfs(prob, worker):
    global ans
    if prob <= ans:
        return

    if worker == n:
        ans = prob
        return

    for work in range(n):
        if not visited[work]:
            visited[work] = True
            dfs(prob * arr[worker][work]/100, worker + 1)  # 확률계산, 직원일 결정 + 1
            visited[work] = False


test_case = int(input())
for tc in range(1, test_case + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [0 for _ in range(n)]
    ans = 0
    dfs(100, 0)  # 100%, 직원일 0개 결정
    ans = round(ans, 6)
    print(f'#{tc}{ans: 6f}')

end = time.time()
print(end-start)