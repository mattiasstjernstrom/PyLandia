import random

class Entity:
    def __init__(self, name, hp=100, attack_value=5, defence_value=1):
        self._name = name
        self._hp = hp
        self._attack_value= attack_value
        self._defence_value= defence_value
        self.is_alive = True

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def hp(self):
        return self._hp
    @hp.setter
    def hp(self, new_hp):
        self._hp = new_hp

    @property
    def attack_value(self):
        return self._attack_value
    @attack_value.setter
    def attack_value(self, new_attack_value):
        self._attack_value = new_attack_value

    @property
    def defence_value(self):
        return self._defence_value
    @defence_value.setter
    def defence_value(self, new_defence_value):
        self._defence_value = new_defence_value
    
    def defend(self):
        self.defence_value *= 2
        print(f"{self.name} is defending and has doubled their defence value!")
    
    def attack(self, target): #snor denna från förra arbetet
        base_damage = self.attack_value - target.defence_value
        damage = round(random.uniform(
            max(0.1 * self.attack_value, base_damage) * 0.8,
            max(0.1 * self.attack_value, base_damage) * 1.2))
        target.receive_damage(damage)
        return damage
    
    def receive_damage(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            self._hp = 0
            self.is_alive = False

    def use_ability(self, abilities, ability, target):
        ability = abilities.get(ability)
        if ability is None:
            print(f"Ability {ability} not found.")
            return
        min_damage = ability.get('min_damage', 0)
        max_damage = ability.get('max_damage', 0)
        damage = round(random.uniform(min_damage, max_damage))
        target.receive_damage(damage)
        print(f"{self.name} used {ability['name']} on {target.name} for {damage} damage!")
        return damage
