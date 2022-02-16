# KMP 알고리즘
# 필요한 함수 -> 실패함수
# 실패함수 -> prefix와 와 suffix가 일치하는 최대길이
# 실패함수를 통해서 일정 부분의 비교 건너뜀
def failure_function(pattern):
    f = [0]  # 실패함수 초기화
    i = 1
    j = 0
    m = len(pattern)
    while i < m:
        if pattern[i] == pattern[j]:
            f.append(j + 1)  # failure function 값 저장
            i += 1
            j += 1
        elif j > 0:
            j = f[j - 1]  # use failure function to shift pattern
        else:
            f.append(0)  # no match
            i += 1

    return f


def kmp(test, pattern):
    f = failure_function(pattern)
    i = 0
    j = 0
    n = len(test)
    m = len(pattern)
    while i < n:
        if test[i] == pattern[j]:  # pattern match
            if j == m - 1:
                return i - j  # match! -> test에서 패턴의 시작위치 리턴
            else:
                i = i + 1
                j = j + 1
        else:  # 불일치
            if j > 0:  # j가 이동했으면, pattern이 몇 번은 matched
                j = f[j - 1]
            else:  # 첨부터 안맞음
                i = i + 1

    return -1  # No match


def last_occurence_fucntion(pattern):
    m = len(pattern)
    # num_of_chars = 256
    last_occurence_lst = [-1] * 256 # -1이 나중에 패턴에 그 문자가 없을때\
    # 패턴의 길이만큼 이동할 수 있도록 도와줌

    # 값 채우기, 앞에서 부터 진행하므로
    # 여러번 나와도 마지막에 나온 인덱스가 저장됨
    for i in range(m):
        last_occurence_lst[ord(pattern[i])] = i;

    # return
    return last_occurence_lst


def boyer_moore_huristic(test, pattern):
    m = len(pattern)
    n = len(test)

    last_occur_lst = last_occurence_fucntion(pattern)

    s = 0  # 패턴 시프트 지점(여기서부터 비교)
    while (s <= n - m):
        j = m - 1  # 패턴의 마지막 글자부터 비교함, 아래 반복문에서 패턴 틀릴때마다 j 리셋됨

        while j >= 0 and test[s + j] == pattern[j]:  # 체크 중이고, 패턴이 맞는 중
            j -= 1  # 거꾸로 읽어가며 비교함
            # s => test에서 비교중인 범위의 가장 앞쪽

        if j < 0:  # 다 체크했는데 매치했음!
            print(f'인덱스 {s}부터 패턴이 매치됨')

            if s + m < n:  # test의 길이를 넘지 않음
                # 패턴이 발견된 바로 뒤 글자가 패턴에서 마지막으로 나타나는 위치로 start 변경
                s += m - last_occur_lst[ord(test[s + m])]

            else:  # 끝에 딱맞게 패턴이 완성됨 -> s에 1더해주고 -> 가장 바깥쪽 while문 탈출
                s += 1

        else:  # 패턴이 틀린경우
            # 최소한칸 start값이 이동이고, 이번에 틀린 test의 문자(알파벳)가
            # 몇 자리 앞에서 패턴에서 나오는지 구해서 그(자리 수)만큼 start 땡겨(shift)주는 방식
            # 여기서 test의 문자가 패턴에 없으면 last_occur_list[문자] = -1 이 되고 j + 1 만큼 땡겨주게 된다.
            # 만약 j가 m-1이면 m(패턴의 길이만큼) 땡기는 것
            s += max(1, j-last_occur_lst[ord(test[s+j])])

print(kmp('abacaababaabaacabaabb', 'abaaba'))
txt = "ABAAABCD"
pat = "ABC"
boyer_moore_huristic(txt, pat)