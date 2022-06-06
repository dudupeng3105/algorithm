import sys
input = sys.stdin.readline

t = int(input())

# a 부분합 구하기
n = int(input())
a = list(map(int, input().split()))

subtotal_a = []
for i in range(len(a)):
    temp_subtotal = 0
    for j in range(i, len(a)):
        temp_subtotal += a[j]
        subtotal_a.append(temp_subtotal)

subtotal_a.sort()
# print(subtotal_a)

# b 부분합 구하기
m = int(input())
b = list(map(int, input().split()))

subtotal_b = []
for i in range(len(b)):
    temp_subtotal = 0
    for j in range(i, len(b)):
        temp_subtotal += b[j]
        subtotal_b.append(temp_subtotal)


subtotal_b.sort()
# print(subtotal_b)

left_point = 0  # a포인터
right_point = len(subtotal_b) - 1  # b포인터
cnt = 0
temp_sum = subtotal_a[left_point] + subtotal_b[right_point]
while True:
    if temp_sum == t:
        # cnt += 1 나중에 더함
        # print(subtotal_a[left_point], subtotal_b[right_point])

        left_num = subtotal_a[left_point]
        right_num = subtotal_b[right_point]
        a_cnt = 1
        b_cnt = 1
        # b 중복체크
        while True:
            right_point -= 1
            if right_point < 0:
                break
            if subtotal_b[right_point] == right_num:
                b_cnt += 1
            else:
                break
        # a 중복체크
        while True:
            left_point += 1
            if left_point > len(subtotal_a) - 1:
               break
            if subtotal_a[left_point] == left_num:
                a_cnt += 1
            else:
                break
        cnt += a_cnt * b_cnt
        if right_point < 0 or left_point > len(subtotal_a) - 1:
            break
        temp_sum = subtotal_a[left_point] + subtotal_b[right_point]

    elif temp_sum > t:
        right_point -= 1
        if right_point < 0:
            break
        temp_sum = subtotal_a[left_point] + subtotal_b[right_point]
    else:  # temp_sum < n
        left_point += 1
        if left_point > len(subtotal_a) - 1:
            break
        temp_sum = subtotal_a[left_point] + subtotal_b[right_point]

print(cnt)
