import sys
test_case = int(input())
for tc in range(test_case):
    a = float(input())
    s = ''
    i = 1
    flag = 0
    while i < 13:
        if a >= 2**(-i):
            a = a - 2**(-i)
            s = s + '1'
        else:
            s = s + '0'
        if a < 2**(-15):
            flag = 1
            break
        i += 1

    if flag:
        print(f'#{tc + 1} {s}')
    else:
        print(f'#{tc + 1} overflow')