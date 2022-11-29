import sys

input = sys.stdin.readline


def dfs(weight, depth):
    global cnt

    if weight < 0:
        return

    if depth == n:
        cnt += 1
        return

    for i in range(n):
        if not visited[i]:
            visited[i] = True
            dfs(weight + arr[i], depth + 1)
            visited[i] = False


n, k = map(int, input().split())
arr = list(map(int, input().split()))
arr = [arr[i] - k for i in range(len(arr))]  # k를 뺌
cnt = 0
visited = [False] * n
dfs(0, 0)
print(cnt)
