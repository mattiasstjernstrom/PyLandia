from ..entity import Entity
import json
import random
import os


class Enemy(Entity):
    def __init__(self, name, hp=100, attack_value=5, defence_value=1):
        super().__init__(name, hp, attack_value, defence_value)
        self.abilities = {}
        self.behaviors = {}

    def load_abilities(self):
        file_path = os.path.join(os.path.dirname(__file__), 'enemy_abilities.json')
        with open(file_path, 'r') as f:
            self.abilities.update(json.load(f))

    def load_behaviors(self):
        file_path = os.path.join(os.path.dirname(__file__), 'behaviors.json')
        with open(file_path, 'r') as f:
            self.behaviors.update(json.load(f))

    def choose_action(self, target):
        behavior_values = list(self.behaviors.values())
        behavior = random.choices(behavior_values, weights=[b['chance'] for b in behavior_values],k=1)[0]
        if behavior['action'] == 'attack':
            self.attack(target)
        elif behavior['action'] == 'defend':
            self.defend()
        elif behavior['action'] == 'ability':
            ability = random.choice(list(self.abilities.keys()))
            self.enemy_use_ability(ability, target)
        else:
            #handle other behaviors
            pass
    
    def enemy_use_ability(self, ability, target):
        super().use_ability(self.abilities, ability, target)