from Entity import Entity
import json
import random
import os


class Enemy(Entity):
    def __init__(self, name, hp=100, attack_value=5, defence_value=1):
        super().__init__(name, hp, attack_value, defence_value)
        self.abilities = {}
        self.behaviors = {}

    def load_abilities(self):
        current_dir = os.path.dirname(__file__)  # Get the directory where this script is located
        file_path = os.path.join(current_dir, 'Enemy_abilities.json')  # Create a path to the JSON file
        with open(file_path, 'r') as f:
            abilities = json.load(f)
        self.abilities.update(abilities)

    def load_behaviors(self):
        current_dir = os.path.dirname(__file__)  # Get the directory where this script is located
        file_path = os.path.join(current_dir, 'Behaviors.json')  # Create a path to the JSON file
        with open(file_path, 'r') as f:
            behaviors = json.load(f)
        self.behaviors.update(behaviors)

    def choose_action(self, target):
        if self.behaviors:
            behavior = random.choices(self.behaviors, weighs=[behavior['chance'] for behavior in self.behaviors], k=1)[0]
            if behavior['action'] == 'attack':
                self.attack(target)
            elif behavior['action'] == 'defend':
                self.defend()
            elif behavior['acion'] == 'ability':
                ability = random.choice(self.abilities)
                self.enemy_use_ability(ability, target)
            else:
                #handle other behaviors
                pass
        else:
            self.attack(target)
    
    def enemy_use_ability(self, ability_index, target):
        super().use_ability(self.abilities, ability_index, target)