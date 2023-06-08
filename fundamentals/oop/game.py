from classes.ninja import Ninja
from classes.pirate import Pirate

michelangelo = Ninja("Michelangelo")

jack_sparrow = Pirate("Jack Sparrow")

# michelangelo.attack(jack_sparrow)
# jack_sparrow.show_stats()

while michelangelo.health >= 0 and jack_sparrow.health >= 0:
    player_input = ""
    choice_input = ""
    while not choice_input == "Pirate" and not choice_input == "Ninja":
        choice_input = input("\nChoose a character class:\nPirate\nNinja\n")
        if choice_input == "Ninja":
            print("\nYou picked Michelangelo!\n")
            while not player_input == "1" and not player_input == "2":
                player_input = input("Choose an action:\n1) Attack\n2) Shuriken Attack\n")
                if player_input == "1":
                    michelangelo.attack(jack_sparrow)
                    jack_sparrow.attack(michelangelo)
                    michelangelo.show_stats()
                    jack_sparrow.show_stats()
                    player_input = ""
                elif player_input == "2":
                    michelangelo.shuriken(jack_sparrow)
                    if jack_sparrow.bullets > 0:
                        jack_sparrow.pistol(michelangelo)
                    else:
                        jack_sparrow.attack(michelangelo)
                    michelangelo.show_stats()
                    jack_sparrow.show_stats()
                    player_input = ""
                else:
                    print("\nChoose a valid action\n")
                if michelangelo.health <= 0:
                    print(f"{jack_sparrow.name} has defeated {michelangelo.name}! Game Over!")
                    break
                elif jack_sparrow.health <= 0:
                    print(f"{michelangelo.name} has defeated {jack_sparrow.name}! Game Over!")
                    break
                
        elif choice_input == "Pirate":
            print("\nYou picked Jack Sparrow!\n")
            while not player_input == "1" and not player_input == "2" and not player_input == "3":
                player_input = input("Choose an action:\n1) Attack\n2) Pistol Shot\n3) Rum\n")
                if player_input == "1":
                    jack_sparrow.attack(michelangelo)
                    michelangelo.attack(jack_sparrow)
                    jack_sparrow.show_stats()
                    michelangelo.show_stats()
                    player_input = ""
                elif player_input == "2":
                    jack_sparrow.pistol(michelangelo)
                    if michelangelo.shurikens > 0:
                        michelangelo.shuriken(jack_sparrow)
                    else:
                        michelangelo.attack(jack_sparrow)
                    jack_sparrow.show_stats()
                    michelangelo.show_stats()
                    player_input = ""
                elif player_input =="3":
                    jack_sparrow.rum()
                    michelangelo.attack(jack_sparrow)
                    jack_sparrow.show_stats()
                    michelangelo.show_stats()
                    player_input = ""
                else:
                    print("\nChoose a valid action\n")
                if michelangelo.health <= 0:
                    print(f"{jack_sparrow.name} has defeated {michelangelo.name}! Game Over!")
                    break
                elif jack_sparrow.health <= 0:
                    print(f"{michelangelo.name} has defeated {jack_sparrow.name}! Game Over!")
                    break
        else:
            print("\nChoose a valid character class!\n")
        # while not player_input == "1" and not player_input == "2":
        #     player_input = input("Choose an action:\n1) Attack\n2) Shuriken Attack\n")
        #     if player_input == "1":
        #         michelangelo.attack(jack_sparrow)
        #     elif player_input == "2":
        #         michelangelo.shuriken(jack_sparrow)
        #     else:
        #         print("\nChoose a valid action\n")
