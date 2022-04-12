n, m = map(int, input().split())

if n >= 3:
    if m >= 7:
        print(4 + (m - 6))
    else:
        ans_lst = [0, 1, 2, 3, 4, 4, 4]
        print(ans_lst[m])
elif n == 1:
    print(1)
elif n == 2:
    if m <= 2:
        print(1)
    elif 3 <= m < 5:
        print(2)
    elif 5 <= m < 7:
        print(3)
    else:
        print(4)
