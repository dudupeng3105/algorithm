# 2022 01 18 homework, WORKSHOP
# HW 1
# mutable => List, Dictinary,
# immutalbe => String, Range, set, Tuple

# HW 2
odd_number = [x for x in range(1, 51) if not x % 2 == 0]
# odd_number = list(range(1,51,2))
print(odd_number)

# HW 3
key_list = ['사람1', '사람2', '사람3', '사람4', '사람5']
value_list = [25, 29, 30, 21, 27]
student_dict = dict(zip(key_list, value_list))
print(student_dict)

# HW 4
n, m = 5, 9
for i in range(m):
    print('*' * n)

# HW 5
temp = 36.5
print('입실 불가') if temp >= 37.5 else print('입실 가능')

# HW 6
scores = [80, 89, 99, 83]
total = 0
for i in scores:
    total += i

print(total/len(scores))

# WS 1

N = int(input())
for num in range(1, N):
    if N % num == 0:
        print(num, end=' ')
print(N)

# WS 2

numbers = [85,72,38,80,69,65,68,96,22,49,67,51,61,63,87,66,24,80,83,71,60,64,52,90,60,49,31,23,99,94,11,25,24]
N = len(numbers)
num_list = sorted(numbers)
mid_num = num_list[int((N-1)/2)]
print(mid_num)

# WS 3

N = int(input())
num_list = list(range(1, N+1))
for i in range(N):
    print(' '.join(map(str, num_list[:i+1])))

# practice 1
