def pre_order(v):
    global last
    if v <= last:  # 마지막 정점번호 이내
        print(v)  # visit(v)
        pre_order(v*2)  # 왼쪽 자식정점 방문
        pre_order(v*2+1)  # 오른쪽 자식정점 방문