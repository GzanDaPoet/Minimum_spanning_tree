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


def kruskal_algo(v, t):
    a = list(t.split('\n'))
    lst = []
    g = []
    for x in a:
        test = x.split(", ")
        tmp = [int(b) for b in test]
        lst.append(tmp)
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
            result.append([u+1, ver+1, w])
            apply_union(parent, rank, x, y)
    return result
