import sys


def itoa(num):  # int -> str
    minus_checker = 0
    # 음수 체크
    if num < 0:
        num = abs(num)
        minus_checker = 1

    s = ''
    digit = 0
    # 자리수 구하기
    while True:
        if num // (10 ** digit) == 0:
            break
        else:
            digit += 1

    # 변환
    for i in range(digit-1, -1, -1):
        temp = num // (10 ** i)
        num -= temp * (10 ** i)
        s += chr(temp+ord('0'))

    if minus_checker: # 음수면
        return '-' + s
    else:
        return s


sys.stdin = open("test.txt")

for tc in range(1, 7):
    n = int(input())
    string_s = itoa(n)
    print(f'#{tc} {string_s} {type(string_s)}')
