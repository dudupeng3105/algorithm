import sys
input = sys.stdin.readline


def find(node):
    # path compression 기법
    if parent[node] != node:
        parent[node] = find(parent[node])
    return parent[node]


def union(node_1, node_2):
    root_1 = find(node_1)
    root_2 = find(node_2)

    parent[root_1] = root_2


# G(게이트 수), P(비행기 수)
g = int(input())
p = int(input())
parent = [i for i in range(g+1)]

cnt = 0
for plane in range(1, p+1):
    g_range = int(input())
    plane_parent = find(g_range)
    if plane_parent == 0:
        break
    union(plane_parent, plane_parent-1)
    cnt += 1

print(cnt)
