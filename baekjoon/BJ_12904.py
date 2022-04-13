a = list(input())
b = list(input())

len_a = len(a)
len_b = len(b)
# b에서 a로 돌아감
while len_a != len_b:
    if b[len_b - 1] == 'A':
        b.pop()  # 그냥 빼기
    else:  # B
        b.pop()  # 빼고
        b = b[::-1]  # 뒤집기

    len_b -= 1


if a == b:
    print(1)
else:
    print(0)

