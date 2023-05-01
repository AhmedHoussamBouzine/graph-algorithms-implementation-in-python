def dfs(G, x0):
    # initialization
    OUVERT = set()  
    couleur = {node: 'blanc' for node in G}
    parent = {node: None for node in G}
    d = {}          
    f = {}        
    t = 0        
    couleur[x0] = 'gris'
    OUVERT.add(x0)
    t += 1
    d[x0] = t
    
    # main loop
    while OUVERT:
        source = OUVERT.pop()  # take the last element of the set
        for x in G[source]:   # for each neighbor x of the source node
            if couleur[x] == 'blanc':
                couleur[x] = 'gris'
                OUVERT.add(x)
                parent[x] = source
                t += 1
                d[x] = t
        couleur[source] = 'noir'
        t += 1
        f[source] = t
    
    return parent, f, d