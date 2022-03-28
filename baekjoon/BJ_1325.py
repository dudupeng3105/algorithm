from collections import defaultdict, deque
import sys
input = sys.stdin.readline


def bfs(start):
    global available_pc
    q = deque()
    visited = [False for _ in range(n + 1)]
    q.append(start)
    visited[start] = True
    while q:
        pc = q.popleft()
        available_pc += 1
        for next_pc in graph[pc]:
            if not visited[next_pc]:
                visited[next_pc] = True
                q.append(next_pc)


# input 받기
n, m = map(int, input().split())
graph = defaultdict(list)
for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)

max_pc_num = 0
ans = []
for s in range(1, n + 1):    
    available_pc = 0
    bfs(s)
    if available_pc < max_pc_num:
        continue
    else:
        if available_pc == max_pc_num:
            ans.append(s)
        else:  # available_pc > max_pc_num
            max_pc_num = available_pc
            ans = [s]

ans.sort()
print(*ans)
