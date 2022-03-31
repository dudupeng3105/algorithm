def quicksort(arr):
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

        return quicksort(smaller) + equal + quicksort(larger)


test_case = int(input())
for tc in range(1, test_case+1):
    n = int(input())
    unsorted_list = list(map(int, input().split()))
    print(quicksort(unsorted_list))
    print(f'#{tc} {quicksort(unsorted_list)[n//2]}')