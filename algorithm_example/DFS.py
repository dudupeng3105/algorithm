# 그래프 탐색알고리즘은 크게 DFS, BFS
# 주로 DFS를 많이 쓰고 구현은 재귀 혹은 스택을 통해 구현한다.
# BFS의 경우 큐로 구현함

graph = {
    1: [2, 3, 4],
    2: [5],
    3: [5],
    4: [],
    5: [6, 7],
    6: [],
    7: [3]
}

# DFS 순회 코드


def recursive_dfs(v, discovered = []):
    discovered.append(v)
    for w in graph[v]:  # 내려가고
        if w not in discovered:
            discovered = recursive_dfs(w, discovered)
    # 해당 정점에 연결된 정점 다돌면 return
    return discovered

# DFS 스택 이용 반복 구조


def iterative_dfs(start_v):
    discovered = []
    stack = [start_v]  # stack = [1] /
    while stack:  # 스택에 내용물 있을 때 까지 stack = [1] / stack = [1,2,3,4] / stack = [2,3]
        v = stack.pop() # v = 1 / v = 4 / v = 3
        if v not in discovered:
            discovered.append(v)  # dis =[1] / dis = [1, 4] / dis = [1, 4, 3]
            for w in graph[v]:  # (1: w[2,3,4]) / (4: w[]) / (3: w[5])
                stack.append(w)  # stack = [2, 3, 4] / stack = [2,3] / stack = [2, 5]
    return discovered


print(f'recursive_dfs: {recursive_dfs(1)}')
print(f'iterative_dfs: {iterative_dfs(1)}')