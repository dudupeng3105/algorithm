import sys
input = sys.stdin.readline

string = input().rstrip()
n = len(string)
dp = [[False for _ in range(n)] for __ in range(n)]
# 팰린드롬 dp 만들기
# 초기화
# 길이 1
for i in range(n):
    dp[i][i] = True
# 길이 2
for i in range(n-1):
    if string[i] == string[i+1]:
        dp[i][i+1] = True

# 채워넣기
for length in range(2, n):
    for i in range(n-length):
        start = i
        end = i + length
        if string[start] == string[end] and dp[start+1][end-1]:
            dp[start][end] = True


# dfs로 분할의 개수의 최솟값을 찾자
result = [2501 for _ in range(n)]
result[0] = 1
for j in range(1, n):
    if dp[0][j]:
        result[j] = min(result[j], 1)

for i in range(1, n):
    result[i] = min(result[i], result[i-1] + 1)

    for j in range(i+1, n):
        if dp[i][j]:
            result[j] = min(result[j], result[i-1] + 1)

print(result[n-1])
