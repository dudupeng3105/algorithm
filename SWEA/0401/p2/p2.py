from collections import defaultdict, deque


def bfs():
    q = deque()
    q.append(1)
    visited = [False for _ in range((len(given_info) // 2) + 1)]
    visited[1] = True
    while q:
        node = q.popleft()
        print(node, end=' ')
        for next_node in graph[node]:
            if not visited[next_node]:
                visited[next_node] = True
                q.append(next_node)

    return


graph = defaultdict(list)

given_info = list(map(int, input().split()))

for i in range(len(given_info) // 2):
    graph[given_info[2 * i]].append(given_info[2 * i + 1])
    graph[given_info[2 * i + 1]].append(given_info[2 * i])

bfs()