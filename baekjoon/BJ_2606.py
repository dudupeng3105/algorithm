from collections import defaultdict, deque
import sys

input = sys.stdin.readline


def bfs(start_pc):
    global corona_pc
    visited = [False for _ in range(n + 1)]
    q = deque()
    q.append(start_pc)
    visited[start_pc] = True
    while q:
        pc = q.popleft()
        corona_pc += 1
        for next_pc in graph[pc]:
            if not visited[next_pc]:
                visited[next_pc] = True
                q.append(next_pc)


n = int(input())
m = int(input())
graph = defaultdict(list)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

corona_pc = 0
bfs(1)
print(corona_pc - 1)  # 1번 컴퓨터는 빼야함
