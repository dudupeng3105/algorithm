import sys
input = sys.stdin.readline


def find(node):
    # path compression
    if parent[node] != node:
        parent[node] = find(parent[node])
    return parent[node]


def union(node_v, node_u):
    root1 = find(node_v)
    root2 = find(node_u)

    # union-by-rank 기법
    if rank[root1] > rank[root2]:
        parent[root2] = root1
    else:
        parent[root1] = root2
        if rank[root1] == rank[root2]:
            rank[root2] += 1


def make_set(node):
    parent[node] = node
    rank[node] = 0


n, m = map(int, input().split())
graph = []
for _ in range(m):
    a, b, w = map(int, input().split())
    graph.append([w, a, b])

# 초기화
parent = [0] * (n + 1)
rank = [0] * (n + 1)
for i in range(1, n + 1):
    make_set(i)

# weight 기반 sort
graph.sort()

# 크루스칼
mst = []  # 선택된 간선

# 간선 연결
ans = 0
for w, a, b in graph:
    if find(a) != find(b):
        union(a, b)
        ans += w
        mst.append(w)
# print(mst)
# 마지막에 추가된 간선이 가장 가중치가 커서 제거해야 최솟값이 됨
ans -= mst.pop()

# print(mst)
print(ans)
