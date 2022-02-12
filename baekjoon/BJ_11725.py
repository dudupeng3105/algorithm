import sys
from collections import deque
sys.setrecursionlimit(100000)
N = int(sys.stdin.readline())

arr = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    arr[a].append(b)
    arr[b].append(a)

# def dfs(node):

#     for i in range(len(arr[node])):
#         next_element = arr[node][i]
#         if not parent_arr[next_element]:
#             parent_arr[next_element] = node
#             dfs(next_element)            

# arr = [[] for _ in range(N+1)]
# for _ in range(N-1):
#     a, b = map(int, sys.stdin.readline().split())
#     arr[a].append(b)
#     arr[b].append(a)

# parent_arr = [0 for _ in range(N+1)]

# dfs(1)

# 스택 구현 #

# stack = []
# stack.append(1)
# parent_arr = [0 for _ in range(N+1)]
# visited = [False for _ in range(N+1)]

# visited[1] = True

# while stack:
#     parent = stack.pop()
#     for child in arr[parent]:
#         if not visited[child]:
#             visited[child] = True
#             parent_arr[child] = parent
#             stack.append(child)



# bfs 큐 구현
# parent_arr = [0 for _ in range(N+1)]
# visited = [False for _ in range(N+1)]

# def bfs(v):
#     q = deque([v])
#     visited[v] = True
#     while q:
#         x = q.popleft()
#         for i in arr[x]:
#             if not visited[i]:
#                 parent_arr[i] = x
#                 q.append(i)
#                 visited[i] = True

# bfs(1)

for parent in parent_arr[2:]:
    print(parent)

