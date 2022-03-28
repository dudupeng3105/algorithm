test_case = int(input())

for tc in range(1, test_case + 1):
    n = int(input())
    last = int(n**(1/3) + 1)
    flag = 0
    for i in range(1, last+1):
        if i**3 == n:
            flag = 1
            break

    if flag:
        print(f'#{tc} {i}')
    else:
        print(f'#{tc} -1')