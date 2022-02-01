from collections import defaultdict


def dfs(person, depth):
    # 조건 해당하는 거 있으면 바로 출력하고 프로그램 종료
    if depth == 5:
        print(1)
        exit(0)

    for man in connected_dict[person]:
        if man in visited:
            continue
        else:
            visited.append(man)
            dfs(man, depth + 1)
            visited.pop()


# 입력 받기
N, M = map(int, input().split())
connected_dict = defaultdict(list)
for _ in range(M):
    a, b = map(int, input().split())
    connected_dict[a].append(b)
    connected_dict[b].append(a)

# dfs 돌리기
visited = []
for i in range(N):  # 시작이 0~N-1 까지
    visited.append(i)
    dfs(i, 1)
    visited.pop()

# 위의 for문 다돌면 없었다는 것이므로 0 출력
print(0)