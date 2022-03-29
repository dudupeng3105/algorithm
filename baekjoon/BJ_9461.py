import sys
input = sys.stdin.readline

test_case = int(input())
dp = [0, 1, 1, 1, 2, 2]
j = 1
for i in range(6, 101):
    dp.append(dp[i-1] + dp[j])
    j += 1

for tc in range(test_case):
    n = int(input())
    print(dp[n])
