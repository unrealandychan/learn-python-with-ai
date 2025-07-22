
# Lesson 23: Solution

class Player:
    def __init__(self, name):
        self.name = name
        self.__health = 100

    def take_damage(self, amount):
        self.__health -= amount
        if self.__health < 0:
            self.__health = 0
        print(f"{self.name} takes {amount} damage.")

    def heal(self, amount):
        self.__health += amount
        if self.__health > 100:
            self.__health = 100
        print(f"{self.name} heals for {amount}.")

    def get_health(self):
        return self.__health

player1 = Player("Aragorn")
print(f"{player1.name}'s health: {player1.get_health()}")

player1.take_damage(25)
print(f"{player1.name}'s health: {player1.get_health()}")

player1.heal(10)
print(f"{player1.name}'s health: {player1.get_health()}")
