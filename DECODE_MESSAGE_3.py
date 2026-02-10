# ouvrir un fichier
with open('message3.txt', 'r', encoding="utf-8") as file:
    message = file.read() # enregistre le contenu dans message
# ici, on ouvre le fichier sous le nom messsage

def decode(message, k):     #fonction qui va décoder le message
    l = []              #on commence par créer une liste vide
    for q in range(len(message)):   # boucle de la taille du message; on prends le numéro ord() (le numéro unicode), de chaque caractère,
        a = ord(message[q])         # puis on ajoute dans la liste vide, un caractère ayant la valeur unicode du caractère précédent + la valeur
        l.append(chr(a+k))          # du décalage du chiffrement de césar
    return(l)

#Pour déterminer la valeur du décallage, j'ai dédicé de regarder sur internet la valeur unicode de Ż présent dans le message crypté, soit 379
#Ensuite, j'ai décidé de regarder ou sont les premiers caractère latins que nous utilisons A -> Z et a -> z, allant de 65 à 122
#Ainsi pour trouver le décallage, j'ai fait 379 -65 = 314 et 379-122 = 257; car le Ż est très probablement parmis eux. 
#Ensuite, j'ai tester manuellement toutes les combinaisons une à une en partant de -257. Ici, on est dans les négatifs car Ż est plus loin dans
# la liste unicode (379>65)
clé = -263              # Ż = 379; A = 65; z =122 >>>>>>>>>> 314 -> 257



décodé_impropre = decode(message, clé) #le message décodé impropre, plein de [] et ''
décodé_propre = []
for loop in range(len(décodé_impropre)):        # même principe que pour le message 1; on transforme la liste de caractère en une chaine propre
    décodé_propre.append("".join(décodé_impropre[loop]))
print(''.join(décodé_propre))

