import sys
sys.setrecursionlimit(100000)
N = int(sys.stdin.readline())

def dfs(node):

    for i in range(len(arr[node])):
        next_element = arr[node][i]
        if not parent_arr[next_element]:
            parent_arr[next_element] = node
            dfs(next_element)

arr = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    arr[a].append(b)
    arr[b].append(a)

#print(arr)
parent_arr = [0 for _ in range(N+1)]

dfs(1)

for parent in parent_arr[2:]:
    print(parent)

