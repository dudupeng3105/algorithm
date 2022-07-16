# 쿼리
import sys

input = sys.stdin.readline


n = int(input())
arr = [[0 for _ in range(n+1)]] + [[0] + list(map(int, input().split())) for _ in range(n)]
dp = [[[0 for _ in range(11)] for _ in range(n+1)] for __ in range(n+1)]

# dp 계산
for r in range(1, n+1):
    for c in range(1, n+1):
        for k in range(1, 11):
            dp[r][c][k] = dp[r][c][k] + dp[r-1][c][k] + dp[r][c-1][k] - dp[r-1][c-1][k]

        dp[r][c][arr[r][c]] += 1


#print(dp)
# 쿼리 받기
k = int(input())
for _ in range(k):
    r1, c1, r2, c2 = map(int, input().split())
    temp = [0 for _ in range(11)]
    # r2, c2
    for i in range(11):
        temp[i] = dp[r2][c2][i]

    # r1, c1 전까지 빼기
    for i in range(11):
        temp[i] = temp[i] - dp[r1-1][c2][i] - dp[r2][c1-1][i] + dp[r1-1][c1-1][i]

    ans = 0
    for i in range(11):
        if temp[i]:  # not 0
            ans += 1

    print(ans)