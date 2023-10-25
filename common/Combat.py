from Entity import Entity

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
        damage = self.player.attack(self.enemy)
        print(f"{self.player.name} attacked {self.enemy.name} for {damage:.2f} damage! {self.enemy.name} has {self.enemy.hp:.2f} HP left")
        
    def enemy_turn(self):
        """
        The enemy turn to deal damage.
        """
        print(f"{self.enemy.name}'s turn!")
        damage = self.enemy.attack(self.player)
        print(f"{self.enemy.name} attacked {self.player.name} for {damage:.2f} damage! {self.player.name} has {self.player.hp:.2f} HP left.")


player = Entity("Daniel", 100, 10, 5)
enemy = Entity("Mattias", 80, 7, 3)
combat = Combat(player, enemy)
combat.fight()