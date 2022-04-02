from collections import defaultdict


def dfs():
    stack = list()
    stack.append(1)
    visited = [False for _ in range((len(given_info) // 2) + 1)]
    visited[1] = True
    while stack:
        #print(stack)
        node = stack.pop()
        print(node, end=' ')
        for next_node in graph[node]:
            if not visited[next_node]:
                visited[next_node] = True
                stack.append(next_node)

    return


graph = defaultdict(list)

given_info = list(map(int, input().split()))

for i in range(len(given_info) // 2):
    graph[given_info[2 * i]].append(given_info[2 * i + 1])
    graph[given_info[2 * i + 1]].append(given_info[2 * i])

dfs()