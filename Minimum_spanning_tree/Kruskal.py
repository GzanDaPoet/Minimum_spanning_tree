# add edge to graph
def add_edge(g, u, v, w):
    g.append([u, v, w])
# Search function


def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])


def apply_union(parent, rank, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)
    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    else:
        parent[yroot] = xroot
        rank[xroot] += 1

#  Applying Kruskal algorithm


def kruskal_algo(v, t):
#     G = """0, 2, 0, 0, 5, 6, 0, 0, 0, 0
# 2, 0, 2, 3, 0, 0, 0, 0, 0, 0
# 0, 2, 0, 6, 0, 0, 0, 8, 0, 0
# 5, 3, 6, 0, 3, 0, 3, 12, 0, 0
# 6, 0, 0, 3, 0, 5, 0, 0, 0, 0
# 0, 0, 0, 0, 5, 0, 5, 0, 2, 3
# 0, 0, 0, 3, 0, 5, 0, 2, 7, 0
# 0, 0, 8, 12, 0, 0, 2, 0, 5, 0
# 0, 0, 0, 0, 0, 2, 7, 5, 0, 1
# 0, 0, 0, 0, 0, 3, 0, 0, 1, 0"""
    rs = ""
    a = list(t.split('\n'))
    lst = []
    g = []
    for x in a:
        test = x.split(", ")
        tmp = [int(b) for b in test]
        lst.append(tmp)
    no_edge = 0
    for i in range(v):
        for j in range(v):
            if lst[i][j] != 0:
                add_edge(g, i, j, lst[i][j])
    result = []
    i, e = 0, 0
    g = sorted(g, key=lambda item: item[2])
    parent = []
    rank = []
    for node in range(v):
        parent.append(node)
        rank.append(0)
    while e < v - 1:
        u, ver, w = g[i]
        i = i + 1
        x = find(parent, u)
        y = find(parent, ver)
        if x != y:
            e = e + 1
            result.append([u, ver, w])
            apply_union(parent, rank, x, y)
    for u, ver, weight in result:
        # print("%d - %d: %d" % (u, ver, weight))
        rs = rs + ("%d - %d : %d \n" % (u, ver, weight))
    return rs

