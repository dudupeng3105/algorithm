def get_root(x):
    if d[x] == x:
        return x
    else:
        return get_root(d[x])


def union(x, y):
    x = get_root(x)
    y = get_root(y)
    if x<y:
        d[y]= x
    else:
        d[x] = y


T = int(input())
for tc in range(1, T+1):
    V, E = map(int,input().split())
    edges = [list(map(int,input().split())) for _ in range(E)]
    edges.sort(key=lambda x: x[2])
    print('edges', edges)
    d = [0] * (V+1)
    for i in range(V+1):
        d[i] = i
    print('parent', d)
    result = 0
    for edge in edges:
        a, b, cost = edge
        if get_root(a) != get_root(b):
            print('edge', edge)
            union(a, b)
            print('parent', d)
            result += cost

    print(f'#{tc} {result}')