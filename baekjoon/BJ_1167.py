import sys
sys.setrecursionlimit(100000)


def dfs(node, result):
    
    for next_node, dist in arr[node]:
        if result[next_node] == 0:
            result[next_node] = result[node] + dist
            dfs(next_node, result)


N = int(sys.stdin.readline())
arr = [[] for _ in range(N+1)]
for _ in range(N):
    a = list(map(int, sys.stdin.readline().split()))
    i = 1
    while i != len(a) - 1:
        arr[a[0]].append([a[i], a[i + 1]])
        i += 2        

# 노드 1에서 가장 먼 vertax 구하고
result = [0 for _ in range(N+1)]
dfs(1, result)
result[1] = 0
temp_i = 0
temp_max = 0
for i, value in enumerate(result):
    if value > temp_max:
        temp_max=value
        temp_i = i

# 가장 먼 vertax에서 또 가장 먼 vetax 구하면 지름
result = [0 for _ in range(N+1)]
dfs(temp_i, result)
result[temp_i] = 0
print(max(result))