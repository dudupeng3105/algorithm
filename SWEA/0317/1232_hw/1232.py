import sys
sys.stdin = open("test.txt")


def operation(sign, a, b):
    if sign == '*':
        return a * b
    elif sign == '-':
        return a - b
    elif sign == '/':
        return a / b
    else:  # '+'
        return a + b


def in_order(node):  # LNR
    # 해당 노드가 있으면
    if node:
        if tree[node][0] in ['*', '-', '/', '+']:
            # LEFT_CHILD
            l_num = in_order(tree[node][2])
            # node
            op_sign = tree[node][0]
            # RIGHT_CHILD
            r_num = in_order(tree[node][3])
            return operation(op_sign, l_num, r_num)
        else:  # 숫자이면
            return tree[node][0]


for tc in range(1, 11):
    n = int(input())
    # value, parent_node, l_child_node, r_child_node
    tree = [['', 0, 0, 0] for _ in range(n + 1)]
    for _ in range(n):
        edge_info = list(map(str, input().split()))
        if len(edge_info) == 4:
            node, op, l_c, r_c = int(edge_info[0]), edge_info[1], int(edge_info[2]), int(edge_info[3])
            tree[node][0] = op
            tree[node][2] = l_c
            tree[node][3] = r_c
            # 자식노드에 부모 등록(할 필요가 없었음)
            tree[l_c][1] = node
            tree[r_c][1] = node
        else:  # len == 2
            node, value = int(edge_info[0]), int(edge_info[1])
            tree[node][0] = value

    result = 0
    result = in_order(1)
    print(f'#{tc} {int(result)}')
