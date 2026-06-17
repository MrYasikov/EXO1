import random
num = random.randint(1, 100)
print("Bienvenu dans le jeu de devinettes!")#affiche un message de bienvenue pour le jeu de devinetttes 
turn = 3 
while True:
    try:
        guess = int(input("Entrez votre nombre deviné (entre 1 et 100): "))
    except ValueError:
        print("Veuillez entrer un nombre valide.")#affiche un message pour indiquer que l'entrée n'est pas un nombre valide
        continue
    if guess < 1 or guess > 100:
        print("Veuillez entrer un nombre entre 1 et 100.")#affiche un message pour indiquer que le nombre deviné n'est pas dans la plage valide
        continue
    if guess == num:
        print("Très bien! Vous avez deviné le nombre {num} en {turn} coups!")#affiche un message pour indiquer que le joueur a deviné le nombre
        break
    elif guess < num:
        print("Too low! Try again.")#affiche un message pour indiquer que le nombre deviné est trop bas
    else:
        print("Too high! Try again.")#affiche un message pour indiquer que le nombre deviné est trop haut
    turn -= 1
    if turn == 0:
        print(f"Game over! The number was {num}.")#affiche un message de fin de jeu si le joueur n'a plus de coups restants et révèle le nombre à deviner 
        break
