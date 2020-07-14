# import characters

# from characters import Wizard, Creature, SmallCreature, Dragon
# import random
# import time
#
#
# def main():
#     print_header()
#     game_loop()
#
#
# def print_header():
#     print('-----------------------------')
#     print('        Battle Wizard App    ')
#     print('-----------------------------')
#
#
# def game_loop():  # getting input from user until game ends
#     # list of creature objects
#     # creatures = [  # the parameters from the Creatures class
#     #     Creature('Toad', 1),  # instances of the Creature class, (obj of creature class)
#     #     Creature('Tiger', 12),
#     #     Creature('Bat', 3),
#     #     Creature('Dragon', 50),
#     #     Creature('Evil Wizard', 100)
#     # ]
#
#     creatures = [  # the parameters from the Creatures class
#         # creatures modeled the same but not behaving the same because of different attributes associated with that obj
#         SmallCreature('Toad', 1),  # behaves as a creature but now weaker because of its different method
#         Creature('Tiger', 12),
#         SmallCreature('Bat', 3), # behaves as a creature but now weaker because of its different method
#         Dragon('Dragon', 90, 75, True), # True - breaths fire
#         Wizard('Evil Wizard', 100,)
#     ]
#
#     # print(creatures)
#     hero = Wizard('Harriet', 80)
#
#     while True:
#
#         active_creature = random.choice(creatures) # coming from the list
#         print('A {} of level {} has appeared from a dark and foggy forest...'.format(
#             active_creature.name, active_creature.level))
#
#         cmd = input('Do you want to [a]ttack, [r]unaway, or [l]ook around? ')
#         if cmd == 'a':
#             #hero.attack(active_creature) # hero attacks random creature
#             # consequences of losing a battle
#             if hero.attack(active_creature): # creature is being randomly selected
#                 creatures.remove(active_creature) # removes a creature
#             else:
#                 print("The wizard runs and hides taking time to recover")
#                 time.sleep(5) # pauses game for 5 seconds
#                 print("The wizard returns refreshed")
#         elif cmd == 'r':
#             print('The wizard has become unsure of his power and flees')
#         elif cmd == 'l':
#             print('The wizard {} takes in the surroundings and looks and sees: '.format(hero.name))
#             for c in creatures: # iterating over creatures
#                 print('* A {} of level {}'.format(c.name, c.level))
#         else:
#             print("Exiting game")
#             break  # ends game
#
#         if not creatures:
#             print("You've defeated all of the creatures!")
#             break
#
#         print()
#
#
# if __name__ == '__main__':
#     main()









import characters
from characters import Wizard, Creature, CutePet, KingOfTheJungle
import random
import time

def main():
    print_header()
    game_loop()  # getting input from the user


def print_header():
    print('-------------------------------')
    print('     Wizard Battle Game        ')
    print('-------------------------------')


def game_loop():
    creatures = [  # blueprints of the Creature class
        CutePet('Rabbit', 10),
        Wizard('Snake', 25),
        CutePet('Mouse', 5),
        Creature('Deer', 50),
        KingOfTheJungle('Lion', 100, 80, True)
    ]

    #print(creature)

    hero_of_the_game = Wizard('Frederick', 85)

    while True:
        new_creature = random.choice(creatures)
        print("{} of level {} just arrived in this dark and foggy forest ".format
              (new_creature.name, new_creature.level))
        cmd = input('Do you [a]ttack, [r]unaway, or [l]ook around? ')

        if cmd == 'a':
            #hero_of_the_game.wizard_behavior(new_creature)
            # a return statement was needed by the if statement of wb in order for this bit of code to run
            if hero_of_the_game.wizard_behavior(new_creature):
                creatures.remove(new_creature) # removing from list

            else:
                print("Wizard has been defeated and now needs to rest")
                time.sleep(3)
                print("The Wizard returns refreshed")

        elif cmd == 'r':
            print('The Wizard runs away like a punk')
        elif cmd == 'l':
            print('The wizard looks around and sees: ')
            for n in creatures: # iterating over the list of creatures
                print("* A {} of level {}".format(n.name, n.level))
        else:
            print('Bye bye')
            break


if __name__ == '__main__':
    main()
