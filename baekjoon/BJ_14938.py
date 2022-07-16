import sys

input = sys.stdin.readline
INF = 100000

# 지역의 개수, 수색범위, 길의 개수
n, m, r = map(int, input().split())
dist = [[INF for _ in range(n+1)] for __ in range(n+1)]
items = [0] + list(map(int, input().split()))
for i in range(n+1):
    dist[i][i] = 0

for _ in range(r):
    a, b, d = map(int, input().split())
    dist[a][b] = d
    dist[b][a] = d

# 플로이드 워셜
for mid in range(n+1):
    for s in range(n+1):
        for e in range(n + 1):
            dist[s][e] = min(dist[s][e], dist[s][mid] + dist[mid][e])


ans = 0
for start in range(1, n+1):
    temp = 0
    for point in range(1, n+1):
        if dist[start][point] <= m:
            temp += items[point]
    if temp > ans:
        ans = temp

print(ans)
