from collections import deque


def bfs(s):
    que = deque()
    visited = [False for i in range(101)]

    que.append((s, 0))
    visited[s] = True

    while que:
        cur, cnt = que.popleft()
        print(cur)

        if cur == 100:
            return cnt

        for nxt in range(cur + 1, cur + 7):
            if not (1 <= nxt < 100) or visited[nxt]:
                continue

            if nxt in move:
                que.append((move[nxt], cnt+1))
                visited[move[nxt]] = True
                continue

            que.append((arr[nxt], cnt+1))
            visited[nxt] = True


arr = [i for i in range(1, 101)]

n, m = map(int, input().split())
move = [0 for _ in range(101)]
for _ in range(n):
    x, y = map(int, input().split())
    move[x] = y

for _ in range(m):
    u, v = map(int, input().split())
    move[u] = v

print(bfs(1))