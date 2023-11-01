from ..Entities.Characters.characters import Character
from ..Entities.Enemies.enemy import Enemy

class Combat:
    def __init__(self, player: Character, enemy: Enemy):
        """
        Initialize the combat with a player and an enemy.
        """
        self._player = player
        self._enemy = enemy
    
    def fight(self) -> None:
        """
        Run the combat loop until the player or enemy has been defeated
        """
        while self._player.is_alive and self._enemy.is_alive:
            self._player_turn()
            if not self._enemy.is_alive:
                print(f"{self._enemy.name} has been defeated!")
                break
            self._enemy_turn()
            if not self._player.is_alive:
                print(f"{self._player.name} has been defeated!")
                break

    def _player_turn(self) -> None:
        """
        The players turn to deal damage.
        """
        print(f"{self._player.name}'s turn")
        choice = self._player.choose_action()
        if choice == 1:
            damage = self._player.attack(self._enemy)
            print(f"{self._player.name} attacked {self._enemy.name} for {damage} damage! {self._enemy.name} has {self._enemy.hp:.2f} HP left")
        elif choice == 2:
            self._player.defend()
        elif choice == 3:
            ability_choice = self._player.choose_ability()
            damage = self._player.player_use_ability(ability_choice, self._enemy)

    def _enemy_turn(self) -> None:
        """
        The enemy turn to deal damage.
        """
        print(f"{self._enemy.name}'s turn!")
        self._enemy.choose_action(self._player)
        print(f"{self._player.name} has {self._player.hp} HP left.")

def test_combat() -> None:
    player = Character("Daniel", 100, 10, 5)
    enemy = Enemy("Mattias", 80, 7, 3)

    player.load_abilities()
    enemy.load_abilities()
    enemy.load_behaviors()

    # Start combat
    combat = Combat(player, enemy)
    combat.fight()


if __name__ == "__main__":
    test_combat()