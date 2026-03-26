with open('Message 5/message5.txt', 'r', encoding="utf-8") as file:
    message = file.read() # enregistre le contenu dans message
# ici, on ouvre le fichier sous le nom messsage


"""tableau = [0 for _ in range(max([ord(c) for c in message])+1)]
for i in range(0, len(message), 1):
    tableau[ord(message[i])] += 1

t = [k for k in tableau if k !=0]
t.sort()


def delta(l):
    return [int(10*(l[i+1]-l[i])/l[i]) for i in range(len(l)-1)]

#print(delta(t))"""

""""A l'aide des fonctions précédentes, on peut supposer que la clé du message est comprise 
entre 3 et 6, alors, on va écrire un code qui teste ceci."""



def splitting(msg):
    splitted = []
    for q in range(len(msg)):
        splitted.append(msg[q])
    return(splitted)

def max_régulier(m, taille_cle):
    L = []
    for q in range(taille_cle):
        tableau ={}
        for i in range(0+q, len(m), taille_cle):
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
        #print("charactère le plus fréquent:", lettre, "en position:", q)
        L.append(lettre)
    return L
       



""""
Comme le message précédent, on applique la même méthode du tableau de fréquences, mais cette fois on sépare les cas
en fonction de la taille de la clé
"""

def decrypt_into_blank(lettre):
    aim = 32
    jump = ord(lettre)-32
    return(jump)

def decode_simple(car, k):    
    a = ord(car)       
    b= chr(a-k)      
    return(b)

"""
Encore une fois, même méthode que précédemment, mais ici on rajoute une condition sur la parité de l'indice de passage de la boucle
pour que il applique un traitement différent
"""

def nettoyage(msg):
    message_propre =[]
    for i in range(len(msg)):        # même principe que pour le message 1; on transforme la liste de caractère en une chaine propre
        message_propre.append("".join(msg[i]))
    return(''.join(message_propre))

def trouverCle(m, b1, b2):
    #cle = b1
    x = 0
    for loop in range(b1, b2+1): # on parcourt les bornes, avec le +1 sur b2 car python va jusqu'à -1
        y = 0                       # on initialise y
        L = max_régulier(m,loop) # associe à L, la liste de taille loop des caractères les plus fréquents 
        for i in range (len(L)): # on parcourt la taille de la liste précédente
            for j in range (len(L)-i): # on parcourt jusqu'à Len -1 pour faire la comparaison avec les caractères devant 
                if L[i] != L[j+i]: # si le caractère i est différent de celui à j+i, j+i+1, j+i+2... alors:
                    y += 1          # 
        y = y/loop
        if y>x :
            x = y
            cle = loop
    #print(cle)
    return cle
        

def decryptage_avec_cle(message, cle):
    a= max_régulier(message, cle)
    decryption_espace= []
    message_clair =[]
    for i in range(len(a)):
        decryption_espace.append(decrypt_into_blank(a[i]))
    for c in range(len(m)):
        message_clair.append(decode_simple(m[c],decryption_espace[c%5]))
    return(message_clair)






m = splitting(message)
m2 = max_régulier(m, 5)
trouverCle(m,2,5)
m3= decryptage_avec_cle(m, 5)
print(nettoyage(m3))