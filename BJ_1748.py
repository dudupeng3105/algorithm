# 수 이어 쓰기 1
N = input()
result_len = 0
N_len = len(str(N))  # N의 자리수
for i in range(0, N_len-1):  # 9, 90, 900, 9000
    result_len += (i+1) * (9*(10**i))

# 마지막 자리 수
if N_len == 1:
    result_len += N_len * int(N)
else:
    result_len += N_len * ((int(N[1:]) + 1) + (int(N[0]) - 1) * (10**(N_len-1)))

print(result_len)
