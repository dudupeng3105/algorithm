import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
inner_arrows = [0 for _ in range(n + 1)]
for _ in range(m):
    seq = list(map(int, input().split()))
    k = seq[0]
    for i in range(1, k):
        a, b = seq[i], seq[i + 1]
        graph[a].append(b)
        inner_arrows[b] += 1

# print(graph)
# print(inner_arrows)
q = deque()
for i in range(1, n + 1):
    if inner_arrows[i] == 0:
        q.append(i)

result = []
while q:
    singer = q.popleft()
    result.append(singer)
    for next_singer in graph[singer]:
        inner_arrows[next_singer] -= 1
        if inner_arrows[next_singer] == 0:
            q.append(next_singer)

if len(result) != n:
    print(0)
else:
    for singer in result:
        print(singer)
