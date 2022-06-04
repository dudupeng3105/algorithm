from collections import defaultdict


test_case = int(input())
for tc in range(1, test_case + 1):
    v, e = map(int, input().split())
    #weight_map = [[0 for _ in range(v+1)] for __ in range(v+1)]
    weight_dict = defaultdict(list)

    for _ in range(e):
        a, b, weight = map(int, input().split())
        weight_dict[a].append([b, weight])
        weight_dict[b].append([a, weight])

    visited = [False for _ in range(v + 1)]
    dist_lst = [100 for _ in range(v + 1)]

    def extract_min(que):
        # 방문안했고, dist 최소
        result_v = 0
        min_dist = 1000
        for node in que:
            if not visited[node] and dist_lst[node] < min_dist:
                result_v = node
                min_dist = dist_lst[node]

        return result_v

    def mst_prim(start_node):
        # 초기화
        q = [x for x in range(v+1)]
        dist_lst[start_node] = 0

        while q:
            node = extract_min(q)
            visited[node] = True
            q.remove(node)
            for adj_node, dist in weight_dict[node]:
                if not visited[adj_node] and dist < dist_lst[adj_node]:
                    dist_lst[adj_node] = dist
            # print(dist_lst)
            # print(visited)

    mst_prim(0)
    print(f'#{tc} {sum(dist_lst)}')
