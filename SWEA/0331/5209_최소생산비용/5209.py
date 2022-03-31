def dfs(cost, product):
    global ans
    if cost > ans:
        return

    if product >= n:
        ans = cost
        return

    for factory in range(n):
        if not visited[factory]:
            visited[factory] = True
            dfs(cost + arr[product][factory], product + 1)  # 코스트합산, 제품가격 product+1개 결정
            visited[factory] = False


test_case = int(input())
for tc in range(1, test_case + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [0 for _ in range(n)]
    ans = 99999999
    dfs(0, 0)  # 0원, 제품 0개 결정

    print(f'#{tc} {ans}')