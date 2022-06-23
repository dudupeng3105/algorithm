import sys
input = sys.stdin.readline

# n, k
n, k = map(int, input().split())

# weight, value
wv = [[0, 0]]

for i in range(n):
    w, v = map(int, input().split())
    wv.append([w, v])

dp = [[0 for _ in range(k+1)] for _ in range(n + 1)]

for back_num in range(1, n + 1):
    weight = wv[back_num][0]
    value = wv[back_num][1]
    for limit_weight in range(k+1):
        if limit_weight < weight:
            # 한계 무게가 물품 무게보다 작으면 물품을 못담으므로 그냥 이전
            dp[back_num][limit_weight] = dp[back_num - 1][limit_weight]
        else:
            # 크면 max(이전 dp, dp[이전][한계무게-물품무게]) 이전이라는 의미는 최신업데이트된 dp라고 볼 수 있음
            dp[back_num][limit_weight] = max(dp[back_num - 1][limit_weight], dp[back_num-1][limit_weight-weight] + value)

# print(dp)
result = 0
for i in range(n+1):
    temp = max(dp[i])
    if temp > result:
        result = temp

print(result)
