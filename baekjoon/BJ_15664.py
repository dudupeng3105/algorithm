# 다시 풀어보기
def dfs(start):
    if len(seq) == M:
        print(' '.join(map(str, seq)))
        return

    pre = 0
    for i in range(start, N):
        if is_used[i]:  # 위에노드에서 쓴 숫자인지 확인
            continue
        if pre == num_list[i]:  # 이전 시블링과 같은 수 인지 확인
            continue

        is_used[i] = True
        seq.append(num_list[i])
        pre = num_list[i]
        dfs(i+1)
        is_used[i] = False
        seq.pop()



N, M = map(int, input().split(' '))
num_list = list(map(int, input().split(' ')))
num_list = sorted(num_list)
seq = []
is_used = [False for _ in range(N)]
dfs(0)