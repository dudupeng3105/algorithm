import sys

input = sys.stdin.readline

N = int(input())
arr = [1]  # n == 1


def dfs(seq, length):
    for k in range(1, length // 2 + 1):
        if seq[-1:-(1 + k):-1] == seq[-(1 + k):-(1 + 2 * k):-1]:
            return

    if length == N:
        print(*seq, sep="")
        exit(0)

    for num in range(1, 4):
        seq.append(num)
        dfs(seq, length + 1)
        seq.pop()

    return


dfs([1], 1)

# for length in range(2, n+1):
#     for num in range(1, 4):  # 1, 2, 3
#         flag = 1
#         arr.append(num)
#         for k in range(1, length//2+1):
#             if arr[-1:-(1+k):-1] == arr[-(1+k):-(1+2*k):-1]:
#                 flag = 0
#                 break
#
#         if not flag:
#             arr.pop()
#             continue
#         else:  # flag == 1
#             break
#
# print(*arr, sep="")
