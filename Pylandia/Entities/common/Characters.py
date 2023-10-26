from Entity import Entity
import json
import os

class Character(Entity):
    def __init__(self, name, hp=100, attack_value=5, defence_value=1):
        super().__init__(name, hp, attack_value, defence_value)
        self.abilities = {}
    
    def load_abilities(self):
        current_dir = os.path.dirname(__file__)  # Get the directory where this script is located
        file_path = os.path.join(current_dir, 'Abilities.json')  # Create a path to the JSON file
        with open(file_path, 'r') as f:
            abilities = json.load(f)
        self.abilities.update(abilities)

    def choose_action(self):
        print("Choose an action:\n1. Attack\n2. Defend\n3. Use Ability")
        choice = input("Enter the number of choice: ")
        return int(choice)
    
    def choose_ability(self):
        ability_names = list(self.abilities.keys())
        print("Choose an ability: ")
        for i, ability in enumerate(ability_names, start=1):
            print(f"{i}. {ability}")
        choice = input("Enter the number of the ability: ")
        return int(choice)
    
    def player_use_ability(self, ability_index, target):
        super().use_ability(self.abilities, ability_index, target)