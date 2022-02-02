from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)
def dfs(start):    
    visited[start] = True 
    
    for i in connected_dict[start]:
        if visited[i] == False:
            dfs(i)    
    

N, M = map(int, sys.stdin.readline().split())  # vertax, edge
connected_dict = defaultdict(list)
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())    
    connected_dict[a].append(b)
    connected_dict[b].append(a)    


visited = [False for x in range(N + 1)]
cnt = 0
for i in range(1, N + 1):    
    if visited[i] == False:
        dfs(i)
        cnt += 1
    else:
        continue

print(cnt)
