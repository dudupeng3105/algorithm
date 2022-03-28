test_case = int(input())

for tc in range(test_case):
    given_hex = input()
    convert_dict = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110', \
                    '7': '0111', '8': '1000', '9': '1001', 'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101', \
                    'E': '1110', 'F': '1111'}

    decode_dict = {'001101': 0, '010011': 1, '111011': 2, '110001': 3, '100011': 4, '110111': 5, '001011': 6, \
                   '111101': 7, '011001': 8, '101111': 9}

    converted_bin = ''
    for i in given_hex:
        converted_bin += convert_dict[i]

    # decoding
    # 1. 시작점 찾기
    flag = 1
    idx = 0
    while flag:
        if converted_bin[idx: 6 + idx] in decode_dict.keys():
            flag = 0
        else:
            idx += 1

    # 2. decoding 하기
    for i in range(len(converted_bin) // 6):
        try:
            print(decode_dict[converted_bin[6 * i + idx: 6 * (i + 1) + idx]], end=' ')
        except KeyError:
            break
    print()