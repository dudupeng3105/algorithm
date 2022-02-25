import sys
sys.stdin = open("test.txt")

test_case = int(input())
for tc in range(1, test_case + 1):
    n = int(input())
    arr = list(map(int, input().split()))
    result = -1  # 없는 경우 -1 나오게 하려고
    # 조합
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            temp = arr[i] * arr[j]
            temp_str = str(temp)
            flag = 1
            for k in range(len(temp_str)-1):
                if int(temp_str[k]) > int(temp_str[k+1]):  # 단조 증가 아닐 때
                    flag = 0
                    break
                else:
                    continue

            if flag:
                if temp > result:
                    result = temp

    print(f'#{tc} {result}')