if __name__ == '__main__':
    from ..entity import Entity
else:
    from Entities.entity import Entity
import json
import os

class Character(Entity):
    def __init__(self, name: str, hp: int = 100, attack_value: int = 5, defence_value: int = 1):
        super().__init__(name, hp, attack_value, defence_value)
        self.abilities: dict[str, dict[str, str|int]] = {}
    
    def load_abilities(self) -> None:
        file_path = os.path.join(os.path.dirname(__file__), 'abilities.json')
        with open(file_path, 'r') as f:
            self.abilities.update(json.load(f))  

    def choose_action(self) -> int:
        print("Choose an action:\n1. Attack\n2. Defend\n3. Use Ability")
        choice = input("Enter the number of choice: ")
        return int(choice)
    
    def choose_ability(self) -> int:
        ability_names = list(self.abilities.keys())
        print("Choose an ability: ")
        for i, ability in enumerate(ability_names, start=1):
            print(f"{i}. {ability}")
        choice = input("Enter the number of the ability: ")
        return int(choice)
    
    def player_use_ability(self, ability_index: int, target: Entity):
        ability_names = list(self.abilities.keys())
        ability_name = ability_names[ability_index - 1]  # Convert index to name
        super().use_ability(self.abilities, ability_name, target)
