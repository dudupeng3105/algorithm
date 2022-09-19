import sys
# 15561번도 동일
input = sys.stdin.readline


def update(idx, val, node, l, r):
    if idx < l or idx > r:
        return tree[node]
    if l == r:
        tree[node] = [val, val, val, val]  # 수열이 원소 1개 짜리 {3}
        return tree[node]
    #print("하이")
    #print(idx, val, node, l, r)
    node_a = update(idx, val, node * 2, l, (l + r) // 2)
    node_b = update(idx, val, node * 2 + 1, (l + r) // 2 + 1, r)
    tree[node][0] = node_a[0] + node_b[0]
    tree[node][1] = max(node_a[1], node_a[0] + node_b[1])
    tree[node][2] = max(node_a[2], node_b[2], node_a[3] + node_b[1])
    tree[node][3] = max(node_b[3], node_a[3] + node_b[0])
    return tree[node]


def ans(node, l, r, s, e):
    if r < s or e < l:
        node_a = [0, -9999999, -9999999, -9999999]
        return node_a
    if s <= l and r <= e:
        return tree[node]
    node_a = ans(node * 2, l, (l + r) // 2, s, e)
    #print(node_a)
    node_b = ans(node * 2 + 1, (l + r) // 2 + 1, r, s, e)
    #print(node_b)
    node_c = [0, 0, 0, 0]
    node_c[0] = node_a[0] + node_b[0]
    node_c[1] = max(node_a[1], node_a[0] + node_b[1])
    node_c[2] = max(node_a[2], node_b[2], node_a[3] + node_b[1])
    node_c[3] = max(node_b[3], node_a[3] + node_b[0])
    return node_c


N, Q, U, V = map(int, input().split())
arr = [0] + list(map(int, input().split()))
tree = [[0, 0, 0, 0] for _ in range(4 * N + 1)]  # all, Lvar, mid, Rvar
#print(arr)
#print(tree)
for i in range(1, 4 * N + 1):
    tree[i][0] = 0
    tree[i][1] = -9999999
    tree[i][2] = -9999999
    tree[i][3] = -9999999
for i in range(1, N+1):
    #print(i)
    update(i, U * arr[i] + V, 1, 1, N)

#print(tree)
for _ in range(Q):
    c, a, b = map(int, input().split())
    if c == 0:
        temp = ans(1, 1, N, a, b)[2]
        print(temp - V)
    else:
        #arr[a] = b
        update(a, U * b + V, 1, 1, N)

# print(tree)
# max(U * (K[i] + K[i+1] + ... K[j]) + V * (j - i))
# = max(U * (K[i] + K[i+1] + ... K[j]) + V * (j - i + 1)) - V