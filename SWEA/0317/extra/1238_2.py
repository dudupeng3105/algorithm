def preorder(node):
    if tree[node]:
        for i in range(1, len(tree[node])):
            if check[tree[node][i]] == 0:
                check[tree[node][i]] = check[node] + 1
                preorder(tree[node][i])


for tc in range(10):
    N, start = map(int, input().split())
    arr = list(map(int, input().split()))
    tree = [0] * 101
    for i in arr:
        tree[i] = [i]
    for i in range(N//2):
        parent = arr[i*2]
        child = arr[i*2+1]
        if child not in tree[parent]:
            tree[parent].append(child)
    #print(tree)
    check = [0] * 101
    preorder(start)
    check[start] = 1
    max_depth = 0
    result = 0
    for i in range(100,0,-1):
        if check[i] >= max_depth:
            max_depth = check[i]
            result = i
    #print(check)
    print(f'#{tc+1} {result}')