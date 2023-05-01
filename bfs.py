from queue import Queue
def bfs(G, x0):
    # initialisation
    ouvert = Queue()
    couleur = {node: 'blanc' for node in G}
    parents = {node: None for node in G}
    couleur[x0] = 'gris'
    ouvert.put(x0)
    # boucle principale
    while not ouvert.empty():
        source = ouvert.get()
        couleur[source] = 'noir'
        for adj in G[source]:
            if couleur[adj] == 'blanc':
                couleur[adj] = 'gris'
                ouvert.put(adj)
                parents[adj] = source
    return parents

# declaration d'un graphe sous forme d'une liste
G = {
    'A': ['B', 'C', 'D'],
    'B': ['D', 'E'],
    'C': ['E'],
    'D': ['A','D'],
    'E': ['F','C'],
    'F': []
}
# appel a l'algorithme
parents = bfs(G, 'A')
# affichage du resulta final
for node in G:
    print(f"Le parent de  {node} est: {parents[node]}")



    


