with open('Message 6/message6.txt', 'r', encoding="utf-8") as file:
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
 

def decryptage_avec_cle(message, cle):
    a= max_régulier(message, cle)
    decryption_espace= []
    message_clair =[]
    m=0
    for i in range(len(a)):
        decryption_espace.append(decrypt_into_blank(a[i]))
    for c in range(len(m)):
        message_clair.append(decode_simple(m[c],decryption_espace[c%5]))
    return(message_clair)


def trouverlavraiecle(message, chiffregrand):
    Liste_diff=[]
    for i in range(chiffregrand):
        y=0
        L= []
        
        for k in range(len(max_régulier(message,i))):
            for j in range(len(max_régulier(message,i))-k):
                if max_régulier(message, i)[k] not in L:
                    y +=1
                    L.append(max_régulier(message, i)[k])
        print(max_régulier(message,i), i)
        print("nb caractères différents:", y)
        Liste_diff.append(y)
    print(max(Liste_diff)+1, max_régulier(message,max(Liste_diff)+1))
    return(max_régulier(message,max(Liste_diff)+1))

def decryptage(m, liste_max):
    liste_ord=[]
    message = []
    for i in range(len(liste_max)):
        liste_ord.append(decrypt_into_blank(liste_max[i]))
    for l in range(len(m)//len(liste_ord)):
        for w in range(len(liste_max)):
            message.append(decode_simple(m[l*len(liste_ord)+w], liste_ord[w]))
    return(message)


m= splitting(message)
#m1= trouverlavraiecle(m,14)
print(nettoyage(decryptage(m, ['\x1f', '"', '(', '#', '!', '#', '&', ')', '%', '$', '+', "'", '*'])))








