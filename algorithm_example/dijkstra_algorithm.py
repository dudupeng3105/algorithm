# 다익스트라 알고리즘 구현
from ipaddress import collapse_addresses
import collections
import heapq
# 모든 노드가 신호를 받는 데 걸리는 시간
# 모든 노으에 도달할 수 있는지 여부
# 우선순위 큐를 사용
# def network_delay_time(times, n, k):
#     graph = collections.defaultdict(list)
#     # 그래프 인접 리스트 구성
#     for u, v, w in times: # u(출발지), v(도착지), w(소요시간)
#         graph[u].append((v, w))
    
#     print(graph)
#     # 큐 변수: [(소요 시간, 정점)]
#     Q = [(0, k)]
#     dist = collections.defaultdict(int)
#     print(dist)
#     # 우선 순위 큐 최소값 기준으로 정점까지 최단 경로 삽입
#     print('Q', Q)    
#     while Q:
#         time, node = heapq.heappop(Q) # (0, 2)
#         if node not in dist:
#             dist[node] = time
#             for v, w in graph[node]:
#                 alt = time + w
#                 heapq.heappush(Q, (alt, v))
#                 print('Q', Q)
#                 print('dist', dist)

#     print('dist', dist)
#     # 모든 노드 최단 경로 존재 여부 판별
#     if len(dist) == n:
#         return max(dist.values())

#     return -1

# times = [[2,3,1],[2,1,1],[3,4,1]]
# N = 4
# K = 2
# print(network_delay_time(times,N,K))

def find_chapest_price(n, flights, src, dst, K):
    graph = collections.defaultdict(list)
    # 그래프 인접 리스트 구성
    for u, v, w in flights: # u:시작, v:도착, w:비용
        graph[u].append((v, w))

    print(graph)
    # 큐 변수 : [(가격, 정점, 남은 가능 경유지 수)]
    Q = [(0, src, K)]
    print('Q', Q)
    
    # 우선 순위 큐 최소값 기준으로 도착점까지 최소 비용 판별
    while Q:
        price, node, k =heapq.heappop(Q)
        
        if node == dst: # src = 0 --> dst = 2
            return price
        if k >= 0:
            for v, w in graph[node]:
                alt = price + w
                heapq.heappush(Q, (alt, v, k - 1))
                print('Q', Q)

    return -1


n = 3
edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0
dst = 2
k = 1
print(find_chapest_price(n,edges, src, dst, k))