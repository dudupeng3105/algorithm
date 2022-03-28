import sys
sys.stdin = open("test_2.txt")


test_case = int(input())

decode_dict = {'0001101': '0', '0011001': '1', '0010011': '2', '0111101': '3', '0100011': '4', '0110001': '5',
               '0101111': '6', '0111011': '7', '0110111': '8', '0001011': '9'}
convert_dict = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110', \
                '7': '0111', '8': '1000', '9': '1001', 'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101', \
                'E': '1110', 'F': '1111'}


def check_ratio(binary_str, this_mux):
    result = [1, 0, 0, 0]
    temp = binary_str[0]
    c = 0
    for i in range(1, this_mux):
        if binary_str[i] == temp:
            result[c] += 1
        else:
            c += 1
            temp = binary_str[i]
            result[c] += 1

    # 비율 최소화
    min_num = min(result)
    while min_num > 1:
        result = [x // min_num for x in result]
        min_num = min(result)
    return result


def convert_func(ratio_list):
    if ratio_list == [3, 2, 1, 1]:
        return '0'
    elif ratio_list == [2, 2, 2, 1]:
        return '1'
    elif ratio_list == [2, 1, 2, 2]:
        return '2'
    elif ratio_list == [1, 4, 1, 1]:
        return '3'
    elif ratio_list == [1, 1, 3, 2]:
        return '4'
    elif ratio_list == [1, 2, 3, 1]:
        return '5'
    elif ratio_list == [1, 1, 1, 4]:
        return '6'
    elif ratio_list == [1, 3, 1, 2]:
        return '7'
    elif ratio_list == [1, 2, 1, 3]:
        return '8'
    elif ratio_list == [3, 1, 1, 2]:
        return '9'


def decoder(converted_bin, shift_size):
    cnt = 0
    mux = 7
    decoded_result = ''
    while cnt < 8:
        if cnt == 0:
            if shift_size == 1:
                temp_bin = converted_bin[-mux * (cnt + 1):]
            else:
                temp_bin = converted_bin[-mux * (cnt + 1) -shift_size + 1: -shift_size + 1]
        else:
            temp_bin = converted_bin[-mux * (cnt + 1) - shift_size + 1: -mux * cnt -shift_size + 1]

        try:
            temp_ratio = check_ratio(temp_bin, mux)
            decoded_result = convert_func(temp_ratio) + decoded_result
            cnt += 1
        except:  # 오류 나면
            mux = mux + 7  # 7, 14, 21...
            cnt = 0  # 뒤로 다시 돌아감

    last_index = -mux * (cnt) - shift_size
    return decoded_result, last_index


def decoding(row, raw_password):
    # hex -> bin
    converted_bin = ''
    for i in raw_password:
        converted_bin += convert_dict[i]

    # 56자리 시도 -> 56자리 실패 -> 112 자리 시도 -> 112 자리 성공 -> 검증
    # 해독
    decoded_result_lst = []
    converted_bin = converted_bin.rstrip('0')
    bin_length = len(converted_bin)
    i = 1
    while i < bin_length:
        if converted_bin[-i] == '1':
            if arr[row - 1][(bin_length - i)//4] == '0' and arr[row + 1][(bin_length - i)//4] != '0':
                decoded_result, last_index = decoder(converted_bin, i)
                decoded_result_lst.append(decoded_result)
                i = i - last_index
            else:
                i += 1

        else:
            i += 1

    return decoded_result_lst


def validation(temp_num):
    num_arr = [int(x) for x in temp_num]
    odd_sum = num_arr[0] + num_arr[2] + num_arr[4] + num_arr[6]
    even_sum = num_arr[1] + num_arr[3] + num_arr[5]
    validation_num = num_arr[7]
    decoded_sum = odd_sum * 3 + even_sum + validation_num

    if not decoded_sum % 10:
         return odd_sum + even_sum + validation_num
    else:
         return 0


for tc in range(test_case):
    r, c = map(int, input().split())
    arr = ['' for _ in range(r)]
    for i in range(r):
        arr[i] = input().rstrip()

    # 암호 끝점 찾기
    raw_password = ''
    flag = 0
    total = 0
    for i in range(r):
        for j in range(c - 1, -1, -1):
            if arr[i][j] != '0':  # 0이 아니면 암호임
                if arr[i - 1][j] == '0' and arr[i + 1][j] != '0':
                    temp_raw_password = arr[i][0:j + 1]
                    result_lst = decoding(i, temp_raw_password)
                    for result in result_lst:
                        total += validation(result)
                    break

    print(f'#{tc+1} {total}')
