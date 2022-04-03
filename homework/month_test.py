def selectionsort(arr):
    n = len(arr)
    for i in range(n):
        min_i = i
        # 최솟값을 찾아 계속 앞으로 하나씩 보내는 개념
        for j in range(i + 1, n):
            if arr[j] < arr[min_i]:
                min_i = j
        arr[min_i], arr[i] = arr[i], arr[min_i]

    return arr


def selectionsort_recur(arr):
    n = len(arr)
    if n == 1:
        return arr
    min_i = 0
    # 최솟값을 찾아 계속 앞으로 하나씩 보내는 개념
    for j in range(1, n):
        if arr[j] < arr[min_i]:
            min_i = j
    arr[min_i], arr[0] = arr[0], arr[min_i]

    return [arr[0]] + selectionsort_recur(arr[1:])


# def merge_sorted(arr1, arr2):
#     sorted_arr = []
#     i, j = 0, 0
#     while i < len(arr1) and j < len(arr2):
#         if arr1[i] < arr2[j]:
#             sorted_arr.append(arr1[i])
#             i += 1
#         else:
#             sorted_arr.append(arr2[j])
#             j += 1
#
#     while i < len(arr1):
#         sorted_arr.append(arr1[i])
#         i += 1
#     while j < len(arr2):
#         sorted_arr.append(arr2[j])
#         j += 1
#
#     return sorted_arr
#
#
# def mergesort(arr):
#     if len(arr) < 2:
#         return arr[:]
#     else:
#         middle = len(arr) // 2
#         l1 = mergesort(arr[:middle])
#         l2 = mergesort(arr[middle:])
#         return merge_sorted(l1, l2)

def merge_sorted(arr1, arr2):
    result_arr = []
    i, j = 0, 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            result_arr.append(arr1[i])
            i += 1
        else:
            result_arr.append(arr2[j])
            j += 1

    while i < len(arr1):
        result_arr.append(arr1[i])
        i += 1
    while j < len(arr2):
        result_arr.append(arr2[j])
        j += 1

    return result_arr


def mergesort(arr):
    if len(arr) < 2:
        return arr[:]
    else:
        middle = len(arr) // 2
        l1 = mergesort(arr[:middle])
        l2 = mergesort(arr[middle:])
        return merge_sorted(l1, l2)


unsorted_lst = [12, 4, 3, 1, 15, 45, 33, 21, 10, 2]
print(unsorted_lst)
sorted_lst = selectionsort(unsorted_lst)
print(sorted_lst)

sorted_lst = selectionsort_recur(unsorted_lst)
print(sorted_lst)

sorted_lst = mergesort(unsorted_lst)
print(sorted_lst)

print('######################재귀 호출을 통한 순열 생성 #######################')


def perm(n, k):
    if n == k:
        print(p)
    else:
        for i in range(n, k):
            p[n], p[i] = p[i], p[n]
            # print('#', p)
            perm(n + 1, k)
            p[n], p[i] = p[i], p[n]


def perm_2(n, k):
    if n == k:
        print(p2)
        return
    else:
        for i in range(k):
            if not used[i]:
                p2.append(arr_perm[i])
                used[i] = True
                perm_2(n + 1, k)
                used[i] = False
                p2.pop()


p = [1, 2, 3]
perm(0, 3)
print('##########################')
arr_perm = [1, 2, 3, 4]

p2 = []
used = [0 for _ in range(len(arr_perm))]
perm_2(0, 4)

print('############ 바이너리 카운트 부분집합 생성##############')
arr = [3, 6, 7]
n = len(arr)

for i in range(0, 1 << n):
    for j in range(0, n):
        if i & (1 << j):
            print(f'{arr[j]}', end='')
    print()

print('############ 재귀 호출을 이요한 조합 생성 알고리즘##############')


def comb(n, r):
    if r == 0:
        print(tr)
    elif n < r:
        return
    else:
        tr[r - 1] = arr[n - 1]
        comb(n - 1, r - 1)
        comb(n - 1, r)


arr = [1, 2, 3, 4, 5]
k = 3
tr = [0 for _ in range(k)]
comb(5, k)

print('############ 퀵 정렬 ##############')


def quick(arr, l, r):
    if l < r:
        s = partition(arr, l, r)
        # s를 기준으로 나누고 재귀
        quick(arr, l, s - 1)
        quick(arr, s + 1, r)


def partition(arr, l, r):
    # 피봇을 가장 왼쪽으로 선택
    p = arr[l]
    i, j = l, r
    # i 와 j가 교차할 때 까지
    while i <= j:
        #  i 는 피봇보다 큰 값, j 는 작은 값을 찾아감
        while i <= j and arr[i] <= p:
            i += 1
        while i <= j and arr[j] >= p:
            j -= 1
        # 반복을 돌렸는데도 j가 더 큰 상황이면 두 원소를 바꿔줌 (i는 피봇보다 크고 j 는 작음)
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    # 만약에 교차한다면 수정하기 전 왼쪽 값(피폿)과 j(피봇보다 작음) 를 바꿈
    arr[l], arr[j] = arr[j], arr[l]
    # j는 자기 위치를 찾음 (왜냐면 왼쪽은 다 작은값, 오른쪽은 다 큰 값이라)
    return j


def part(arr, l, r):
    # arr에 i+1번째 인덱스에 기준값(r)보다 큰 수가 들어있다.
    # 다르게 말하면 i+1 이전엔 중간값 r보다 큰 수가 없다
    i = l - 1
    for j in range(l, r + 1):
        if arr[j] < arr[r]:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[r] = arr[r], arr[i + 1]
    # 기준값의 위치를 반환
    return i + 1


def quick_sort_2(arr, l, r):
    # 길이가 2이상일때만
    if l < r:
        # part함수에서 기준점 기준으로 큰값들 작은값들 나눠줌
        # 기준점 기준으로 나눠진 두 구간의 기준점을 찾고 또 찾고 ~~~
        s = part(arr, l, r)
        quick_sort_2(arr, l, s - 1)
        quick_sort_2(arr, s + 1, r)


def quicksort_3(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[-1]
        smaller, equal, larger = [], [], []
        for num in arr:
            if num < pivot:
                smaller.append(num)
            elif num == pivot:
                equal.append(num)
            else:
                larger.append(num)

        return quicksort_3(smaller) + equal + quicksort_3(larger)


unsorted_lst = [12, 4, 3, 1, 15, 45, 33, 21, 10, 2]
print(quick(unsorted_lst, 0, len(unsorted_lst) - 1))
print(unsorted_lst)
unsorted_lst = [12, 4, 3, 1, 15, 45, 33, 21, 10, 2]
print(quick_sort_2(unsorted_lst, 0, len(unsorted_lst) - 1))
print(unsorted_lst)
unsorted_lst = [12, 4, 3, 1, 15, 45, 33, 21, 10, 2]
print(quicksort_3(unsorted_lst))

print('############ 이진 탐색 ##############')


def binary_search(target, data):
    data.sort()
    start = 0
    end = len(data) - 1

    while start <= end:
        mid = (start + end) // 2

        if data[mid] == target:
            return mid  # 함수를 끝내버린다.
        elif data[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return None


arr = [1, 2, 3, 4, 5, 6, 7]
print(binary_search(3, arr))
