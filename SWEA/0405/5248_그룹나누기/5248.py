from collections import deque, defaultdict


def bfs(s_node):
    q = deque()
    q.append(s_node)
    visited[s_node] = True
    while q:
        node = q.popleft()
        for next_node in graph[node]:
            if not visited[next_node]:
                visited[next_node] = True
                q.append(next_node)

    return


test_case = int(input())
for tc in range(1, test_case + 1):
    n, m = map(int, input().split())
    given_edges = list(map(int, input().split()))
    graph = defaultdict(list)

    for i in range(m):
        graph[given_edges[2 * i]].append(given_edges[2 * i + 1])
        graph[given_edges[2 * i + 1]].append(given_edges[2 * i])

    cnt = 0
    visited = [False for _ in range(n + 1)]
    for start_node in range(1, n + 1):
        if not visited[start_node]:
            bfs(start_node)
            cnt += 1
        else:
            continue

    print(f'#{tc} {cnt}')