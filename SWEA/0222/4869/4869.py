import sys
sys.stdin = open("test.txt")

test_case = int(input())
for tc in range(1, test_case + 1):
    n = int(input()) // 10  # 10이면 1 20이면 2
    # dp
    dp = [0 for _ in range(n+1)]
    dp[1] = 1
    dp[2] = 3
    for i in range(3, n+1):  # 3 ~ n
        dp[i] = 2 * dp[i-2] + dp[i-1]

    print(f'#{tc} {dp[n]}')

