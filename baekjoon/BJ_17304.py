from collections import defaultdict, deque


def bfs(s):
    q = deque()
    q.append(s)
    while q:
        node = q.popleft()
        for next_node in graph[node]:
            if not visited[next_node]:
                if node in graph[next_node]:
                    continue
                visited[next_node] = True
                q.append(next_node)

    return


n, m = map(int, input().split())
graph = defaultdict(list)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

visited = [False for _ in range(n + 1)]
for i in range(1, n+1):
    start = i
    bfs(start)
    #print(visited)


for i in range(1, n+1):
    if not visited[i]:
        for adj_node in graph[i]:
            if i in graph[adj_node] and visited[adj_node]:
                visited[i] = True

flag = 0
for i in range(1, n+1):
    if not visited[i]:
        flag = 1
        break

if flag:
    print('NO')
else:
    print('YES')

