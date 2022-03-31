v, e = map(int, input().split())
graph = [[0, 0] for _ in range(v+1)]
edges = list(map(int, input().split()))
for i in range(e):
    if graph[edges[2*i]][0]:
        graph[edges[2 * i]][1] = edges[2 * i + 1]
    else:
        graph[edges[2 * i]][0] = edges[2 * i + 1]


def preorder(node):  # NLR
    # node
    print(node, end=' ')
    # left Child
    if graph[node][0]:
        preorder(graph[node][0])
    # right child
    if graph[node][1]:
        preorder(graph[node][1])


def inorder(node):  # LNR
    # left Child
    if graph[node][0]:
        inorder(graph[node][0])
    # node
    print(node, end=' ')
    # right child
    if graph[node][1]:
        inorder(graph[node][1])


def postorder(node):  # LRN
    # left Child
    if graph[node][0]:
        postorder(graph[node][0])
    # right child
    if graph[node][1]:
        postorder(graph[node][1])
    # node
    print(node, end=' ')


#print(graph)
print('전위 순회 : ', end="")
preorder(1)
print()
print('중위 순회 : ', end="")
inorder(1)
print()
print('후위 순회 : ', end="")
postorder(1)