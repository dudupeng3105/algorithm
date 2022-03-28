import sys

sys.stdin = open("test.txt")


def preorder(node):  # NLR
    # 해당 노드가 있으면
    if node:
        # node
        print(f'{node}', end=' ')
        # LEFT_CHILD
        preorder(tree[node][1])
        # RIGHT_CHILD
        preorder(tree[node][2])


def in_order(node):  # LNR
    # 해당 노드가 있으면
    if node:
        # LEFT_CHILD
        in_order(tree[node][1])
        # node
        print(f'{node}', end=' ')
        # RIGHT_CHILD
        in_order(tree[node][2])


def postorder(node):  # LRN
    # 해당 노드가 있으면
    if node:
        # LEFT_CHILD
        postorder(tree[node][1])
        # RIGHT_CHILD
        postorder(tree[node][2])
        # node
        print(f'{node}', end=' ')


# 각 노드의 수
V = int(input())
# 간선의 수
E = V - 1

# 간선 정보
arr = list(map(int, input().split()))
print(arr)

tree = [[0, 0, 0] for _ in range(V + 1)]
# [Parent, L_child, R_child]
for i in range(E):
    parent, child = arr[2 * i], arr[2 * i + 1]
    if tree[parent][1] == 0:  # 왼쪽 비었으면
        tree[parent][1] = child
    else:
        tree[parent][2] = child

    # 자식에 부모 입력
    tree[child][0] = parent

print(tree)
print('전위 순회')
preorder(1)
print()
print('-'*30)
print('중위 순회')
in_order(1)
print()
print('-'*30)
print('후위 순회')
postorder(1)
print()
print('-'*30)
