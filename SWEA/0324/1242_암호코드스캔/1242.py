import sys

sys.stdin = open("test_2.txt")

test_case = int(input())

# 16진수 -> 2진수를 위한 dict
convert_dict = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110', \
                '7': '0111', '8': '1000', '9': '1001', 'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101', \
                'E': '1110', 'F': '1111'}


# 코드의 숫자의 비율을 계산 ex [9:3:3:6]계산 후 -> [3: 1: 1: 2]로 바꿔줌
def check_ratio(binary_str, this_mux):
    result_ratio_lst = [1, 0, 0, 0]
    temp = binary_str[0]
    c = 0
    for i in range(1, this_mux):
        if binary_str[i] == temp:
            result_ratio_lst[c] += 1
        else:
            c += 1
            temp = binary_str[i]
            result_ratio_lst[c] += 1

    # 비율 최소화
    min_num = min(result_ratio_lst)
    while min_num > 1:
        result_ratio_lst = [x // min_num for x in result_ratio_lst]
        min_num = min(result_ratio_lst)
    return result_ratio_lst


# 비율에 맞는 숫자를 반환(암호해독을 위한 함수)
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
    cnt = 0  # 해독된 숫자의 수
    mux = 7  # 숫자하나당 = 2진수 7 자리로 시작
    decoded_result = ''  # 결과 리스트 초기화
    while cnt < 8:  # 8개 모이기 전까지 돌림
        if cnt == 0:  # cnt=0 일때는 converted_bin[-mux * (cnt + 1):] 꼴이어야 인덱싱이 바로돼서 해논 것
            if shift_size == 1:  # 처음만난 암호 일때는
                temp_bin = converted_bin[-mux * (cnt + 1):]
            else:  # 처음만난 암호가 아니면 shift(시작점 조정의 의미)를 해줘야함
                temp_bin = converted_bin[-mux * (cnt + 1) - shift_size + 1: -shift_size + 1]
        else:
            temp_bin = converted_bin[-mux * (cnt + 1) - shift_size + 1: -mux * cnt - shift_size + 1]

        # 일단 dict에 키값이 있는지 확인해보고 있으면 숫자스트링을 리스트에 붙이고
        try:  # 없으면 숫자하나당 2진수가 14개, 21개, 28개로 올려줘야함
            temp_ratio = check_ratio(temp_bin, mux)
            decoded_result = convert_func(temp_ratio) + decoded_result
            cnt += 1
        except:  # key값이 없을때 숫자하나당 2진수가 mux개가 아니였음 그럼 mux를 7 늘려준다.
            mux = mux + 7  # 7, 14, 21...
            cnt = 0  # 뒤로 다시 돌아감, 다시 시작

    last_index = -mux * cnt - shift_size  # 한 암호를 다 해독했을때 마지막점을 리턴해줌
    # 왜냐하면 이 암호 바로 앞부터 다시 체크해나가야 하니까
    return decoded_result, last_index


# 암호해독 함수
def decoding(row, raw_password):  # (해당 row, 끝자리 1부터 맨앞까지의 16진수 string)
    # 1. 먼저 16진수를 2진수 스트링으로 변환
    # hex -> bin
    converted_bin = ''
    for i in raw_password:
        converted_bin += convert_dict[i]

    # 2. 해독
    decoded_result_lst = []  # 해독된 암호를 담음 리스트 초기화
    converted_bin = converted_bin.rstrip('0')  # 암호의 2진수는 항상 1로 끝나므로 오른쪽의 0을 모두 제거
    bin_length = len(converted_bin)
    i = 1  # 거꾸로 읽어감
    # 56자리 시도 -> 56자리 실패 -> 112 자리 시도 -> 112 자리 성공 -> 검증
    while i < bin_length:  # i가 범위 벗어날때 까지
        if converted_bin[-i] == '1':  # 거꾸로 읽어가면서 2진수 1을 만나면
            # 여기서 해당 arr의 위칸이 0이고 아래칸이 0이 아닌지 확인 암호블럭의 최상단일때만 계산하므로
            # //4 를 하는이유 현재 bin_length는 16진수를 2진수로 바꾸어 길이가 * 4이므로
            if arr[row - 1][(bin_length - i) // 4] == '0' and arr[row + 1][(bin_length - i) // 4] != '0':
                decoded_result, last_index = decoder(converted_bin, i)  # 실제 해독함수로 집어넣음
                decoded_result_lst.append(decoded_result)  # 결과를 lst에 담음
                # converted_bin[-i] == '1'를 다시 시작할 위치를
                # 이미 해독한 코드의 바로 앞부터 시작할 수 있도록 조정
                i = i - last_index

            else:
                i += 1  # 한 칸씩 거꾸로 읽어가는 것

        else:
            i += 1  # 한 칸씩 거꾸로 읽어가는 것

    return decoded_result_lst


# 홀수자리합*3 + 짝수 자리 합 + 검증코드가 10의 배수인지 검증하는 함수
# 만약에 10의 배수이면 모든 자리의 합을 return, 아니면 유효하지 않으므로 0 리턴
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
            if arr[i][j] != '0':  # 0이 아니면 암호시작일 수 있음
                # 위의 칸이 0이고 아래칸이 0이 아니면 암호블럭의 최상단임
                if arr[i - 1][j] == '0' and arr[i + 1][j] != '0':
                    # 끝의 1부터 맨앞까지 가져옴
                    temp_raw_password = arr[i][0:j + 1]
                    # decoding 함수의 넣어 result_lst 받음(한 줄에 암호 2개일수도 있으니까)
                    result_lst = decoding(i, temp_raw_password)
                    for result in result_lst:
                        total += validation(result)
                    # 한 줄에서 다 탐색했으면 그 줄 탐색 필요없으므로 다음 행으로 넘어가기 위한 break
                    break

    print(f'#{tc + 1} {total}')
