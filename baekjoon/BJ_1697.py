import sys
from collections import deque


def bfs(): 
    q = deque()
    q.append(start)
    map_1d[start] = 1
    parent[start] = -1
    while q:
        next_point = q.popleft()
        a = [next_point + 1, next_point - 1, 2*next_point]
        for point in a:       
            if  point > 100000 or point < 0\
                or map_1d[point]:  # 이미 탐색한 곳이나 범위 밖
                continue
            else:  #새로 탐색
                map_1d[point] = map_1d[next_point] + 1
                if point == end:
                    parent[point] = next_point
                    return
                else:
                    q.append(point)
                    parent[point] = next_point


start, end = map(int, sys.stdin.readline().split())
map_1d = [0] * (100001)
parent = [0] * (100001)
bfs()
print(map_1d[end]-1)

# 경로 계산
result = []
p = end
while parent[p] != -1:
    result.append(p)
    p = parent[p]

result.append(p)
print(*result[::-1])
    

    
