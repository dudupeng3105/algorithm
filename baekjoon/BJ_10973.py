# 이전 순열
# 사전 순으로 바로 이전에 오는 순열
N = int(input())
given_seq = list(map(int, input().split()))
prev_bottom = -1
for i in range(N-1, 0, -1): # 뒤에서 부터 찾음
    if given_seq[i-1] > given_seq[i]:
        prev_bottom = i - 1        
        break

# 자리 교환
if prev_bottom == -1:
    print(-1)
else:    
    # given_seq[prev_bottom]보다 작지만 가장 가까운 수 찾기
    for i in range(N-1, prev_bottom, -1):        
        if given_seq[prev_bottom] > given_seq[i]:            
            given_seq[prev_bottom], given_seq[i] =\
            given_seq[i], given_seq[prev_bottom]
            break        

    given_seq = given_seq[:prev_bottom + 1] + \
        sorted(given_seq[prev_bottom + 1:], reverse= True)

    print(*given_seq)
