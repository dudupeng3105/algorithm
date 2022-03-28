from collections import deque, defaultdict
import sys
input = sys.stdin.readline


def bfs(start):
    q = deque()
    q.append(start)
    visited[start] = True
    tree_minimum_price = price_lst[start]
    while q:
        node = q.popleft()
        if price_lst[node] < tree_minimum_price:
            tree_minimum_price = price_lst[node]

        for next_node in graph[node]:
            if not visited[next_node]:
                visited[next_node] = True
                q.append(next_node)

    return tree_minimum_price


n, m, my_money = map(int, input().split())
price_lst = [0] + list(map(int, input().split()))
visited = [False for _ in range(n+1)]
graph = defaultdict(list)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

minimum_price_lst = []
for i in range(1, n+1):
    if not visited[i]:
        temp = bfs(i)
        minimum_price_lst.append(temp)

ans = sum(minimum_price_lst)
if my_money >= ans:
    print(ans)
else:
    print("Oh no")
