# 참조용
from collections import deque
import sys
input = sys.stdin.readline

way = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}


n, m = map(int, input().split())
Map = [list(input().strip()) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
cnt = 1


def solve():
    global cnt
    for i in range(n):
        for j in range(m):
            if not visited[i][j]:
                print()
                dfs(i, j)
                for k in range(n):
                    print(visited[k])
    print(cnt-1)


def dfs(x, y):
    global cnt
    dx, dy = way[Map[x][y]]
    nx, ny = x+dx, y+dy
    if not visited[nx][ny]:
        visited[x][y] = cnt
        dfs(nx, ny)
        visited[x][y] = visited[nx][ny]
    else:
        if visited[nx][ny] == cnt:
            cnt += 1
        visited[x][y] = visited[nx][ny]


solve()