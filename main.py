import random

route = 0
player_stats = {}
enemie = {}
enemie_type = ("goblin", "bandit", "orc")

def reset(player):
    print()
    print("Welcome to the Text RPG".center(40, "-"))
    name = input("\nEnter your name: ")

    player.clear()
    player.update({
        "name": name,
        "hp": 10,
        "hpmax": 10,
        "damage": 5,
        "lvl": 1,
        "xp": 0,
        "potions": 0
    })

def show_stats():
    print("\nSTATS" \
    f"\n Name: {player_stats["name"]}" \
    f"\n HP: {player_stats["hp"]}/{player_stats["hpmax"]}" \
    f"\n Damage: {player_stats["damage"]}" \
    f"\n LvL: {player_stats["lvl"]}" \
    f"\n XP: {player_stats["xp"]}")

def random_enemie():
    rng = random.choice(enemie_type)
    enemie.clear()
    enemie.update({"name": rng, "hp": 5*route, "damage": 2*route})
    print()
    print(f"ROUTE {route}".center(40, "-"))
    print(f'\nYou see a {rng} going towards you')

def xp_gain():
    xp = route * 5
    player_stats["xp"] += xp
    print(f"You gain {xp} XP")
    if player_stats["xp"] >= player_stats["lvl"] * 10:
        player_stats["xp"] = 0
        player_stats["lvl"] += 1
        player_stats["damage"] += 3
        player_stats["hpmax"] += 5
        player_stats["hp"] = player_stats["hpmax"]
        print("LEVEL UP!!!")
        print(f"Your level is now {player_stats["lvl"]}")

def enemie_attack():
    damage = route * 1
    player_stats["hp"] -= damage
    print(f"{enemie['name']} attacked you causing {damage} damage")

def attack_system():
    print(f"{enemie["name"]}: {enemie['hp']}HP")
    option = ''
    while enemie["hp"] > 0:
        print()
        print("".center(40, "-"))
        option = input("\n1- Attack" \
        "\n2- Stats" \
        "\n3- Use potion" \
        "\n4- Run" \
        "\nWhat do you do? ")
        if option in list("1234"):
            print()
            print("".center(40, "-"))
            if option == "1":
                enemie["hp"] -= player_stats["damage"]
                print(f"You attack the {enemie["name"]} causing {player_stats['damage']} damage.")
                if enemie["hp"] <= 0:
                    print(f"The {enemie["name"]} are dead.")
                    xp_gain()
                    if route %3 == 0:
                        print("You gain 2 potion!")
                        player_stats["potions"] += 2
                else:
                    enemie_attack()
                    if player_stats['hp'] <= 0:
                        break
                    print(f"{player_stats["name"]}: {player_stats['hp']}HP")
                    print(f"{enemie["name"]}: {enemie['hp']}HP")
            elif option == "2":
                show_stats()
            elif option == "3":
                if player_stats["potions"] > 0:
                    print("You used the potion and restored your HP to maximum.")
                    player_stats["hp"] = player_stats["hpmax"]
                    player_stats["potions"] -= 1
                else:
                    print("You dont have potions to use :( ")
                print("Potions: ",player_stats["potions"])
            elif option == "4":
                print("You run away from the fight.")
                break
        else:
            print("     Invalid option.")

def play():
    random_enemie()
    attack_system()

running = False
while True:
    if not running:
        reset(player_stats)
        running = True
        route = 1
    play()
    route += 1
    if player_stats["hp"] <= 0:
        running = False
        print("\nYOU ARE DEAD")
        play_again = input("Do you wanna play again? ").lower()
        if play_again in ["n", "no", ""]:
            break