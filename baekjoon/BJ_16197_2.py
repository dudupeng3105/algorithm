r, c = map(int, input().split())
graph = []
coins = []
for i in range(r):
    row = input()
    tmp = []
    for j in range(c):
        if row[j] == "o":
            tmp.append(True)
            coins.append([i, j])
        elif row[j] == ".":
            tmp.append(True)
        else:  # row[j] == "#"
            tmp.append(False)
    graph.append(tmp)

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
visited = [[[[False]*c for _ in range(r)]
            for __ in range(c)] for ___ in range(r)]
print(visited)
que = []


def visitable(x, y):
    return 0 <= x < r and 0 <= y < c


def solve(init):
    que.append(init)
    visited[init[0][0]][init[0][1]][init[1][0]][init[1][1]] = True
    while que:
        coins = que.pop(0)
        # print(coins)
        if coins[2] > 10:
            break
        for i in range(4):
            # 이동
            nr1 = coins[0][0] + dr[i]
            nc1 = coins[0][1] + dc[i]
            nr2 = coins[1][0] + dr[i]
            nc2 = coins[1][1] + dc[i]
            cnt = coins[2]
            # 둘 다 떨어졌을 때
            if not visitable(nr1, nc1) and not visitable(nr2, nc2):
                continue
            # 하나만 떨어졌을 때
            if (not visitable(nr1, nc1) and visitable(nr2, nc2)) or (visitable(nr1, nc1) and not visitable(nr2, nc2)):
                return cnt
            # 벽을 만났을 때
            if not graph[nr1][nc1]:
                nr1, nc1 = coins[0][0], coins[0][1]
            if not graph[nr2][nc2]:
                nr2, nc2 = coins[1][0], coins[1][1]
            # 둘 다 안떨어졌을 때
            if not visited[nr1][nc1][nr2][nc2]:
                visited[nr1][nc1][nr2][nc2] = True
                que.append([[nr1, nc1], [nr2, nc2], cnt+1])
    return -1


print(solve(coins+[1]))





