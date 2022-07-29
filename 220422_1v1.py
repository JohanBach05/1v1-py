import random

RULES = """Voici les regles:
- Vous et votre ennemi avez 50PV.
- A chaque tour vous pouvez attaquer votre ennemi en lui infligeant entre 5 et 10 points de degats.
- Vous pouvez egalement vous soigner 15 a 50 PV en utilisant une potion, mais attention vous n'avez que 3 potions et si vous en utilisez une, vous passerez le tour suivant.
- Votre ennemi n'a pas de potion.
- Votre ennemi inflige entre 5 et 15 points de degats
- Bonne chance !"""

print(RULES)

PLAYER_HEALTH = 50
ENEMY_HEALTH = 50
NUMBER_OF_POTIONS = 3
SKIP_TURN = False

while True:

    # Jeu du joueur
    if SKIP_TURN:
        print("Vous passez votre tour...")
        SKIP_TURN = False
    else:
        user_choice = ""
        while user_choice not in ["1", "2"]:
            user_choice = input("Souhaitez-vous attaquer (1) ou utiliser une potion (2) ? ")
        if user_choice == '1': # Attaque
            dodge = random.randint(1, 12)
            if dodge == 1:
                print("L'ennemi a esquive votre attaque")
            else:
                your_attack = random.randint(5, 10)
                ENEMY_HEALTH -= your_attack
                print("Vous avez inflige " + str(your_attack) + " points de degats.")
        elif user_choice == '2': # Heal
            if NUMBER_OF_POTIONS > 0:
                heal = random.randint(15, 50)
                PLAYER_HEALTH += heal
                NUMBER_OF_POTIONS -= 1
                SKIP_TURN = True
                print("Vous vous etes soigne de " + str(heal) + " PV. ")
            else:
                print("Vous n'avez plus de potion...")
                continue

    if ENEMY_HEALTH <= 0:
        print("Vous avez gagne !")
        break

    # Attaque de l'ennemi
    enemy_dodge = random.randint(1, 7)
    if enemy_dodge == 1:
        print("Vous avez esquive l'attaque ennemie")
    else:
        enemy_attack = random.randint(5, 15)
        PLAYER_HEALTH -= enemy_attack
        print("L'ennemi vous a inflige " + str(enemy_attack) + " points de degats. ")

    if PLAYER_HEALTH <= 0:
        print("Vous avez perdu ;-;")
        break

    # Stats
    print("Il vous reste " + str(PLAYER_HEALTH) + " PV. ")
    print("Il reste " + str(ENEMY_HEALTH) + " PV a l'ennemi. ")
    print("-" * 50)

print("Fin du jeu.")
