tc = int(input())

for _ in range(tc):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()    
    cnt = 0
    start = 0
    end = 0
    while start < N:
        if A[start] <= B[end]:                   
            cnt += end
            start += 1
            #print('if',start, end, cnt)  
            if start == N:
                break
        else:            
            end += 1
            if end == M:
                end = M-1                   
                cnt += end + 1 
                start += 1
                #print('else',start, end, cnt)               
    
    print(cnt)