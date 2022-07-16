import sys
input = sys.stdin.readline

n = int(input())
parent = list(map(int, input().split()))
graph = [] + [[] for _ in range(n)]
for i in range(1, n):
    node = parent[i]
    graph[node].append(i)

time = [0] + [0 for _ in range(n)]

# dfs
def dfs(node):
    temp = []

    for next_node in graph[node]:
        dfs(next_node) # 파고들어감
        temp.append(time[next_node])  # 맨밑에서는 0이 올라옴

    if temp:
        temp.sort(reverse=True)  # 큰 순서대로 정렬
        # 큰 거 부터 넣어야함
        # i가 작을수록 먼저넣는다는 의미, + 1은 최소 1분이니까는
        next_time = [(temp[i] + i + 1) for i in range(len(temp))]
        time[node] = max(next_time)


dfs(0)
# print(time)
print(time[0])
