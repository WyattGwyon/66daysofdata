# Soldier
class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    
    def attack(self):
        return self.strength
    
    def receiveDamage(self, damage):    
        self.health -= damage

# Viking
class Viking(Soldier):
    def __init__(self, name, health, strength):
        self.name = name
        super().__init__(health, strength)

    def receiveDamage(self,damage):
        super().receiveDamage(damage)
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        else: 
            return f"{self.name} has died in act of combat" 

    def battleCry(self):
        return "Odin Owns You All!"

# Saxon
class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)
    
    def receiveDamage(self, damage):
        super().receiveDamage(damage)
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return f"A Saxon has died in combat"

import random
class War:
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []
        
    def addViking(self, viking):
        self.vikingArmy.append(viking)
    
    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)
        
    def vikingAttack(self):
        randSaxon = random.choice(self.saxonArmy)
        randViking = random.choice(self.vikingArmy)
        results = randSaxon.receiveDamage(randViking.attack())
        
        if results == f"A Saxon has died in combat":
            self.saxonArmy.remove(randSaxon)
        return results 

    def saxonAttack(self):
        randSaxon = random.choice(self.saxonArmy)
        randViking = random.choice(self.vikingArmy)
        results = randViking.receiveDamage(randSaxon.attack())

        if results == f"{randViking.name} has died in act of combat":
            self.vikingArmy.remove(randViking)
        return results

    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        if len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."