# HW 1
print(dir(__builtins__))


# abs(), all(), any(), bool(), complex(), filter(), id(), globals() 등등

# HW 2
def get_middle_char(given_str):
    n = len(given_str)
    if n % 2 == 0:  # 길이 짝수
        return given_str[n // 2 - 1: n // 2 + 1]
    else:
        return given_str[n // 2]


print(get_middle_char('ssafy'))
print(get_middle_char('coding'))


# HW 3
def ssafy(name, location='서울'):
    print(f'{name}의 지역은 {location}입니다.')


# (1)
ssafy('허준')

# (2)
ssafy(location='대전', name='철수')

# (3)
ssafy('영희', location='광주')


# (4) 정답
# ssafy(name='철수', '구미')
# 키워드 아규먼트 다음에 포지셔널 아규먼트 사용 불가

# HW 4
def my_func(a, b):
    c = a + b
    print(c)


result = my_func(3, 7)
print('result:', result)

# output : 10


# HW 5
def my_avg(*args):
    total = 0
    cnt = 0
    for num in args:
        total = total + num
        cnt = cnt + 1

    return total / cnt


print(my_avg(77, 83, 95, 80, 70))


# WS 1
def list_sum(integer_list):
    total = 0

    for num in integer_list:
        total = total + num

    return total


print(list_sum([1, 2, 3, 4, 5]))


# WS 2
def dict_list_sum(arr):
    total = 0

    for i in arr:
        total = total + i['age']

    return total


print(dict_list_sum([{'name': 'kim', 'age': 12},
                     {'name': 'lee', 'age': 4}]))


# WS 3
def all_list_sum(arr):
    total = 0

    for element in arr:
        for num in element:
            total = total + num

    return total


print(all_list_sum([[1], [2, 3], [4, 5, 6], [7, 8, 9, 10]]))
