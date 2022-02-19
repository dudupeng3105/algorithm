import sys
sys.stdin = open("test.txt")


def selection_sort(arr, length):

    for i in range(length):
        min_index = i
        for j in range(i+1, length):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


test_case = int(input())
for tc in range(1, test_case+1):
    n = int(input())
    num_lst = list(map(int, input().split()))

    num_lst = selection_sort(num_lst, n)
    print(f'#{tc}', end=' ')
    print(*num_lst)
