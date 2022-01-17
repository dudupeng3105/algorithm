# 2072 홀수만 더하기
# test_case = int(input())
# for i in range(test_case):
#     num_list = list(map(int, input().split(' ')))
#     sum_num = 0
#     for num in num_list:
#         if num % 2 == 0:
#             continue
#         sum_num = sum_num + num
#     print(f'#{i+1} {sum_num}')


# 2071 평균값 구하기
# test_case = int(input())
# for i in range(test_case):
#     num_list = list(map(int, input().split(' ')))
#     sum_num = 0
#     avg_num = 0
#     for num in num_list:
#         sum_num = sum_num + num
#     avg_num = round(sum_num/len(num_list))
#     print(f'#{i+1} {avg_num}')


# 2070 큰 놈, 작은 놈, 같은 놈
# test_case = int(input())
# for i in range(test_case):
#     a, b = map(int, input().split(' '))
#     if a > b:
#         print(f'#{i + 1} >')
#     elif a < b:
#         print(f'#{i + 1} <')
#     else:
#         print(f'#{i + 1} =')

# 2068 최대수 구하기
# test_case = int(input())
# for i in range(test_case):
#     num_list = list(map(int, input().split(' ')))
#     max_num = 0
#     for num in num_list:
#         max_num = max(max_num, num)
#     print(f'#{i+1} {max_num}')

# 2063 중간값 찾기기
# N = int(input())
# num_list = list(map(int, input().split(' ')))
# num_list = sorted(num_list)
# mid_num = num_list[int((N - 1) / 2)]
# print(mid_num)

# 2058 자릿수 더하기
# N_str = input()
# sum_num = 0
# for x in N_str:
#     sum_num = sum_num + int(x)
# print(sum_num)

# 2056 연월일 달력
# test_case = int(input())
# list_31 = [x for x in range(1,32)]
# list_30 = [y for y in range(1,31)]
# list_28 = [z for z in range(1,29)]
# flag = 0
# for i in range(test_case):
#     num_list = input()
#     year = num_list[0:4]
#     month = int(num_list[4:6])
#     day = int(num_list[6:])
#     if 1 <= month <= 12:
#         if month in [1,3,5,7,8,10,12]:
#             if int(day) in list_31:
#                 print(f"#{i+1} {year}/{num_list[4:6]}/{num_list[6:]}")
#             else:
#                 print(f"#{i+1} -1")
#         elif month in [4,6,9,11]:
#             if int(day) in list_30:
#                 print(f"#{i+1} {year}/{num_list[4:6]}/{num_list[6:]}")
#             else:
#                 print(f"#{i+1} -1")
#         else:  #2월
#             if int(day) in list_28:
#                 print(f"#{i+1} {year}/{num_list[4:6]}/{num_list[6:]}")
#             else:
#                 print(f"#{i+1} -1")
#     else:
#         print(f"#{i + 1} -1")


# 2050 알파벳을 숫자로 변환
# num_list = [x for x in range(1, 27)]
# alpha_list = [chr(y) for y in range(ord('A'), ord('Z') + 1)]
# alpha_num_dict = dict(zip(alpha_list, num_list))
# given_string = list(input())
# for i in range(len(given_string)-1):
#     print(alpha_num_dict[given_string[i]], end=' ')
#
# print(alpha_num_dict[given_string[len(given_string)-1]])

# 2047. 신문 헤드라인
# given_string = input()
# print(given_string.upper())

# 2046. 스탬프 찍기
# N = int(input())
# print('#' * N)

# 2043. 서랍 비밀번호
# P, K = map(int, input().split(' '))
# print(P-K+1)

# 2029 몫과 나머지 출력하기
# test_case = int(input())
# for i in range(test_case):
#     a, b = map(int, input().split(' '))
#     print(f'#{i+1} {a//b} {a%b}')

# 2027 대각선 출력하기
# print('#++++')
# print('+#++')
# print('++#++')
# print('+++#+')
# print('++++#')

# 2025 N줄 덧셈
# N = int(input())
# sum_num = 0
#
# for num in range(1, N+1):
#     sum_num = sum_num + num
#
# print(sum_num)

# 1938 아주 간단한 계산기
# a, b = map(int, input().split(' '))
# print(a+b)
# print(a-b)
# print(a*b)
# print(a//b)

# 1933 간단한 N의 약수
# N = int(input())
# for num in range(1, N):
#     if N % num == 0:
#         print(num, end=' ')
# print(N)

# 1936 1대1 가위바위보
# a, b = map(int, input().split(' '))
# if a == 1:  # 가위
#     if b == 3:  # 보
#         print('A')
#     else:
#         print('B')
#
# elif a == 2:  # 바위
#     if b == 1:  # 가위
#         print('A')
#     else:
#         print('B')
#
# else:  #보
#     if b == 2: # 바위
#         print('A')
#     else:
#         print('B')

# 2019 더블더블
# N = int(input())
# num = 1
# for _ in range(N):
#     print(num, end = ' ')
#     num = num * 2
#
# print(num)

# 1545 거꾸로 출력해 보아요
# N = int(input())
# for num in range(N, 0, -1):
#     print(num, end=' ')
# print(0)