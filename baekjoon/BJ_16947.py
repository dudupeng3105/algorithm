import sys
from collections import defaultdict
sys.setrecursionlimit(10000)
from collections import deque


def dfs(now_vertax, depth):    
    global cycle, circular
    # 종료조건     
    if now_vertax == intersection and depth >= 2:        
        cycle = 1
        for station in stations:
            circular[station] = True
        return

    visited[now_vertax] = True
    # 재귀    
    for vertax in connected_dict[now_vertax]:                
        if not visited[vertax]:
            stations.append(vertax)
            dfs(vertax, depth + 1)
            stations.pop()              
        elif vertax == intersection and depth >= 2:
            dfs(vertax, depth)  
    


# 입력 받기
N = int(sys.stdin.readline())
connected_dict = defaultdict(list)
for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())
    connected_dict[a].append(b)
    connected_dict[b].append(a)

intersection_lst = [] # 순환선의 교차점 기록
stations = [] # circular에 쓰기위해 임시 리스트(temp)
circular = [False for _ in range(N + 1)] # 순환선인지 아닌지 기록
# 순환선의 역 중 지선과 연결되는 역을 찾아냄(intersection)
for key in connected_dict.keys():
    if len(connected_dict[key]) > 2:  #연결된 간선 3개 이상
        visited = [False for _ in range(N + 1)]
        cycle = 0        
        visited[key] = True
        intersection = key        
        dfs(key, 0)
        if cycle == 1:
            intersection_lst.append(key)        
        visited[key] = False


q = deque()
for intersection in intersection_lst:
    circular[intersection] = True
    q.append(intersection)

# 거리 찾기
while q:
    station = q.popleft()
    for i in connected_dict[station]:        
        if circular[i]: # 순환선이면
            continue
        else: # 지선이면
            circular[i] = circular[station] + 1
            q.append(i)

# 거리 계산
for i in range(N+1):
    if circular[i] == 1 or circular[i] == 0:
        circular[i] = 0
    else:
        circular[i] = circular[i] - 1
# 출력
print(*circular[1:])




# import sys
# N=int(input())
# parent=[0]*(N+1)
# ans=[0]*(N+1)
# graph=[[] for _ in range(N+1)]
# graphSize=[0]*(N+1)
# for _ in range(N):
#     a,b=map(int,input().split())
#     graph[a].append(b)
#     graph[b].append(a)
#     graphSize[a]+=1
#     graphSize[b]+=1
# while 1 in graphSize:
#     for i in range(1,N+1):
#         if graphSize[i]==1:
#             parent[i]=graph[i][0]
#             graphSize[i]=0
#             graphSize[parent[i]]-=1
#             graph[parent[i]].remove(i)
# while any(parent):
#     for i in range(1,N+1):
#         if parent[i]!=0:
#             if parent[parent[i]]==0:
#                 ans[i]=ans[parent[i]]+1
#                 parent[i]=0
# for i in range(1,N+1):
#     print(ans[i],end=' ')​