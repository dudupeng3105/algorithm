from collections import defaultdict, deque


# 풀이 1(dfs)
def bfs():
    q = deque()
    visited = [False for _ in range(n + 1)]
    q.append((1, 0))  # node, dist
    visited[1] = True
    while q:
        node, dist = q.popleft()
        for next_node in friend_dict[node]:
            if not visited[next_node]:
                visited[next_node] = True
                q.append((next_node, dist + 1))
                if next_node == f:
                    return dist + 1

    return False

T = int(input())
for tc in range(1, T + 1):
    f, n = map(int, input().split())
    friend_dict = defaultdict(list)
    for i in range(1, n + 1):
        friend_dict[i] = list(map(int, input().split()))

    result = bfs()
    if not result:
        result = '티미룸 안써!'
    print(f'#{tc} {result}')