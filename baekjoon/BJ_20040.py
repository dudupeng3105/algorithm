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

    # 사이클 찾음
    if root_1 == root_2:
        return True

    # 사이클 아닐 경우 계속 만들어감
    # union-by-rank 기법
    if rank[root_1] > rank[root_2]:
        parent[root_2] = root_1
    else:
        parent[root_1] = root_2
        if rank[root_1] == rank[root_2]:
            rank[root_2] += 1

    return False


# def make_set(node):
#     parent[node] = node
#     rank[node] = 0


# 점의 개수, 진행된 차례 수
n, m = map(int, input().split())
flag = 0
# 초기화
parent = [i for i in range(n)]
rank = [0 for _ in range(n)]
for k in range(m):
    a, b = map(int, input().split())
    result = union(a, b)
    if result:
        flag = k + 1
        break

if flag:
    print(flag)
else:  # flag ==0
    print(0)
