def dfs(elements):
    if len(prev_element) == N:
        print(' '.join(map(str, prev_element)))

    
    for e in elements:
        next_elements = elements[:]
        next_elements.remove(e)
        prev_element.append(e)

        dfs(next_elements)
        prev_element.pop()   




N = int(input())
prev_element = []
num_list = [x for x in range(1, N + 1)]
dfs(num_list)











