import sys

sys.stdin = open("test.txt")


def in_order(node):  # LNR
    global cnt
    # 해당 노드가 있으면
    if node:
        cnt += 1
        # LEFT_CHILD
        in_order(tree[node][1])
        # node
        # RIGHT_CHILD
        in_order(tree[node][2])


test_case = int(input())
for tc in range(1, test_case + 1):
    e, n = map(int, input().split())
    # parent, l_child, r_child
    tree = [[0, 0, 0] for _ in range(1002)]
    edge_info = list(map(int, input().split()))
    for i in range(e):
        a, b = edge_info[2 * i], edge_info[2 * i + 1]
        if not tree[a][1]:
            tree[a][1] = b
        else:
            tree[a][2] = b
        # 자식노드에 부모정보 입력
        tree[b][0] = a

    cnt = 0
    in_order(n)
    print(f'#{tc} {cnt}')