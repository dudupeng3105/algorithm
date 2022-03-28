test_case = int(input())

for tc in range(test_case):
    r, c = map(int, input().split())
    arr = ['' for _ in range(r)]
    for i in range(r):
        arr[i] = input()

    # 암호 끝점 찾기
    raw_password = ''
    flag = 0
    for i in range(r):
        for j in range(c-1, -1, -1):
            if arr[i][j] == '1':
                raw_password = arr[i][j-55:j+1]
                flag = 1
                break
        if flag:
            break

    decode_dict = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4, '0110001': 5, '0101111': 6, \
                   '0111011': 7, '0110111': 8, '0001011': 9}

    # 해독
    decoded_sum = 0
    odd_sum = 0
    even_sum = 0
    for i in range(7):  # 0 ~ 5
        if i % 2:  # 짝수(7자리라 앞에서 읽으면 짝수임)
            even_sum += decode_dict[raw_password[7 * i:7 * (i + 1)]]
        else:
            odd_sum += decode_dict[raw_password[7 * i:7 * (i + 1)]]
    validation_num = decode_dict[raw_password[49: 56]]
    decoded_sum = odd_sum*3 + even_sum + validation_num
    if not decoded_sum % 10:
        print(f'#{tc + 1} {odd_sum + even_sum + validation_num}')
    else:
        print(f'#{tc + 1} 0')