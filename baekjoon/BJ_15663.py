# 나중에 다시풀어보기
def dfs(seq):
    if len(seq) == M:
        print(' '.join(map(str, seq)))
        return

    pre = 0
    for i in range(N):
        if is_used[i]:  # 위에노드에서 쓴 숫자인지 확인
            continue
        if pre == num_list[i]:  # 이전 시블링과 같은 수 인지 확인
            continue

        seq.append(num_list[i])
        is_used[i] = True
        pre = num_list[i]
        dfs(seq)
        seq.pop()
        is_used[i] = False


N, M = map(int, input().split(' '))
num_list = list(map(int, input().split(' ')))
num_list = sorted(num_list)
prev_elements = []
is_used = [False for _ in range(N)]
dfs([])