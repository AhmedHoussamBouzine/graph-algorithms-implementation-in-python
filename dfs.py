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

#declaration d'un graphe sous forme d'une liste
G = {
    'S':['D', 'G','A','C'],
    'A': ['G', 'B','F','H'],
    'B': ['H', 'E','F'],
    'C': ['F', 'E'],
    'D': ['H'],
    'E': ['H','I'],
    'F': ['I'],
    'G': ['H'],
    'H': ['I'],
    'I':[]
}
#appel a la fonction dfs 
dfs = dfs(G,'S')

# affichage du resultat
print(dfs)

