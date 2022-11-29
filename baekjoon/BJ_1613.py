# 1613 역사
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = [[500 for _ in range(n + 1)] for __ in range(n + 1)]
for i in range(n + 1):
    arr[i][i] = 0

for _ in range(k):
    a, b = map(int, input().split())
    arr[a][b] = 1

# 플로이드 - 워셜
# s - m - e
for m in range(n + 1):  # 경유하는 점
    for s in range(n + 1):  # 출발점
        for e in range(n + 1):  # 도착점
            # m을 경유해서 가는 경우가 더 좋으면 갱신
            arr[s][e] = min(arr[s][e], arr[s][m] + arr[m][e])


s = int(input())
for _ in range(s):
    a, b = map(int, input().split())
    if arr[a][b] != 500:
        print(-1)
    elif arr[b][a] != 500:
        print(1)
    else:
        print(0)
