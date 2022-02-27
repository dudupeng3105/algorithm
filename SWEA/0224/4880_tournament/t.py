import sys
sys.stdin = open("test.txt")


#인덱스를 받자
def RSP(idx_a, idx_b) :
    global tournamant_tree
    #무승부
    if tournamant_tree[idx_a] == tournamant_tree[idx_b] :
        return idx_a
    #가위
    elif tournamant_tree[idx_a] == 1 :
        if tournamant_tree[idx_b] == 2 :
            return idx_b
        elif tournamant_tree[idx_b] == 3 :
            return idx_a
    #바위
    elif tournamant_tree[idx_a] == 2 :
        if tournamant_tree[idx_b] == 3 :
            return idx_b
        elif tournamant_tree[idx_b] == 1 :
            return idx_a
    #보
    else :
        if tournamant_tree[idx_b] == 1 :
            return idx_b
        elif tournamant_tree[idx_b] == 2 :
            return idx_a


def partition(L, R):
    global tournamant_tree
    if len(tournamant_tree[L:R+1]) <= 2:
        winner = RSP(L, R)
        #winner는 인덱스 값이다
        return winner
    else :
        mid = (L+R)//2
        a = partition(L, mid)
        b = partition(mid+1, R)
        winner = RSP(a, b)
        return winner


tc = int(input())

for t in range(tc):
    n = int(input())
    tournamant_tree = list(map(int, input().split()))
    result = partition(0, n-1)
    print(f'#{t+1} {result+1}')