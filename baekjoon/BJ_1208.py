import sys
from itertools import combinations

input = sys.stdin.readline


def cal_sub_sum_seq(seq):
    sub_sum_seq = []

    for i in range(1, len(seq) + 1):
        for combi in combinations(seq, i):
            sub_sum_seq.append(sum(combi))

    sub_sum_seq.sort()
    return sub_sum_seq


n, s = map(int, input().split())
arr = list(map(int, input().split()))
if n == 1:
    if arr[0] == s:
        print(1)
    else:
        print(0)
else:
    arr1 = arr[:n // 2]
    arr2 = arr[n // 2:]
    # print(arr1, arr2)
    # 부분합 구하기
    sub_sum_seq1 = cal_sub_sum_seq(arr1)
    sub_sum_seq2 = cal_sub_sum_seq(arr2)
    # print(sub_sum_seq1)
    # print(sub_sum_seq2)
    left_pointer = 0
    right_pointer = len(sub_sum_seq2) - 1
    temp_sum = sub_sum_seq1[left_pointer] + sub_sum_seq2[right_pointer]
    cnt = 0
    # 왼쪽수열의 합으로만 가능한 경우
    cnt += sub_sum_seq1.count(s)
    # 오른쪽수열의 합으로만 가능한 경우
    cnt += sub_sum_seq2.count(s)
    # print(cnt)
    while left_pointer < len(sub_sum_seq1) and right_pointer >= 0:
        temp_sum = sub_sum_seq1[left_pointer] + sub_sum_seq2[right_pointer]
        if temp_sum == s:
            lv = sub_sum_seq1[left_pointer]
            rv = sub_sum_seq2[right_pointer]
            lc = 0
            rc = 0
            while left_pointer < len(sub_sum_seq1) and lv == sub_sum_seq1[left_pointer]:
                lc += 1
                left_pointer += 1
            while right_pointer >= 0 and rv == sub_sum_seq2[right_pointer]:
                rc += 1
                right_pointer -= 1
            cnt += (lc * rc)

        elif temp_sum > s:
            right_pointer -= 1

        else:  # temp_sum < s
            left_pointer += 1

    print(cnt)
