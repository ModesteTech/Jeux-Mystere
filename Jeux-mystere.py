
from random import randint
print("\n","Bienvenue au JEUX MYSTERE".center(50, "-"),"\n")
print("Dans ce jeux la confirmation c'est 'y' et autre chose pour la non confirmation\nCommencons\n")

response='y'
while response=='y':
    nbr_mystere = randint(0, 21)
    result = 0
    tentatives = 1
    print("Vous devez deviner le nombre que j'ai choisi de maniere aleatoire")
    print("Ce nombre est compris entre 0 et 20")
    while tentatives<6:
        nbr=int(input("Entrez un nombre: "))
        if nbr_mystere==nbr :
            print("Brovo!!! Vous avez devinez le nombre mystere, vous remportez cette partie\n")
            result=1
            break
        elif nbr<nbr_mystere:
            print("C'est plus")
            print("Il vous reste {} tentatives".format(5-tentatives))
        elif nbr>nbr_mystere:
            print("C'est moins")
            print("Il vous reste {} tentatives".format(5 - tentatives))
        tentatives+=1
    if result == 0:
        print("Vous avez epuise touts vos 5 tentatives, vous perdez donc cette partie\n")
    response=input("Voulez vous rejouer ? ")
    response=response.lower()

Q=input("Avez vous des suggestions a faire ?\n")
Q=Q.lower()
if Q=='y':
    Commentaire=input("Entrez votre commentaire: ")
    print("Votre commentaire a bien ete pris en compte, Merci.\n")

print("Merci d'avoir participe a ce jeux, n'hesitez pas a revenir si necessaire. PARTIE TERMINE\n\n")

input("Appuyer sur Entre pour fermer le programme")