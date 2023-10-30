from .Entity import Entity
import json
import os

class Character(Entity):
    def __init__(self, name, hp=100, attack_value=5, defence_value=1):
        super().__init__(name, hp, attack_value, defence_value)
        self.abilities = {}
    
    def load_abilities(self):
        file_path = os.path.join(os.path.dirname(__file__), 'Abilities.json')
        with open(file_path, 'r') as f:
            self.abilities.update(json.load(f))
            
        

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
        ability_names = list(self.abilities.keys())
        ability_name = ability_names[ability_index - 1]  # Convert index to name
        super().use_ability(self.abilities, ability_name, target)
