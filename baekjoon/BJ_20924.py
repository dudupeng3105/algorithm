import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def dfs(node, tmp_dist):
    global branch_dist
    if tmp_dist > branch_dist:
        branch_dist = tmp_dist

    for n_node, add_dist in tree[node]:
        if not visited[n_node]:
            visited[n_node] = True
            dfs(n_node, tmp_dist + add_dist)
            visited[n_node] = False


N, R = map(int, input().split())
# print(N, R)
tree = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b, dist = map(int, input().split())
    tree[a].append((b, dist))
    tree[b].append((a, dist))

# print(tree)

# STEP 1 기가 노드 찾기 => 기둥 길이
this_node = R
pillar_dist = 0
visited = [False for _ in range(N + 1)]
while True:
    visited[this_node] = True

    tmp_cnt = 0
    for check_node, check_dist in tree[this_node]:
        if not visited[check_node]:  # False
            tmp_cnt += 1
    # print("tmp_cnt", tmp_cnt, "this_node", this_node)
    if tmp_cnt != 1:  # 기가 노드 찾음
        break

    else:
        for nxt_node, tmp_dist in tree[this_node]:
            if visited[nxt_node]:
                continue
            else:
                pillar_dist += tmp_dist
                this_node = nxt_node
                break

# print(this_node, pillar_dist, visited)
if len(tree[this_node]) == 0:  # 기가 == 리프
    print(pillar_dist, 0)
else:
    # STEP 2 기가노드(this_node) 부터 DFS => 가지 길이
    branch_dist = 0
    dfs(this_node, 0)  # Node, tmp_dist
    print(pillar_dist, branch_dist)
