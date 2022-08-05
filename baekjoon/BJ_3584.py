import sys
input = sys.stdin.readline

tc = int(input())
for _ in range(tc):
    n = int(input())
    graph = [0 for _ in range(n+1)]
    for __ in range(n-1):
        a, b = map(int, input().split())
        graph[b] = a

    node1, node2 = map(int, input().split())
    parent1, parent2 = [node1], [node2]
    # node 1
    while graph[node1] > 0:
        parent1.append(graph[node1])
        node1 = graph[node1]

    # node 2
    while graph[node2] > 0:
        parent2.append(graph[node2])
        node2 = graph[node2]

    for node in parent1:
        if node in parent2:
            print(node)
            break
