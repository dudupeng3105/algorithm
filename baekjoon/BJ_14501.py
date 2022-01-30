def dfs(start, sum):
    global ans

    if start > N:
        return

    ans = max(ans, sum)

    for i in range(start, N):
        dfs(i + T[i], sum + P[i])


N = int(input())
T = [0 for x in range(15)]
P = [0 for x in range(15)]
for i in range(0, N):
    T[i], P[i] = map(int, input().split())
ans = 0
dfs(0, 0)
print(ans)