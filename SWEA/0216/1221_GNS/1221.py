import sys

sys.stdin = open("test_input.txt")
num_str = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

test_case = int(input())
for _ in range(1, test_case + 1):
    tc, length = input().rstrip().split()
    num_cnt = [0 for x in range(10)]
    length = int(length)
    num_seq = input()
    for i in range(length):
        temp_str_num = num_seq[4 * i:4 * i + 3]  # 3자리씩 읽음
        for index, value in enumerate(num_str):
            if value == temp_str_num:
                num_cnt[index] += 1

    print(tc)
    for j in range(10):
        for _ in range(num_cnt[j]):
            print(num_str[j], end=' ')

    print()
