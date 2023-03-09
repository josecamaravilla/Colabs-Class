
print("Welcome to your first Pokemon Battle\n")
## Variables
pokemon = None
npc = None
player = None

hp_initial_pikachu = 100
hp_initial_charizard = 140

hp_pikachu = hp_initial_pikachu
hp_charizard= hp_initial_charizard


#### Library
import random
###



while pokemon != "a" and pokemon != "A" and pokemon != "b" and pokemon != "B":
    pokemon = input("Choose your Pokemon:\n"
                    "a) Pikachu\n"
                    "b) Charizard\n")
if pokemon == "a" or pokemon == "A":
    npc = "CHARIZARD"
    player = "PIKACHU"
    print("You choose: PIKACHU")
else:
    npc = "PIKACHU"
    player = "CHARIZARD"
    print("You choose: CHARIZARD")

while hp_charizard > 0 and hp_pikachu > 0:
    ## NPC Turn
    print(npc + " Turn")
    npc_attack = random.randint(1,3)
    if npc == "CHARIZARD" :
        if npc_attack == 1:
            print(npc + " use Dragon Breath")
            hp_pikachu -= 30
        elif npc_attack == 2:
            print(npc + " use Flamethrower")
            hp_pikachu -= 20
        else:
            print( npc + " use Iron tail")
            hp_pikachu -= 10
    else:
        if npc_attack == 1:
            print(npc + " use Thunder")
            hp_charizard -= 25
        elif npc_attack == 2:
            print(npc + " use Electro Ball")
            hp_charizard -= 15
        else:
            print( npc + " use Iron tail")
            hp_charizard -= 45
    hp_bar_pikachu = int((hp_pikachu/hp_initial_pikachu)*20)
    hp_bar_charizard = int((hp_charizard / hp_initial_charizard) * 20)
    print("HP PIKACHU:      [{}{}] ({}/{})\n".format("*"*hp_bar_pikachu," " * (20-hp_bar_pikachu),hp_pikachu,
                                                     hp_initial_pikachu))
    print("HP CHARIZARD:    [{}{}] ({}/{})\n".format("*" * hp_bar_charizard, " " * (20 - hp_bar_charizard),hp_charizard,
                                                     hp_initial_charizard))
    input("Enter to continue.... \n\n")
    if hp_pikachu<0 or hp_charizard <0:
        break

    ## Player Turn
    print(player + " Turn")
    player_attack = None
    if player == "CHARIZARD":
        while player_attack != "1" and player_attack != "2" and player_attack != "3" :
            player_attack = input("Choose your attack: \n"
                              "1) Dragon Breath\n"
                              "2) FlameThrower\n"
                              "3) Iron Tail\n")

        player_attack = int(player_attack)
        if player_attack == 1:
            print(player + " use Dragon Breath")
            hp_pikachu -= 30
        elif player_attack == 2:
            print(player + " use Flamethrower")
            hp_pikachu -= 20
        else:
            print(player + " use Iron tail")
            hp_pikachu -= 10
    else:
        while player_attack != "1" and player_attack != "2" and player_attack != "3" :
            player_attack = input("Choose your attack: \n"
                              "1) Thunder\n"
                              "2) Electro Ball\n"
                              "3) Iron Tail\n")

        player_attack = int(player_attack)
        if player_attack == 1:
            print(player + " use Thunder")
            hp_charizard -= 25
        elif player_attack == 2:
            print(player + " use Electro Ball")
            hp_charizard -= 15
        else:
            print(player + " use Iron tail")
            hp_charizard -= 45
    hp_bar_pikachu = int((hp_pikachu/hp_initial_pikachu)*20)
    hp_bar_charizard = int((hp_charizard / hp_initial_charizard) * 20)
    print("HP PIKACHU:      [{}{}] ({}/{})\n".format("*"*hp_bar_pikachu," " * (20-hp_bar_pikachu),hp_pikachu,
                                                     hp_initial_pikachu))
    print("HP CHARIZARD:    [{}{}] ({}/{})\n".format("*" * hp_bar_charizard, " " * (20 - hp_bar_charizard),hp_charizard,
                                                     hp_initial_charizard))
    input("Enter to continue.... \n\n")

if player == "CHARIZARD" and hp_charizard > hp_pikachu:
    print("YOU WIN!!!!!")
else:
    print("GAME OVER: TRY HARDER NEXT TIME")
