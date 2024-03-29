def Dijkstra(G, x0):
    #initialisation
    S, A, C = G
    Q = S.copy()
    visited = set()
    d = {node: float('inf') for node in S}
    parent = {node: None for node in S}
    d[x0] = 0
    # boucle principale 
    while Q:
        U = min(Q, key=d.get)
        visited.add(U)
        Q.remove(U)

        for y in A[U]:
            if y in Q:
                if d[y] > d[U] + C[(U, y)]:
                    d[y] = d[U] + C[(U, y)]
                    parent[y] = U

    return parent, d



# declarations
S = set(['1', '2', '3', '4', '5'])
A = {
    '1': set(['2', '3']),
    '2': set(['1', '3', '4', '5']),
    '3': set(['1', '2', '4']),
    '4': set(['2', '3', '5']),
    '5': set(['2', '4'])
}
C = {
    ('1', '2'): 1,
    ('1', '3'): 4,
    ('2', '1'): 1,
    ('2', '3'): 3,
    ('2', '4'): 2,
    ('2', '5'): 3,
    ('3', '1'): 4,
    ('3', '2'): 3,
    ('3', '4'): 2,
    ('4', '2'): 2,
    ('4', '3'): 2,
    ('4', '5'): 1,
    ('5', '2'): 3,
    ('5', '4'): 1
}

# appel a la fonction prim
parent, key = Dijkstra((S, A, C), '1')

# affichage des resultats
print("parent =", parent)
print("key =", key)