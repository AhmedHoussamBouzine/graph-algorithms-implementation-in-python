

def dfs(G, x0):
    # initialiSation
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
    
    while OUVERT:
        source = OUVERT.pop() 
        for x in G[source]:   
            if couleur[x] == 'blanc':
                couleur[x] = 'gris'
                OUVERT.add(x)
                parent[x] = source
                t += 1
                d[x] = t
            else: 
                couleur[source] = 'noir'
                t += 1
                f[source] = t
    
    return parent, f, d


def topological_sort(graph):
    topological_order = set()
    dfs = dfs(graph)
    topological_order.add(dfs['f'])
    return topological_order


