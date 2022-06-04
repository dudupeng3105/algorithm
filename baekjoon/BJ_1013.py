import sys
input = sys.stdin.readline


# (100+1+ | 01)+
def check(wave):
    i = 0
    len_str = len(wave)
    while i < len_str:
        if wave[i] == '0':
            if i + 1 >= len_str:
                return False
            if wave[i + 1] != '1':
                return False
            else:  # wave[i+1] == '1'
                i += 2
        else:  # '1'
            if i + 3 >= len_str:
                return False
            if wave[i + 1] != '0' or wave[i + 2] != '0':
                return False
            i += 1
            while i < len_str and wave[i] == '0':
                i += 1

            if i >= len_str:
                return False
            i += 1
            # 1의 seq(1001100같은 경우 계속 확인해줘야함)
            while i < len_str and wave[i] == '1':
                if i + 2 < len_str:
                    if wave[i + 1] == '0' and wave[i + 2] == '0':
                        break
                i += 1
    return True


test_case = int(input())
for _ in range(test_case):
    wave = input().rstrip()
    if check(wave):
        print('YES')
    else:
        print('NO')
