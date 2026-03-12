# ouvrir un fichier
with open('Message 3/message3.txt', 'r', encoding="utf-8") as file:
    message = file.read() # enregistre le contenu dans message
# ici, on ouvre le fichier sous le nom messsage

def splitting(msg):
    splitted = []
    for q in range(len(msg)):
        splitted.append(msg[q])
    return(splitted)

"""
Cette première fonction split le message crypté en une liste de charactère pour avoir une
manipulation plus simple
"""


def max(m):
    tableau ={}
    for i in range(len(m)):
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

"""
Cette fonction max, créé un tableau des fréquences des charactères du message crypté
On suppose (à raison), que le charactère le plus commun est un espace crypté. Vraissemblablement,
sur un message long, chaque mot possède au moins un espace or un mot ne possède pas nécessairement un "e" ou un "a".
Ensuite on parcours le tableau pour trouver quel est le charactère le plus fréquent, ici c'est h-barre, comme en physique quantique.
"""

def decrypt_into_blank(lettre):
    aim = 32
    jump = ord(lettre)-32
    return(jump)
"""

"""

def decode(msg, k):     #fonction qui va décoder le message
    l = []              #on commence par créer une liste vide
    for q in range(len(msg)):   # boucle de la taille du message; on prends le numéro ord() (le numéro unicode), de chaque caractère,
        a = ord(msg[q])         # puis on ajoute dans la liste vide, un caractère ayant la valeur unicode du caractère précédent + la valeur
        l.append(chr(a-k))          # du décalage du chiffrement de césar
    return(l)

def nettoyage(msg):
    message_propre =[]
    for i in range(len(msg)):        # même principe que pour le message 1; on transforme la liste de caractère en une chaine propre
        message_propre.append("".join(msg[i]))
    return(''.join(message_propre))

    
m = splitting(message)
m2 = max(m)
m3= decrypt_into_blank(m2)
m4 = decode(message, m3)
m5 = nettoyage(m4)
print(m5)












#décodé_impropre = decode(message, clé) #le message décodé impropre, plein de [] et ''
#décodé_propre = []
#for loop in range(len(décodé_impropre)):        # même principe que pour le message 1; on transforme la liste de caractère en une chaine propre
#    décodé_propre.append("".join(décodé_impropre[loop]))


#print(''.join(décodé_propre))


