import sys


def dfs(depth, result):
    global max_num, min_num
    if depth == N - 1:
        temp = num_seq[0]
        for i in range(N - 1):
            if result[i] == '+':
                temp += num_seq[i + 1]
            elif result[i] == '-':
                temp -= num_seq[i + 1]
            elif result[i] == '*':
                temp *= num_seq[i + 1]
            else:  # /
                # 부호같음
                if (temp > 0 and num_seq[i + 1] > 0) or \
                        (temp < 0 and num_seq[i + 1] < 0):
                    temp = temp // num_seq[i + 1]
                # 부호 다를때
                else:
                    temp = - (abs(temp) // abs(num_seq[i + 1]))

        if temp > max_num:
            max_num = temp
        if temp < min_num:
            min_num = temp
        # 계산 들어감
        return

    for i in range(4):
        if sign_cnt[i]:
            sign_cnt[i] -= 1
            result += sign[i]
            dfs(depth + 1, result)
            sign_cnt[i] += 1
            result.pop()
        else:
            continue


N = int(sys.stdin.readline())
num_seq = list(map(int, sys.stdin.readline().split()))
sign_cnt = list(map(int, sys.stdin.readline().split()))
sign = ['+', '-', '*', '/']

max_num = -sys.maxsize
min_num = sys.maxsize
dfs(0, [])
print(max_num)
print(min_num)