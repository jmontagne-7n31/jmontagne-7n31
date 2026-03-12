# ouvrir un fichier
with open('Message 4/message4.txt', 'r', encoding="utf-8") as file:
    message = file.read() # enregistre le contenu dans message
# ici, on ouvre le fichier sous le nom messsage

def splitting(msg):
    splitted = []
    for q in range(len(msg)):
        splitted.append(msg[q])
    return(splitted)

def max_pair(m):
    tableau ={}
    for i in range(0, len(m), 2):
        if m[i] in tableau:
            tableau[m[i]] += 1
        if m[i] not in tableau:
            tableau[m[i]] = 1
    max = 0
    lettre = ""
    for l,v in tableau.items():
        if v > max:
            max = v
            lettre = l
    return(lettre)

def max_impair(m):
    tableau ={}
    for i in range(1, len(m), 2):
        if m[i] in tableau:
            tableau[m[i]] += 1
        if m[i] not in tableau:
            tableau[m[i]] = 1
    max = 0
    lettre = ""
    for l,v in tableau.items():
        if v > max:
            max = v
            lettre = l
    return(lettre)

""""
Comme le message précédent, on applique la même méthode du tableau de fréquences, mais cette fois on sépare les cas
caractère paire et caractère impaire, car c'est ainsi que le message a été crypté
"""

def decrypt_into_blank(lettre):
    aim = 32
    jump = ord(lettre)-32
    return(jump)

def decode(msg, k, kbis):     #fonction qui va décoder le message
    l = []              #on commence par créer une liste vide
    for q in range(len(msg)):   # boucle de la taille du message; on prends le numéro ord() (le numéro unicode), de chaque caractère,
        if q%2 == 0: 
            a = ord(msg[q])         # puis on ajoute dans la liste vide, un caractère ayant la valeur unicode du caractère précédent + la valeur
            l.append(chr(a-k))          # du décalage du chiffrement de césar
        if q%2 != 0:
            a = ord(msg[q])
            l.append(chr(a-kbis))
    return(l)

"""
Encore une fois, même méthode que précédemment, mais ici on rajoute une condition sur la parité de l'indice de passage de la boucle
pour que il applique un traitement différent aux caractères pairs/impairs
"""

def nettoyage(msg):
    message_propre =[]
    for i in range(len(msg)):        # même principe que pour le message 1; on transforme la liste de caractère en une chaine propre
        message_propre.append("".join(msg[i]))
    return(''.join(message_propre))

m = splitting(message)
m2 = max_pair(m)
m2bis= max_impair(m)
m3= decrypt_into_blank(m2)
m3bis= decrypt_into_blank(m2bis)
m4 = decode(message, m3, m3bis)
m5 = nettoyage(m4)
print(m5)
