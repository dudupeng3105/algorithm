##########1107번####################
possible_button = [0,1,2,3,4,5,9]
want_channel = 5457
now_channel = 100
cnt = 0
def good_case(want_channel, N, cnt):
    head_number = want_channel // (10**N)
    if head_number in possible_button:
        cnt += 1 # 1번 클릭
        want_channel = want_channel % (10**N)
        bad_case_flag = 0
        N = N -1
    else:
        bad_case_flag = 1

    return want_channel, cnt, bad_case_flag, N

def bad_case(want_channel, N, cnt):
    ## 남은 수 올라가면서
    head_number = want_channel // (10 ** N)
    head_number += 1
    if head_number not in possible_button:
        head_number += 1


    ## 남은 수 내려가면서