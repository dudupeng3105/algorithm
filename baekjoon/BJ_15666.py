def dfs(start):
    if len(seq) == M:
        print(' '.join(map(str, seq)))
        return

    pre = 0
    for i in range(start, N):
        if pre == num_list[i]:  # 이전 시블링과 같은 수 인지 확인
            continue

        seq.append(num_list[i])
        pre = num_list[i]
        dfs(i)
        seq.pop()



N, M = map(int, input().split(' '))
num_list = list(map(int, input().split(' ')))
num_list = sorted(num_list)
seq = []
dfs(0)
