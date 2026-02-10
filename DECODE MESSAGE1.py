with open('message1.txt', 'r', encoding="utf-8") as file:
    message = file.read() # enregistre le contenu dans message

from math import ceil #importe l'outil ceil pour arrondir au supérieur

N = len(message)    # définit N comme la longueur du message
numcol = 57         # nombre de colonnes utilisées pour l'encryption, déterminé à la main en faisant +1 jusqu'à trouver le bon
numline = ceil(N/numcol)    # Nombre de ligne, taille du message divisée par le nombre de colonnes
numtrous = numcol * numline - N # on trouve le nombre de trou mathématiquement en calculant le nombre de "cases" dans un carré de numcol*numline - la taille du message. les trous sont dus au fait que l'on fait un arrondi, car parfois les messages ne sont pas de taille numcol*numline

def découpage(m):   #je réintroduis ma fonction découpage car je l'aime bien :)
    vide = []
    for kq in range(len(m)):
        vide.append(m[kq])
    return(vide)
c = découpage(message) #essentiellement, elle transforme le message en une suite de charactère unique exemple: fromage >'f' 'r' 'o' 'm' 'a' 'g' 'e'
print(c)

t = [[] for line in range(numline)] #on créé une liste vide
compteur = 0                        # compteur de décalage
for col in range(numcol):       # boucle qui parcourt les colonnes, c'est à partir d'ici que l'on commence à inverser le message enchiffré pour le déchiffrer
    for line in range(numline): 
        if line+1 < numline or col + numtrous < numcol: # condition pour éviter les débordements, on vérifie si on est à la dernière ligne ou pas
           t[line].append(c[compteur])  # si l'une des deux condition est validée, on ajoute à t, à l'emplacement line, le charactère à l'empalcement compteur de la liste c
           compteur += 1 #incrémentation

m =[] #on va créer un affichage propre
for loop in range(len(t)): #boucle qui ajoute chaque charactère à la liste vide m. On évite ainsi que le résultat soit un gros paté moche tel que ['b'], ['o'], ['n'], ['j']...
    m.append("".join(t[loop]))
print(''.join(m))
# On print le résultat

#En conclusion, j'ai passé beaucoup de temps sur ce message (qui n'est que le premier ahah), le code ici présent est celui que vous m'avez aidé à réécrire en 
# se basant sur le code que j'avais déjà fait, je l'ai par la suite un peu modifié, et pour la partie qui fait l'affichage propre, Aurélie ma conseillé la structure "".join(t[loop]))