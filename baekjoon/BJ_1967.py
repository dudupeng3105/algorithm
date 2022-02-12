import sys
sys.setrecursionlimit(100000)


def dfs(node, result):
    
    for next_node, dist in arr[node]:
        if result[next_node] == 0:
            result[next_node] = result[node] + dist
            dfs(next_node, result)


N = int(sys.stdin.readline())
arr = [[] for _ in range(N+1)]
for _ in range(N-1):
    start, end, dist = map(int, sys.stdin.readline().split())
    arr[start].append([end, dist])
    arr[end].append([start, dist])
    

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