import sys

input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))

dp = [[0 for _ in range(n)] for __ in range(3)]
# streak, index
dp[1][0] = arr[0]

for i in range(1, n):
    dp[0][i] = max(dp[2][i-1], dp[1][i-1], dp[0][i-1])
    dp[1][i] = dp[0][i-1] + arr[i]
    dp[2][i] = dp[1][i-1] + arr[i]

print(max(dp[0][n-1], dp[1][n-1], dp[2][n-1]))