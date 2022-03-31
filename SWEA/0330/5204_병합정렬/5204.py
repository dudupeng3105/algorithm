def merge_sorted(arr1, arr2):
    global cnt
    if arr1[-1] > arr2[-1]:
        cnt += 1
    sorted_arr = []
    i, j = 0, 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            sorted_arr.append(arr1[i])
            i += 1
        else:
            sorted_arr.append(arr2[j])
            j += 1

    while i < len(arr1):
        sorted_arr.append(arr1[i])
        i += 1
    while j < len(arr2):
        sorted_arr.append(arr2[j])
        j += 1

    return sorted_arr


def mergesort(arr):
    if len(arr) < 2:
        return arr[:]
    else:
        middle = len(arr) // 2
        l1 = mergesort(arr[:middle])
        l2 = mergesort(arr[middle:])
        return merge_sorted(l1, l2)


test_case = int(input())
for tc in range(1, test_case+1):
    n = int(input())
    unsorted_list = list(map(int, input().split()))
    cnt = 0
    sorted_list = mergesort(unsorted_list)
    print(f'#{tc} {sorted_list[n//2]} {cnt}')