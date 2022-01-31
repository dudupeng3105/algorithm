N, S = map(int, input().split())
seq = list(map(int, input().split()))
cnt = 0
for i in range(1, 2**N):
    bit = bin(i)
    result = 0
    i = 0
    for b in bit[2:][::-1]:
        if b == '0':
            pass
        else:
            result += seq[i]
        i += 1
    if result == S:
        cnt += 1

print(cnt)

# def main():
#     N, S = map(int, input().split())
#     seq = list(map(int, input().split()))
#
#     answer = 0
#     for select in range(1, 1 << N):
#         tmp = 0
#         for i in range(N):
#             if select & (1 << i): # i 자리수가 1이면 더함
#                 tmp += seq[i]
#         if tmp == S:
#             answer += 1
#
#     print(answer)
#
# if __name__ == '__main__':
#     main()

# 다른사람 풀이 보니까 itertools 쓰는게 빠르긴함(10배 정도)
