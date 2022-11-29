# 2698 인접한 비트의 개수
import sys
input = sys.stdin.readline

tc = int(input())
# 100*100*2
dp = [[[0 for _ in range(2)] for __ in range(101)] for ___ in range(101)]
# [n][k][끝나는 수(1 or 0)] = 개수
dp[1][0][0] = 1
dp[1][0][1] = 1

for n in range(2, 101):
    for k in range(n):   # 0 ~ n-1
        if k == 0:
            dp[n][k][0] = dp[n - 1][k][0] + dp[n - 1][k][1]
            dp[n][k][1] = dp[n - 1][k][0]
        else:
            dp[n][k][0] = dp[n-1][k][0] + dp[n-1][k][1]
            dp[n][k][1] = dp[n-1][k-1][1] + dp[n-1][k][0]


for _ in range(tc):
    n, k = map(int, input().split())
    print(dp[n][k][0] + dp[n][k][1])