## 가장 큰 것 출력
import sys
input = sys.stdin.readline

while True:
    try:
        x = int(input())
        n = int(input())
        arr = []
        for _ in range(n):
            a = int(input())
            arr.append(a)

        arr.sort()
        # print(arr)

        s = 0
        e = len(arr) - 1
        target_x = x * 10000000  # 10 ^ 7

        flag = False
        while s < e:
            temp_sum = arr[s] + arr[e]
            if temp_sum == target_x:
                flag = True
                break
            elif temp_sum > target_x:
                e -= 1
            elif temp_sum < target_x:
                s += 1

        if flag:
            print(f'yes {arr[s]} {arr[e]}')
        else:
            print('danger')
    except:
        break
