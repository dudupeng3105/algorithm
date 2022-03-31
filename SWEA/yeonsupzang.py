from itertools import permutations
from pprint import pprint

t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    # pprint(arr)

    permu = [x for x in range(n)]
    # print(permu)

    minn = 10e9
    for this_lst in permutations(permu, n):
        #print(this_lst)
        summ = 0
        row = 0
        for factory in this_lst:
            summ += arr[row][factory]
            if summ >= minn:
                break
            row += 1
            # print(summ)
        if summ < minn:
            minn = summ

    print(f'#{tc} {minn}')