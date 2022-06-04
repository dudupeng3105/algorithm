given_str = input()


def check(given_str):
    i = 0
    len_str = len(given_str)
    while i < len_str:
        if given_str[i] == '0':
            if i + 1 >= len_str:
                return False
            if given_str[i+1] != '1':  # 01 밖에 안됨
                return False
            else:  # given_str[i+1] == '1':
                i += 2
        else:  # 1이 걸리면 100으로 시작해야함 최소 그리고 1로끝나거나 1*多로 끝남
            if i + 3 >= len_str:
                return False
            if given_str[i + 1] != '0' or given_str[i + 2] != '0':
                return False
            i += 1
            while i < len_str and given_str[i] == '0':
                i += 1

            if i >= len_str:
                return False
            i += 1
            # 1의 seq 건너뛰면서도 1인데 00붙은거도 체크함
            while i < len_str and given_str[i] == '1':
                if i + 2 < len_str:
                    if given_str[i + 1] == '0' and given_str[i + 2] == '0':
                        break
                    else:
                        i += 1

    return True


if check(given_str):
    print('SUBMARINE')
else:
    print('NOISE')















# p = re.compile('(100+1+|01)+')  # ~는 1개이상이니 +으로 바꾸기
#
# string = input()
# if p.fullmatch(string):
#     print('SUBMARINE')
#
# else:
#     print('NOISE')
