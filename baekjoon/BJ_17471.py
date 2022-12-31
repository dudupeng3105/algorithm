import sys
from collections import defaultdict, deque
from itertools import combinations

input = sys.stdin.readline

N = int(input())
person_number = list(map(int, input().split()))
graph = defaultdict(list)

for i in range(N):
    link_list = list(map(int, input().split()))
    for link_node in link_list[1:]:
        graph[i].append(link_node - 1)

# print(graph)
node_list = [i for i in range(N)]
# itertool로 조합 만들어주고 / a구역, b구역 리스트 만듬
ans_diff = 10001
for a_num in range(1, N // 2 + 1):
    b_num = N - a_num
    for combi in combinations(node_list, a_num):
        a_check, b_check = True, True
        visited = [False for _ in range(N)]
        s_node = combi[0]
        # Check A BFS
        q = deque()
        q.append(s_node)
        visited[s_node] = True

        while q:
            node = q.popleft()
            for n_node in graph[node]:
                if n_node in combi and not visited[n_node]:
                    q.append(n_node)
                    visited[n_node] = True

        for check_node in combi:
            if not visited[check_node]:
                a_check = False
                b_check = False

        if b_check:
            # Check B BFS
            for i in range(N):
                if not visited[i]:
                    s_node = i
            q = deque()
            q.append(s_node)
            visited[s_node] = True

            while q:
                node = q.popleft()
                for n_node in graph[node]:
                    if not visited[n_node]:
                        q.append(n_node)
                        visited[n_node] = True

        for j in range(N):
            if not visited[j]:
                b_check = False

        # 차이 계산
        if a_check and b_check:
            tmp_diff = 0
            for i in range(N):
                if i in combi:
                    tmp_diff += person_number[i]
                else:
                    tmp_diff -= person_number[i]

            tmp_diff = abs(tmp_diff)
            if tmp_diff < ans_diff:
                ans_diff = tmp_diff

if ans_diff == 10001:
    print(-1)
else:
    print(ans_diff)
