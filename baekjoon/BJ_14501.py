N = int(input())
T = [0 for x in range(N+1)]
P = [0 for x in range(N+1)]
dp = [0 for x in range(N+2)]

for i in range(1, N + 1):
    T[i], P[i] = map(int, input().split())

for i in range(N, 0, -1):
    if T[i] + i > (N + 1):
        dp[i] = dp[i + 1]
    else:
        dp[i] = max(P[i] + dp[i + T[i]], dp[i + 1])

print(dp[1])

