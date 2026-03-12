with open('Message 4/message4.txt', 'r', encoding="utf-8") as file:
    message = file.read() # enregistre le contenu dans message


def decode(message, k, w):     #fonction qui va décoder le message
    l = []              #on commence par créer une liste vide
    for q in range(len(message)):   # boucle de la taille du message; on prends le numéro ord() (le numéro unicode), de chaque caractère,
        if q %2 == 0:

            a = ord(message[q])         # puis on ajoute dans la liste vide, un caractère ayant la valeur unicode du caractère précédent + la valeur
            l.append(chr(a+k))          # du décalage du chiffrement de césar
        if q%2 !=0:
            a = ord(message[q])         # puis on ajoute dans la liste vide, un caractère ayant la valeur unicode du caractère précédent + la valeur
            l.append(chr(a+w))
    return(l)

clé = -(124-111)        #Pour trouver les clés, je me suis basé sur le fait que la fin du message est fort probablement "Joël", ainsi, j'ai regardé
clé2 = -(125-74)  #la fin du message qui est "}|Ğy", j'ai compté le nombre de caractère total, de sorte à savoir si "}" et "|" sont sur des
                  # positions paires ou impaires. Finalement, j'ai regardé la valeur unicode de "}" et "|", et j'ai comparé avec celle de "J"
                  # et "o". On fait une soustraction pour calculer le décalage, et voilà. Magique!
décodé_impropre = decode(message, clé, clé2) #le message décodé impropre, plein de [] et ''
décodé_propre = []
for loop in range(len(décodé_impropre)):        # même principe que pour le message 1; on transforme la liste de caractère en une chaine propre
    décodé_propre.append("".join(décodé_impropre[loop]))
print(''.join(décodé_propre))
