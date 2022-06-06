import sys

input = sys.stdin.readline

n = int(input())
arr = [0] + list(map(int, input().split()))
m = int(input())
dp = [[0 for _ in range(n + 1)] for __ in range(n + 1)]
# 미리 계산
for i in range(1, n + 1):
    dp[i][i] = 1
    if arr[i - 1] == arr[i]:
        dp[i - 1][i] = 1

for i in range(2, n + 1):  # 길이
    for s in range(1, n + 1 - i):  # 시작 위치
        e = s + i
        if arr[s] == arr[e] and dp[s + 1][e - 1] == 1:
            dp[s][e] = 1

for _ in range(m):
    start, end = map(int, input().split())
    print(dp[start][end])
