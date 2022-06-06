import sys

input = sys.stdin.readline

n = int(input())
matrix_info = [[0, 0]]
for _ in range(n):
    row, col = map(int, input().split())
    matrix_info.append([row, col])

dp = [[0 for _ in range(n + 1)] for __ in range(n + 1)]

# 길이 하나 짜리 초기화

for start in range(1, n):
    end = start + 1
    dp[start][end] = matrix_info[start][0] * \
                     matrix_info[start][1] * matrix_info[end][1]

for length in range(2, n):
    for start in range(1, n + 1 - length):
        end = start + length
        # print(length, start, end)
        for cut_index in range(start, end):
            if not dp[start][end]:  # dp[start][end] == 0
                dp[start][end] = dp[start][cut_index] + dp[cut_index + 1][end] + matrix_info[start][0] * \
                                 matrix_info[cut_index][1] * matrix_info[end][1]
            else:
                dp[start][end] = min(dp[start][end], \
                                     dp[start][cut_index] + dp[cut_index + 1][end] + matrix_info[start][0] *
                                     matrix_info[cut_index][1] * matrix_info[end][1])
# print(dp)
print(dp[1][n])
