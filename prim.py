def prim(G, x0):
    # Initialisation
    S, A, W = G
    Q = S.copy()
    visited = set()
    key = {node: float('inf') for node in S}
    parent = {node: None for node in S}

    # boucle principale
    while Q:
        U = min(Q, key=key.get)
        Q.remove(U)

        visited.add(U)

        for X in A[U]:
            if X in Q and key[X] > W[(U, X)]:
                key[X] = W[(U, X)]
                parent[X] = U

    return parent, key


# declarations
S = set(['1', '2', '3', '4', '5'])
A = {
    '1': set(['2', '3']),
    '2': set(['1', '3', '4', '5']),
    '3': set(['1', '2', '4']),
    '4': set(['2', '3', '5']),
    '5': set(['2', '4'])
}
W = {
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
parent, key = prim((S, A, W), '1')

# affichage des resultats
print("parent =", parent)
print("key =", key)


