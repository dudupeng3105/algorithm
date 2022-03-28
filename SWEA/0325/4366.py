test_case = int(input())

for tc in range(1, test_case + 1):
    binary_str = input()
    tri_str = input()
    bin_to_dec = int('0b' + binary_str, 2)
    #print(bin_to_dec)
    tri_to_dec = 0
    tri_length = len(tri_str)
    for i in range(len(tri_str)):
        tri_to_dec = tri_to_dec + int(tri_str[i]) * (3 ** (tri_length - i - 1))
    #print(tri_to_dec)

    # 2 진수 경우의 수 구하기
    binary_set = set()
    bin_length = len(binary_str)
    for i in range(bin_length):
        if i == 0:  # 맨 앞자리는 안바꿈(0이면 원래 없던거라 의미가 없음)
            continue

        if binary_str[i] == '1':  # 1 -> 0 으로
            temp = bin_to_dec - (2 ** (bin_length - i - 1))
            binary_set.add(temp)
        else:  # '0' -> 1
            temp = bin_to_dec + (2 ** (bin_length - i - 1))
            binary_set.add(temp)

    # 3 진수 경우의 수 구하기
    tri_set = set()
    for i in range(tri_length):
        if tri_str[i] == '2':  # 1, 0로변경
            temp = tri_to_dec - (3 ** (tri_length - i - 1))
            temp_2 = tri_to_dec - 2 * (3 ** (tri_length - i - 1))
            tri_set.add(temp)
            tri_set.add(temp_2)
        elif tri_str[i] == '1':  # 0, 2로 변경
            temp = tri_to_dec - (3 ** (tri_length - i - 1))
            temp_2 = tri_to_dec + (3 ** (tri_length - i - 1))
            tri_set.add(temp)
            tri_set.add(temp_2)
        else:  # tri_str[i] == '0':  # 1, 2로 변경
            temp = tri_to_dec + (3 ** (tri_length - i - 1))
            temp_2 = tri_to_dec + 2 * (3 ** (tri_length - i - 1))
            tri_set.add(temp)
            tri_set.add(temp_2)

    #print(binary_set)
    #print(tri_set)
    result = list(binary_set.intersection(tri_set))
    print(f'#{tc} {result[0]}')
