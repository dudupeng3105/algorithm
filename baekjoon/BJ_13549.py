import sys
from collections import deque
# 한번더 체크해보기

def bfs(): 
    q = deque()
    q.append(start)
    map_1d[start] = 1
    visited[start] = True
    while q:
        next_point = q.popleft()
        a = [2*next_point, next_point + 1, next_point - 1]
        for i in range(3):
            point = a[i]
            if  point > 100000 or point < 0\
                or visited[point]:  # 이미 탐색한 곳이나 범위 밖
                continue
            else:  #새로 탐색
                if i == 0: # 순간이동은 0 초임
                    map_1d[point] = map_1d[next_point]
                    visited[point] = True
                    q.appendleft(point)
                else:
                    map_1d[point] = map_1d[next_point] + 1
                    visited[point] = True
                    q.append(point)

                if point == end:
                    return                
                            


start, end = map(int, sys.stdin.readline().split())
map_1d = [0] * (100001)
visited = [False for _ in range(100001)]
bfs()
print(map_1d[end]-1)