import sys

input = sys.stdin.readline

n, m = map(int, input().split())  # n개의 앱, 필요한 메모리
mem_list = [0] + list(map(int, input().split()))
cost_list = [0] + list(map(int, input().split()))

dp = [[0 for _ in range(sum(cost_list) + 1)] for __ in range(len(cost_list) + 1)]
result = 9999999999

for i in range(1, len(cost_list)):
    cost = cost_list[i]
    mem = mem_list[i]
    # print(dp)
    for j in range(len(dp[1])):  # 누적비용
        if j < cost:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j - cost] + mem, dp[i - 1][j])

        if dp[i][j] >= m:
            result = min(result, j)

print(result)
