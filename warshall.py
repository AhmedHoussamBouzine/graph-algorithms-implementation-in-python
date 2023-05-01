def warshall(G):
    n = len(G)
    
    for i in range(n):
        for j in range(n):
            if G[i][j] == 1:
                for k in range(n):
                    if G[j][k] == 1:
                        G[i][k] = 1
    return G

    
    
# declaration d'une matrice  
G = [[1, 1, 0, 1],[1, 1, 0, 0],[0, 0, 1, 0],[1, 0, 1, 1]]
# appel a la fonction warshall
warshall(G)
# affichage du resultat final
print(G)


