# OOP
import random


# class Wizard: # blueprint
#     def __init__(self, name, level):
#         self.name = name
#         self.level = level
#
#     def attack(self, creature): # instance method
#         print('The wizard {} attacks {}!'.format(
#             self.name, creature.name
#         ))
#         # algorithm for deciding who wins a roll/round
#         my_roll = random.randint(1, 12) * self.level # self is the hero
#         #creature_roll = random.randint(1, 12) * creature.level
#         creature_roll = creature.get_defensive_roll() # up to the creature to take all of its attributes into account
#
#         print("You roll {} ...".format(my_roll))
#         print("{} rolls {}".format(creature.name, creature_roll))
#
#         if my_roll >= creature_roll:
#             print("The wizard has handily defeated {}".format(creature.name))
#             return True
#         else:
#             print("The wizard has been defeated")
#             return False


# class Creature: # blueprint
#     def __init__(self, name, the_level): # magic method
#         self.name = name
#         self.level = the_level
#
#     def __repr__(self): # magic method
#         return "Creature {} of level {}".format(
#             self.name, self.level
#         )
#
#     def get_defensive_roll(self):
#         return random.randint(1,12) * self.level
#
#
# class Wizard(Creature):
#     # init method isn't necessary because I'm just moving up the inheritance
#     # Creature attributes are given to Wizard
#     # Wizard can now be any player in the game, not just the hero. Is now a Creature
#     # def __init__(self, name, level):
#     #     self.name = name
#     #     self.level = level
#         # used if I was adding more behavior to Wizard
#         #super().__init__(name,level) # creature attributes will be used here. Direct access to Creature
#
#     def attack(self, creature): # instance method
#         print('The wizard {} attacks {}!'.format(
#             self.name, creature.name
#         ))
#         # algorithm for deciding who wins a roll/round
#         #my_roll = random.randint(1, 12) * self.level # self is the hero
#         #creature_roll = random.randint(1, 12) * creature.level
#
#         my_roll = self.get_defensive_roll() # Wizard is now a Creature as well
#         creature_roll = creature.get_defensive_roll() # up to the creature to take all of its attributes into account
#
#         print("You roll {} ...".format(my_roll))
#         print("{} rolls {}".format(creature.name, creature_roll))
#
#         if my_roll >= creature_roll:
#             print("The wizard has handily defeated {}".format(creature.name))
#             return True
#         else:
#             print("The wizard has been defeated")
#             return False
#
#
# class SmallCreature(Creature):
#     def get_defensive_roll(self):
#         base_roll = super().get_defensive_roll() # super comes from the Creature class
#         return base_roll / 2 # extra weak creature
#
#
# class Dragon(Creature):
#     def __init__(self, name, level, scaliness, breaths_fire):
#         super().__init__(name,level) # more behavior added so super is used
#         self.breaths_fire = breaths_fire
#         self.scaliness = scaliness
#
#     def get_defensive_roll(self):
#             base_roll = super().get_defensive_roll()  # super comes from the Creature class
#             # fire_modifier = None
#             # if self.breaths_fire:
#             #     fire_modifier = 5
#             # else:
#             #     fire_modifier = 1
#
#             # Condensed version = fire_modifier = Value  IF_TRUE IS SOME_TEST ELSE VALUE IF FALSE
#             fire_modifier = 5 if self.breaths_fire else 1 # if fire_modifier is 5 == True - else False == 1
#             scale_modifier = self.scaliness / 10
#
#             return base_roll * fire_modifier * scale_modifier
#


# OOP

class Creature:  # blueprint
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def __repr__(self):  # representing obs as strings
        return "Creature {} from level {}".format(
            self.name,
            self.level
        )

    def character_rolls(self):
        return random.randint(1, 12) * self.level


class Wizard(Creature):  # blueprint
    # def __init__(self, name, level):
    #     self.name = name
    #     self.level = level

    # algorithm- formula for who wins - wizard and a creature roll  condition to decide who wins
    # this is an attack method
    def wizard_behavior(self, creature):  # instance method attacking a creature
        print("The wizard {} attacks {}".format(
            self.name, creature.name
        ))

        wizard_roll = self.character_rolls()
        creature_roll = creature.character_rolls()

        print("{} rolls {}".format(self.name, wizard_roll))
        print("{} rolls {}".format(creature.name, creature_roll))

        if wizard_roll > creature_roll:
            print('{} has defeated {}'.format(self.name, creature.name))
            return True  # need to return data in order for creature to be removed
        elif creature_roll > wizard_roll:
            print('{} defeats {}'.format(creature.name, self.name))
            return False  # need to return data in order for creature to be removed


class CutePet(Creature):
    def character_rolls(self):
        base_roll = random.randint(1, 12) * self.level
        return base_roll / 2


class KingOfTheJungle(Creature):
    def __init__(self, name, level, speed, shoots_fire):
        super().__init__(name, level)
        self.speed = speed
        self.shoots_fire = shoots_fire

    def character_rolls(self):
        base_roll = super().character_rolls()
        shoots_fire = 5 if self.shoots_fire else 1
        speed = self.speed / 5

        return base_roll * shoots_fire



