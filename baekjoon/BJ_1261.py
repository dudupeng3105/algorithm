import sys
import heapq
M, N = map(int, sys.stdin.readline().split())

arr = [[0 for _ in range(M)] for __ in range(N)]
dist = [[-1 for _ in range(M)] for __ in range(N)]
for i in range(N):
    arr[i] = list(map(int, sys.stdin.readline().rstrip()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
Q = [(0, 0, 0)]
while Q:
    time, row, col = heapq.heappop(Q)    
    if dist[row][col] == -1: # 아직 가보지 않았다면
       dist[row][col] = time
       for i in range(4): # 0인 경우부터 처리함(다익스트라)           

           if row+dx[i] < N and col+dy[i] < M \
               and row + dx[i] >= 0 and col+dy[i] >= 0 \
               and arr[row+dx[i]][col+dy[i]] == 0 and \
                   dist[row+dx[i]][col+dy[i]] == -1:
               alt = time
               heapq.heappush(Q, (alt, row+dx[i], col+dy[i]))
       for i in range(4): # 벽인 경우
            if row+dx[i] < N and col+dy[i] < M \
                and row + dx[i] >= 0 and col+dy[i] >= 0 \
                and arr[row+dx[i]][col+dy[i]] == 1 and\
                    dist[row+dx[i]][col+dy[i]] == -1:
                alt = time + 1
                heapq.heappush(Q, (alt, row+dx[i], col+dy[i]))


# 벽이 없을 때 최단 경로는 (row-1) + (col-1)
print(dist[N-1][M-1])

