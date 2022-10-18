from collections import defaultdict

summit_intensity = [0, 10000001]


def solution(n, paths, gates, summits):
    # create graph
    # gates 출발지
    # summit 봉우리
    # n 노드 개수
    graph = defaultdict(list)
    for path in paths:
        a, b, w = path
        graph[a].append((b, w))
        graph[b].append((a, w))

    def dfs(node, depth, temp_intensity, this_summit):
        global summit_intensity
        if node in summits:
            if depth:  # 처음에는 건너뜀
                return

        if temp_intensity > summit_intensity[1]:
            return

        if node in gates:
            if temp_intensity < summit_intensity[1]:
                # print(node, temp_intensity)
                summit_intensity = [this_summit, temp_intensity]
            return

        for next_node, dist in graph[node]:
            if not visited[next_node]:
                visited[next_node] = True
                dfs(next_node, depth + 1, max(dist, temp_intensity), this_summit)
                visited[next_node] = False

    summits.sort()
    print(summits)
    for summit in summits:
        visited = [False for _ in range(n + 1)]
        dfs(summit, 0, 0, summit)

    # print(summit_intensity)
    answer = summit_intensity
    return answer