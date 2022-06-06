test_case = int(input())

for tc in range(1, test_case + 1):
    n = int(input())
    boxes_list = list(map(int, input().split()))

    result = 0
    for i in range(n):
        max_height = n - 1 - i
        for j in range(i+1, n, 1):
            if boxes_list[i] <= boxes_list[j]:
                max_height -= 1

        if result < max_height:
            result = max_height

    print(result)
