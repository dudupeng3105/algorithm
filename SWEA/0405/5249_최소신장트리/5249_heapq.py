from collections import defaultdict
import heapq


test_case = int(input())
for tc in range(1, test_case + 1):
    v, e = map(int, input().split())
    weight_dict = defaultdict(list)

    for _ in range(e):
        a, b, weight = map(int, input().split())
        weight_dict[a].append([weight, a, b])
        weight_dict[b].append([weight, b, a])

    visited = [False for _ in range(v + 1)]

    # 힙(min heap)사용 시 현재 노드에서 최소 간선을 찾는 함수를
    # 만들 필요가 없음 (min heap의 root는 가장 가중치 작은 간선이 있음)
    def mst_prim(start_node):
        # 초기화
        visited[start_node] = True
        candidate = weight_dict[start_node]
        #print('원래리스트', candidate)
        heapq.heapify(candidate)
        #print('히피파이 후', candidate)
        mst = []
        total_weight = 0

        while candidate:
            weight, u, v = heapq.heappop(candidate)

            if not visited[v]:
                visited[v] = True
                mst.append((u, v))
                #print('mst', mst)
                total_weight += weight

                for edge in weight_dict[v]:  # 다음 인접 간선 탐색
                    if not visited[edge[2]]:
                        heapq.heappush(candidate, edge)
                        #print('push후', candidate)

        #print(mst)
        return total_weight

    print(f'#{tc} {mst_prim(0)}')
