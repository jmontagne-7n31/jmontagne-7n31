with open('Message 2/message2.txt', 'r', encoding="utf-8") as file:
    message = file.read() # enregistre le contenu dans message


def decode(message, k):     #fonction qui va décoder le message
    l = []              #on commence par créer une liste vide
    for q in range(len(message)):   # boucle de la taille du message; on prends le numéro ord() (le numéro unicode), de chaque caractère,
        a = ord(message[q])         # puis on ajoute dans la liste vide, un caractère ayant la valeur unicode du caractère précédent + la valeur
        l.append(chr(a+k))          # du décalage du chiffrement de césar
    return(l)

clé = -38           # Ż = 379; A = 65; z =122 >>>>>>>>>> 314 -> 257



décodé_impropre = decode(message, clé) #le message décodé impropre, plein de [] et ''
décodé_propre = []
for loop in range(len(décodé_impropre)):        # même principe que pour le message 1; on transforme la liste de caractère en une chaine propre
    décodé_propre.append("".join(décodé_impropre[loop]))
print(''.join(décodé_propre))
