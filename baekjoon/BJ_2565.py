# 전깃줄
# 전봇대의 위치가 계속 증가하면 교차되지 않는다
# --> 최대 증가하는 부분수열(LIS)

import sys
input = sys.stdin.readline

n = int(input())
wire = []
# wire 입력 받기
for i in range(n):
    a, b = map(int, input().split())
    wire.append([a, b])

# 도달하는 전봇대의 위치를 오름차순으로 정렬
wire.sort(key=lambda x: x[1])
# print(wire)

dp = [1 for _ in range(n)]

for i in range(n):
    for j in range(i):
        # 만약 i 번쨰 wire의 시작 전봇대 위치보다 j 번째 wire의 시작 전봇대 위치
        # 가 작다면! -> j번째 wire다음에 올 수 있다는 말(dp[j] + 1)
        # j의 도달점은 걱정할 필요가 없다 -> 왜냐 j<i이고 이미 도달점 정렬이 되어있으므로
        # 도달점의 위치는 i가 크다(꼬이지 않는다!)
        # 이걸 기존의 dp[i]와 비교해서 넣는다
        if wire[i][0] > wire[j][0]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n-max(dp))