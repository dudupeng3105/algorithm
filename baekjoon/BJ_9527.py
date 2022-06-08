import sys
input = sys.stdin.readline


def acc_one_nums(x):
    if x == 0:
        return 0
    if x == 1:
        return 1

    len_x = len(bin(x)) - 2
    # else
    return x - 2 ** (len_x - 1) + 1 + acc_one_nums(x - 2 ** (len_x - 1)) + (len_x - 1) * 2**(len_x - 2)


a, b = map(int, input().split())
print(acc_one_nums(b) - acc_one_nums(a - 1))
