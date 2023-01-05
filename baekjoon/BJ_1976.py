import sys
input = sys.stdin.readline

def find_root(x):
    # x가 root이면, 그대로 반환
    if x != parent[x]:
        return find_root(parent[x])
    return x

def union_root(x, y):
    x = find_root(x)
    y = find_root(y)

    if x != y:
        if node_rank[x] > node_rank[y]:
            parent[y] = x
        elif node_rank[y] > node_rank[x]:
            parent[x] = y
        else:
            parent[y] = x
            node_rank[x] += 1

    else:
        return


N = int(input())  # 도시의 수 200 이하
M = int(input())  # 여행 계획에 속한 도시들의 수 M
connected_arr = [list(map(int, input().split())) for _ in range(N)]
travel_plan = list(map(int, input().split()))
parent = [x for x in range(N)]
node_rank = [0 for _ in range(N)]

for i in range(N):
    for j in range(i, N): # 반 만 하면 됨
        if i != j:
            if connected_arr[i][j]:
                #print(i, j)
                union_root(i, j)

parent_node = parent[travel_plan[0]-1]
flag = 1
for plan in travel_plan:
    if parent_node != find_root(plan-1):
        flag = 0
        break

if flag:
    print("YES")
else:
    print("NO")

# print(connected_arr)
# print(travel_plan)
# print(parent)
# print(node_rank)


