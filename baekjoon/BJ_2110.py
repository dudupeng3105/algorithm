import sys
input = sys.stdin.readline


def det(d):
    # d 만큼의 거리 차이를 두면 c개 만큼 공유기를 설치할 수 있는가?
    global c
    # 제일 왼쪽 집부터 가능한 많이 설치해본다.
    # d 만큼 거리를 두면서 최대로 설치한 개수와 c를 비교
    cnt = 1
    last = arr[1]
    for i in range(2, n+1):
        if arr[i] - last >= d:  # 테스트 해보려는 d(간격)보다 큰 경우에 설치함
            # d 보다만 크면됨 왜냐면 d보다 크면 가장 인접한 두 공유기 사이의 거리가
            # 최소는 d는 만족하니까
            cnt += 1
            last = arr[i]

    if cnt >= c:  # 최소 d 간격으로 뒀을 때 원하는 공유기의 수를 만족하는가?
        # 만족하면
        return True
    else:
        # 안하면
        return False


n, c = map(int, input().split())
arr = [0]
for i in range(n):
    arr.append(int(input()))

# 정렬
arr.sort()

l = 1
# 좌표 10억까지 가능
r = arr[-1]
ans = 0
# 이분탐색으로 빠르게 찾아보자(좌표가 너무 커서 이분탐색안하면 시간초과남)
while l <= r:
    mid = (l+r)//2
    if det(mid):  # True 라고 끝나는게 더 큰 거 찾아봄(최대 거리니까)
        ans = mid
        l = mid + 1
    else:
        r = mid - 1

print(ans)