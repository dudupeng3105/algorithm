import sys
input = sys.stdin.readline


def find(node):
    if parent[node] != node:
        parent[node] = find(parent[node])
    return parent[node]


def union(node1, node2):
    root1 = find(node1)
    root2 = find(node2)

    if root1 == root2:
        return node1

    if rank[root1] > rank[root2]:
        parent[root2] = root1
    else:  # rank[root1] <= rank[root2]
        parent[root1] = root2
        if rank[root1] == rank[root2]:
            rank[root2] += 1

    return False


tc = int(input())
for _ in range(tc):
    n = int(input())
    parent = [i for i in range(n + 1)]
    rank = [0 for _ in range(n + 1)]
    cycle = [False for _ in range(n + 1)]
    team_made = [False for _ in range(n + 1)]
    student = [0] + list(map(int, input().split()))
    for i in range(1, n + 1):
        a, b = i, student[i]
        cycle_root = union(a, b)
        if cycle_root:
            cycle[cycle_root] = True

    # print("이까지옴")
    # print(parent)
    # print(cycle)
    # 사이클 경로 찾기(사이클의 부모부터 시작해서 돌면서 팀원 체크)
    cnt = 0
    for i in range(1, n + 1):
        if cycle[i]:  # True
            start = i
            # print(start)
            # team_made[i] = True
            next_node = student[start]
            team_made[next_node] = True
            cnt += 1
            while next_node != start:
                # print(next_node)
                next_node = student[next_node]
                team_made[next_node] = True
                cnt += 1

    print(n - cnt)
