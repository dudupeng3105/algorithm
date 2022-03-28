test_case = int(input())


def binary_to_deci(binary_str):  # p1 문제
    length = len(binary_str) // 7
    for i in range(length + 1):
        if i == length:
            temp_bin = binary_str[7 * i:]
        else:
            temp_bin = binary_str[7 * i: 7 * (i + 1)]

        square_num = 0
        a = 0
        for num_bin in temp_bin[::-1]:
            a += int(num_bin) * (2 ** square_num)
            square_num += 1

        print(a, end=' ')


for tc in range(test_case):
    given_hex = input()
    convert_dict = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110',\
                    '7': '0111', '8': '1000', '9': '1001', 'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101',\
                    'E': '1110', 'F': '1111'}

    converted_bin = ''
    for i in given_hex:
        converted_bin += convert_dict[i]
    binary_to_deci(converted_bin)
