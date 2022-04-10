import sys
input = sys.stdin.readline


def get_root(node):
    if d[node] == node:
        return node
    d[node] = get_root(d[node])
    return d[node]


def union(x, y):
    d[get_root(x)] = get_root(y)


v, e = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(e)]
edges.sort(key = lambda x : x[2])
d = [x for x in range(v+1)]

result =0
cnt = 0
for edge in edges:
    a, b, weight = edge
    if cnt >= v-1:
        break
    if get_root(a) != get_root(b):  # 루트가 같으면 사이클임
        cnt += 1
        union(a, b)
        result += weight

print(result)