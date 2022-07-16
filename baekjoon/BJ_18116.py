import sys
# 로봇 조립
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
        # 해당 로봇(최상위 부모)의 부품 개수 업데이트
        cnt[root_1] = cnt[root_1] + cnt[root_2]

    else:
        parent[root_1] = root_2
        if rank[root_1] == rank[root_2]:
            rank[root_2] += 1
        # 해당 로봇(최상위 부모)의 부품 개수 업데이트
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
        # union-find를 이용해 같은 부품끼리 집합을 만들어감
        if find(a) != find(b):
            union(a, b)

    else:  # ins[0] =='Q'
        c = int(ins[2:])
        # c 부품의 집합의 부모가 되는 로봇의 cnt를 return
        print(cnt[find(c)])