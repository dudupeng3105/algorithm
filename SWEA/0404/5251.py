from collections import defaultdict, deque

test_case = int(input())
for tc in range(1, test_case+1):
    end, edges_num = map(int, input().split())
    graph = defaultdict(list)
    dist_map = [10000001 for _ in range(edges_num+1)]
    for i in range(edges_num):
        s, e, dist = map(int, input().split())
        graph[s].append([e, dist])
    print(graph)
    # bfs
    q = deque()
    q.append(0)
    dist_map[0] = 0
    while q:
        node = q.popleft()
        for next_node, dist in graph[node]:
            if dist_map[node] + dist < dist_map[next_node]:
                dist_map[next_node] = dist_map[node] + dist
                q.append(next_node)
                print(dist_map)
            else:
                continue

    print(f'#{tc} {dist_map[end]}')
