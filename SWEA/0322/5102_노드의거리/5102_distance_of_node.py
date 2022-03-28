from collections import deque


def bfs():
    while q:
        node, dist = q.popleft()
        for next_node in graph[node]:
            if not truth_map[next_node]:
                truth_map[next_node] = True
                q.append((next_node, dist + 1))
                if next_node == g:
                    return dist + 1

    return 0


dr = [0, 0, 1, -1]
dc = [-1, 1, 0, 0]
test_case = int(input())
for tc in range(1, test_case + 1):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v + 1)]
    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    s, g = map(int, input().split())
    truth_map = [False for _ in range(v + 1)]
    q = deque()
    q.append((s, 0))  # start, dist
    truth_map[s] = True
    result = bfs()
    print(f'#{tc} {result}')
