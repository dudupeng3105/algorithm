import sys
# 마니또, 사이클 문제
input = sys.stdin.readline


def make_set(node):
    parent[node] = node
    rank[node] = 0


def find(node):
    if parent[node] != node:
        parent[node] = find(parent[node])
    return parent[node]


def union(node_1, node_2):
    root1 = find(node_1)
    root2 = find(node_2)

    if rank[root1] > rank[root2]:
        parent[root2] = root1
    else:
        parent[root1] = root2
        if rank[root1] == rank[root2]:
            rank[root2] += 1


tc = 1
while True:
    n = int(input())

    if not n:
        break

    # 문자열이라서 dict로 했음
    graph = dict()
    parent = dict()
    rank = dict()

    for i in range(n):
        a, b = map(str, input().rstrip().split(' '))
        make_set(a)
        graph[a] = b

    # 연결하면서 사이클 체크
    cnt = 0
    for start in graph.keys():
        end = graph[start]

        if find(start) != find(end):
            union(start, end)
        else:  # 지금 연결하려는 데 부모가 같으면 사이클이 형성됨
            # 마니또 체인 + 1
            cnt += 1

    print(tc, cnt)
    tc += 1
