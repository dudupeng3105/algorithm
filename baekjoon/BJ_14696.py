n = int(input())
for _ in range(n):
    cnt_1 = [0, 0, 0, 0]
    cnt_2 = [0, 0, 0, 0]

    a1 = list(map(int, input().split()))
    for i in a1[1:]:
        cnt_1[i - 1] += 1

    a2 = list(map(int, input().split()))
    for i in a2[1:]:
        cnt_2[i - 1] += 1

    flag = 1
    for k in range(3, -1, -1):
        if cnt_1[k] > cnt_2[k]:
            print('A')
            flag = 0
            break
        if cnt_1[k] < cnt_2[k]:
            print('B')
            flag = 0
            break

    if flag:
        print('D')
