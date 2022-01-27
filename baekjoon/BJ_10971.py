# 외판원 순회 2
N = int(input())
maps = []
for _ in range(N):
    maps.append(list(map(int, input().split())))
res = 999999999
discovered = [0] * N
add = 0

def DFS(v, add, discovered):
    global res        
    if add > res:
        return
    if sum(discovered) == N-1: # 4개면 출발지에서 나머지 3개도시(간선 3번탐) 마지막 한개 추가
        if maps[v][0]:
            res = min(res, add + maps[v][0])
        return

    for i in range(1, N): # 0 ~ N-1
        if maps[v][i] and discovered[i] == 0: # 가는 길이 존재하고 안 들렀음
            discovered[i] = 1
            DFS(i, add+maps[v][i], discovered)
            discovered[i] = 0

for i in range(1, N):
    if maps[0][i]: # 출발지에서 가는길이 존재
        discovered[i] = 1
        DFS(i, maps[0][i], discovered)
        discovered[i] = 0
print(res)
