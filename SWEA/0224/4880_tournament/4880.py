import sys
sys.stdin = open("test.txt")


def rock_paper_scissors(human1, human2):
    # human1 = [(a, b)]
    # human1[0] = (a,b)
    # human1[0][1] = b --> 왼쪽사람이 낸 거
    # a => 학생 번호
    #  1.가위 2.바위 3.보
    if human1[0][1] == 1:  # 가위
        if human2[0][1] == 1:  # 비김
            return human1
        elif human2[0][1] == 2:  # 졌음
            return human2
        else:  # 이겼음
            return human1

    elif human1[0][1] == 2:  # 바위
        if human2[0][1] == 2:  # 비김
            return human1
        elif human2[0][1] == 3:  # 졌음
            return human2
        else:  # 이겼음
            return human1

    elif human1[0][1] == 3:  # 보
        if human2[0][1] == 3:  # 비김
            return human1
        elif human2[0][1] == 1:  # 졌음
            return human2
        else:  # 이겼음
            return human1


def divide_conquer(arr):

    start = 0
    end = len(arr) -1

    if start == end:  # 한 조각 되면 리턴
        return arr

    mid = (start + end) // 2

    left_block = divide_conquer(arr[start:mid+1])  # 한 조각 까지 가면 그 값 리턴
    right_block = divide_conquer(arr[mid+1:])  # 한 조각 까지 가면 그 값 리턴

    return rock_paper_scissors(left_block, right_block)  # 조각끼리 가위바위보하고 -> 한 조각 리턴


test_case = int(input())
for tc in range(1, test_case+1):
    n = int(input())
    given_rps = list(map(int, input().split()))
    arr = [(x+1, given_rps[x]) for x in range(n)]  # (a, b)  # a = 학생번호, b = 뭐 냈는지
    victory = divide_conquer(arr)
    print(f'#{tc} {victory[0][0]}')