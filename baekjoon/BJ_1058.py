import sys
input = sys.stdin.readline
# 친구 2
n = int(input())
dist = [[1000 for _ in range(n)] for __ in range(n)]
for i in range(n):
    relation = input().rstrip()
    for j in range(n):
        if relation[j] == 'Y':
            dist[i][j] = 1

for mid in range(n):
    for s in range(n):
        for e in range(n):
            dist[s][e] = min(dist[s][e], dist[s][mid] + dist[mid][e])

cnt = 0
for i in range(n):
    temp = 0
    for j in range(n):
        if i != j:
            if dist[i][j] < 3:
                temp += 1

    if temp > cnt:
        cnt = temp

print(cnt)