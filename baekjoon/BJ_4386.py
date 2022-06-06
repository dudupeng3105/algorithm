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


n = int(input())
stars = []
for _ in range(n):
    stars.append(list(map(float, input().split())))
# print(stars)

# 가중치 그래프 만들기
graph = []
for i in range(n):
    for j in range(i+1, n):
        w = (abs(stars[i][0] - stars[j][0])**2 + abs(stars[i][1] - stars[j][1])**2)**0.5
        graph.append([w, i, j])

# print(graph)

# 초기화
parent = [0] * (n)
rank = [0] * (n)
for i in range(1, n):
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

print(round(ans, 2))
# 마지막에 추가된 간선이 가장 가중치가 커서 제거해야 최솟값이 됨
# ans -= mst.pop()

# print(mst)
# print(ans)