def prim(v, g):
    rs = ""
    INF = 9999999
    a = list(g.split('\n'))
    lst = []
    for x in a:
        test = x.split(", ")
        tmp = [int(b) for b in test]
        lst.append(tmp)
    g=lst
    selected = []
    for i in range (v):
        selected.append(0)
    no_edge = 0
    selected[0] = True
    while (no_edge < v - 1):
        minimum = INF
        x = 0
        y = 0
        for i in range(v):
            if selected[i]:
                for j in range(v):
                    if ((not selected[j]) and g[i][j]):
                        if minimum > g[i][j]:
                            minimum = g[i][j]
                            x = i
                            y = j
        # print(str(x) + " - " + str(y) + " : " + str(g[x][y]))
        rs=rs+str(x) + " - " + str(y) + " : " + str(g[x][y])+"\n"
        selected[y] = True
        no_edge += 1
    return rs