#  남학생은 자기 배수 스위치 클릭
def male_operator(array, num):
    for i in range(len(array)):
        if (i + 1) % num == 0:  # 배수 이면
            array[i] = (array[i] + 1) % 2
        else:
            continue

    return array


#  여학생은 자기 숫자 중심 좌우 대칭 구간
def female_operator(array, num):
    num = num - 1
    i = 0
    while (num - i) >= 0 and (num + i) < switch_num:
        if array[num - i] == array[num + i]:
            i += 1
            continue
        else:
            break

    i -= 1  # 위에서 1더한 상태로 실패하기 때문에 1빼줌
    # 상태변경
    for j in range(num - i, num + i + 1):
        array[j] = (array[j] + 1) % 2

    return array


switch_num = int(input())
arr = [0 for _ in range(switch_num)]
arr = list(map(int, input().split()))
test_case = int(input())
for _ in range(test_case):
    s, number = map(int, input().split())
    if s == 1:  # 남자
        arr = male_operator(arr, number)

    else:  # 여자
        arr = female_operator(arr, number)

line_num = ((switch_num - 1) // 20 ) + 1 # 21개면 넘어감

for i in range(line_num):  # 21개면 넘어감
    print(*arr[20 * i:20 * (i + 1)])
