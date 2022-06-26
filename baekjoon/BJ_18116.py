import sys

input = sys.stdin.readline


def find(node):
    if parent[node] != node:
        parent[node] = find(parent[node])
    return parent[node]


def union(node_1, node_2):
    root_1 = parent[node_1]
    root_2 = parent[node_2]

    if rank[root_1] > rank[root_2]:
        parent[root_2] = root_1
        cnt[root_1] = cnt[root_1] + cnt[root_2]

    else:
        parent[root_1] = root_2
        if rank[root_1] == rank[root_2]:
            rank[root_2] += 1
        cnt[root_2] = cnt[root_1] + cnt[root_2]


n = int(input())
# make_set
parent = [node for node in range(10 ** 6 + 1)]
rank = [0 for _ in range(10 ** 6 + 1)]
cnt = [1 for _ in range(10 ** 6 + 1)]
for _ in range(n):
    ins = input().rstrip()
    if ins[0] == 'I':
        a, b = map(int, ins[2:].split())
        if find(a) != find(b):
            union(a, b)

    else:  # ins[0] =='Q'
        c = int(ins[2:])
        print(cnt[find(c)])