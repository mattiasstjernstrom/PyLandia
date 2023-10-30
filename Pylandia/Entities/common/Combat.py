from .Characters import Character
from .Enemies import Enemy

class Combat:
    def __init__(self, player, enemy):
        """
        Initialize the combat with a player and an enemy.
        """
        self.player = player
        self.enemy = enemy
    
    def fight(self):
        """
        Run the combat loop until the player or enemy has been defeated
        """
        while self.player.is_alive and self.enemy.is_alive:
            self.player_turn()
            if not self.enemy.is_alive:
                print(f"{self.enemy.name} has been defeated!")
                break
            self.enemy_turn()
            if not self.player.is_alive:
                print(f"{self.player.name} has been defeated!")
                break

    def player_turn(self):
        """
        The players turn to deal damage.
        """
        print(f"{self.player.name}'s turn")
        choice = self.player.choose_action()
        if choice == 1:
            damage = self.player.attack(self.enemy)
            print(f"{self.player.name} attacked {self.enemy.name} for {damage} damage! {self.enemy.name} has {self.enemy.hp:.2f} HP left")
        elif choice == 2:
            self.player.defend()
        elif choice == 3:
            ability_choice = self.player.choose_ability()
            damage = self.player.player_use_ability(ability_choice, self.enemy)

    def enemy_turn(self):
        """
        The enemy turn to deal damage.
        """
        print(f"{self.enemy.name}'s turn!")
        self.enemy.choose_action(self.player)
        print(f"{self.player.name} has {self.player.hp} HP left.")

def run_game():
    player = Character("Daniel", 100, 10, 5)
    enemy = Enemy("Mattias", 80, 7, 3)

    player.load_abilities()
    enemy.load_abilities()
    enemy.load_behaviors()

    # Start combat
    combat = Combat(player, enemy)
    combat.fight()


if __name__ == "__main__":
    run_game()