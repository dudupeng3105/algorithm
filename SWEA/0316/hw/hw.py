import sys

sys.stdin = open("test.txt")


def in_order(node):  # LNR
    # 해당 노드가 있으면
    if node:
        # LEFT_CHILD
        in_order(tree[node][2])
        # node
        print(f'{tree[node][0]}', end='')
        # RIGHT_CHILD
        in_order(tree[node][3])


for tc in range(1, 11):
    n = int(input())
    # alphabet, parent, l_child, r_child
    tree = [['', 0, 0, 0] for _ in range(n + 1)]
    for _ in range(n):
        edge_info = list(map(str, input().split()))
        if len(edge_info) == 4:
            node, char, l_c, r_c = int(edge_info[0]), edge_info[1], int(edge_info[2]), int(edge_info[3])
            tree[node][0] = char
            tree[node][2] = l_c
            tree[node][3] = r_c
            # 자식에 부모 정보
            tree[l_c][1] = node
            tree[r_c][1] = node
        elif len(edge_info) == 3:
            node, char, l_c = int(edge_info[0]), edge_info[1], int(edge_info[2])
            tree[node][0] = char
            tree[node][2] = l_c
            # 자식에 부모 정보
            tree[l_c][1] = node
        else:  # len = 2
            node, char = int(edge_info[0]), edge_info[1]
            tree[node][0] = char

    print(f'#{tc}', end=' ')
    in_order(1)
    print()
