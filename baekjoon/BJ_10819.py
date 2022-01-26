# 다음 순열
def next_permutaion(src):
    n = len(src)
    i = n-1
    while src[i-1] >= src[i]: # src[i] > src[i-1] 인 i 찾음
        i -= 1
    if i <= 0: return -1

    j = n - 1 
    # scr[i-1] 보다 큰 인덱스 중 src[i-1]보다 값은 크지만 차이는 가장 작은놈 찾음
    while src[i-1] >= src[j]: 
        j -= 1
    src[i-1], src[j] = src[j], src[i-1] # swap

    j = n-1
    while i < j:
        src[i], src[j] = src[j], src[i]
        i += 1
        j -= 1
    return src

def difference_max(lst):
    result = 0
    lst.sort()    
    # result 초기화
    for i in range(n - 1):
        result += abs(lst[i] - lst[i+1])

    # 순열 모두 계산
    lst = next_permutaion(lst)    
    while lst != -1:        
        temp = 0        
        for i in range(n - 1):
            temp += abs(lst[i] - lst[i+1])
        
        if result < temp:
            result = temp
        
        lst = next_permutaion(lst)

    return result

n = int(input())
src = list(map(int, input().split()))        
print(difference_max(src))