import sys


def cal_last_occur_lst(pattern):
    m = len(pattern)
    # num_of_chars = 256, 아스키코드가 256개임
    last_occurence_lst = [-1] * 256  # -1이 나중에 패턴에 그 문자가 없을때\
    # 패턴의 길이만큼 이동할 수 있도록 도와줌

    # 값 채우기, 앞에서 부터 진행하므로
    # 여러번 나와도 마지막에 나온 인덱스가 저장됨
    for i in range(m):
        last_occurence_lst[ord(pattern[i])] = i

    # return
    return last_occurence_lst


def boyer_moore(test, pattern):
    m = len(pattern)
    n = len(test)
    last_occur_lst = cal_last_occur_lst(pattern)

    s = 0  # 패턴 시프트 지점(여기서부터 비교)
    while (s <= n - m):
        j = m - 1  # 패턴의 마지막 글자부터 비교함, 아래 반복문에서 패턴 틀릴때마다 j 리셋됨

        while j >= 0 and test[s + j] == pattern[j]:  # 체크 중이고, 패턴이 맞는 중
            j -= 1  # 거꾸로 읽어가며 비교함
            # s => test에서 비교중인 범위의 가장 앞쪽

        if j < 0:  # 다 체크했는데 매치했음!
            return 1  # 하나라도 나오면 바로 함수 리턴

        else:  # 패턴이 틀린경우
            # 최소한칸 start 값이 이동이고, 이번에 틀린 test의 문자(알파벳)가
            # 몇 자리 앞에서 패턴에서 나오는지 구해서 그(자리 수)만큼 start 땡겨(shift)주는 방식
            # 여기서 test의 문자가 패턴에 없으면 last_occur_list[문자] = -1 이 되고 j + 1 만큼 땡겨주게 된다.
            # 만약 j가 m-1이면 m(패턴의 길이만큼) 땡기는 것
            s += max(1, j-last_occur_lst[ord(test[s+j])])

    return 0


sys.stdin = open("test.txt")
test_case = int(input())
for tc in range(1, test_case + 1):
    string_1 = list(input())
    string_2 = list(input())
    if len(string_1) > len(string_2):
        pattern = string_2
        test = string_1
    else:
        pattern = string_1
        test = string_2

    print(f'#{tc} {boyer_moore(test, pattern)}')










