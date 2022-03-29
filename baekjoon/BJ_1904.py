n = int(input())

pre_pre_num = 1
pre_num = 1
ans = 1
for i in range(2, n + 1):
    ans = (pre_pre_num + pre_num) % 15746
    pre_pre_num = pre_num
    pre_num = ans

print(ans % 15746)
