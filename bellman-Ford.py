def belman_ford(G, x0):
    S, A, coux = G
    # Initialisation
    d = {node: float('inf') for node in S}
    parent = {node: None for node in S}
    d[x0] = 0

    # boucle principale
    for _ in range(len(A) - 1):
        for (x, y) in A:
            if d[y] > d[x] + coux[(x, y)]:
                d[y] = d[x] + coux[(x, y)]
                parent[y] = x
    
    # detection d'un circuit absorbant
    for (x, y) in A:
        if d[y] > d[x] + coux[(x, y)]:
            return False, None, None
    
    return True, d, parent


# test 

S = set([1, 2, 3, 4])
A = [(1, 2), (3, 2), (4, 3), (1, 4)]
coux = {(1, 2): 4, (3, 2): -10, (4, 3): 3, (1, 4): 5}
G = (S, A, coux)


result, d, parent = belman_ford(G, 1)

if not result:
    print("un circuit absorbant a ete detecte")


print("d:", d)
print("Parent:", parent)

