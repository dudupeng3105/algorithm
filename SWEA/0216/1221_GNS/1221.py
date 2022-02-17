import sys

sys.stdin = open("test_input.txt")
num_str = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

test_case = int(input())
for _ in range(1, test_case + 1):
    tc, length = input().rstrip().split()
    num_cnt = [0 for x in range(10)]  # 숫자별 등장횟수를 세기 위한 리스트
    length = int(length)  # 숫자의 개수
    num_seq = input()

    for i in range(length):
        temp_str_num = num_seq[4 * i:4 * i + 3]  # 3자리씩 읽음(4의 배수인 이유는 3자리마다 공백있으므로)
        for index, value in enumerate(num_str):  # ex) index: 2 value: "TWO"
            if value == temp_str_num:  # "TWO" == "TWO"
                num_cnt[index] += 1  # num_cnt[2] += 1

    print(tc)
    for j in range(10):
        for _ in range(num_cnt[j]):  # num_cnt[1] = 490 이면 "ONE"을 490번 출력함
            print(num_str[j], end=' ')  # 숫자 단어 사이에 공백 처리

    print()
